import {
  Component,
  ChangeDetectorRef,
  ViewEncapsulation,
  ChangeDetectionStrategy,
  Output,
  EventEmitter,
  Input,
} from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { BlockUIModule } from 'primeng/blockui';
import { DialogModule } from 'primeng/dialog';
import { TabViewModule } from 'primeng/tabview';
import { EditorModule } from 'primeng/editor';
import { TableModule } from 'primeng/table';
import { CommonModule } from '@angular/common';
import RecordRTC from 'recordrtc';
import {
  FormControl,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
} from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { AudioRecordingService } from '../../services/audio-recording.service';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';
import { Subscription } from 'rxjs';
import { AiService } from '../../generated';

@Component({
  selector: 'app-audio-recorder-button',
  standalone: true,
  imports: [
    CommonModule,
    BlockUIModule,
    DialogModule,
    ReactiveFormsModule,
    EditorModule,
    TabViewModule,
    HttpClientModule,
    FormsModule,
    ButtonModule,
    TableModule,
  ],
  templateUrl: './audio-recorder-button.component.html',
  styleUrl: './audio-recorder-button.component.scss',
  encapsulation: ViewEncapsulation.Emulated,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class AudioRecorderButtonComponent {
  public dialogVisible: boolean = false;
  public isRecording: boolean = false;
  audioBlobUrl: SafeUrl | null = null;
  audioBlob: any;
  audioName: string = '';
  audioTime: string = '';
  subscriptions: Subscription[] = [];

  @Input({ required: true }) noteId: string | null = null;
  @Output() onTranscriptionCreated: EventEmitter<string> =
    new EventEmitter<string>();

  formGroup: FormGroup = new FormGroup({
    transcribedText: new FormControl(),
  });

  constructor(
    private cdRef: ChangeDetectorRef,
    private audioRecordingService: AudioRecordingService,
    private aiService: AiService,
    private sanitizer: DomSanitizer,
  ) {
    this.subscriptions.push(
      this.audioRecordingService.recordingFailed().subscribe(() => {
        this.isRecording = false;
        this.cdRef.detectChanges();
      }),
    );

    this.subscriptions.push(
      this.audioRecordingService.getRecordedTime().subscribe((time) => {
        this.audioTime = time;
        this.cdRef.detectChanges();
      }),
    );

    this.subscriptions.push(
      this.audioRecordingService.getRecordedBlob().subscribe((data) => {
        this.audioBlob = data.blob;
        this.audioName = data.title;
        this.audioBlobUrl = this.sanitizer.bypassSecurityTrustUrl(
          URL.createObjectURL(data.blob),
        );
        this.cdRef.detectChanges();
      }),
    );
  }

  ngOnInit() {}

  public openRecorderDialog() {
    this.dialogVisible = true;
  }

  public closeRecorderDialog() {
    this.dialogVisible = false;
  }

  public async startRecording() {
    this.isRecording = true;
    let stream = await navigator.mediaDevices.getUserMedia({
      video: true,
      audio: true,
    });
    let recorder = new RecordRTC.RecordRTCPromisesHandler(stream, {
      type: 'audio',
    });
    recorder.startRecording();

    const sleep = (m: any) => new Promise((r) => setTimeout(r, m));
    await sleep(3000);

    await recorder.stopRecording();
    let blob = await recorder.getBlob();
    RecordRTC.invokeSaveAsDialog(blob);
  }

  public stopRecording() {
    setTimeout(() => {
      this.isRecording = false;
      this.cdRef.markForCheck();
    }, 0);
  }

  startAudioRecording() {
    if (!this.isRecording) {
      this.isRecording = true;
      this.audioRecordingService.startRecording();
    }
  }

  abortAudioRecording() {
    if (this.isRecording) {
      this.isRecording = false;
      this.audioRecordingService.abortRecording();
    }
  }

  stopAudioRecording() {
    if (this.isRecording) {
      this.audioRecordingService.stopRecording();
      this.isRecording = false;
    }
  }

  clearAudioRecordedData() {
    this.audioBlobUrl = null;
  }

  downloadAudioRecordedData() {
    this._downloadFile(this.audioBlob, 'audio/mp3', this.audioName);
  }

  transcribeAudio() {
    const blob = new Blob([this.audioBlob], { type: 'audio/mp3' });
    this.aiService
      .transcribeAudioForNote(this.noteId!, blob)
      .subscribe((transcription) => {
        this.onTranscriptionCreated.emit(transcription);
        this.closeRecorderDialog();
      });
  }

  ngOnDestroy(): void {
    this.abortAudioRecording();
    this.subscriptions.forEach((subscription) => {
      subscription.unsubscribe();
    });
  }

  _downloadFile(data: any, type: string, filename: string): any {
    const blob = new Blob([data], { type: type });
    const url = window.URL.createObjectURL(blob);
    //this.video.srcObject = stream;
    //const url = data;
    const anchor = document.createElement('a');
    anchor.download = filename;
    anchor.href = url;
    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);
  }
}
