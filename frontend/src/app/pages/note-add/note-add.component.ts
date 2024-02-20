import {
  Component,
  ChangeDetectorRef,
  ViewEncapsulation,
  ChangeDetectionStrategy,
} from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { BlockUIModule } from 'primeng/blockui';
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
import { AudioRecorderButtonComponent } from '../../components/audio-recorder-button/audio-recorder-button.component';

@Component({
  selector: 'app-note-detail',
  standalone: true,
  templateUrl: './note-detail.component.html',
  styleUrl: './note-detail.component.scss',
  encapsulation: ViewEncapsulation.Emulated,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [
    CommonModule,
    BlockUIModule,
    ReactiveFormsModule,
    EditorModule,
    TabViewModule,
    HttpClientModule,
    FormsModule,
    ButtonModule,
    TableModule,
    AudioRecorderButtonComponent,
  ],
})
export class NoteDetailComponent {
  public isRecording: boolean = false;
  audioBlobUrl: SafeUrl | null = null;
  audioBlob: any;
  audioName: string = '';
  audioTime: string = '';

  formGroup: FormGroup = new FormGroup({
    transcribedText: new FormControl(),
  });

  constructor(
    private cdRef: ChangeDetectorRef,
    private audioRecordingService: AudioRecordingService,
    private sanitizer: DomSanitizer,
  ) {}

  ngOnInit() {}

  startAudioRecording() {
    if (!this.isRecording) {
      this.isRecording = true;
      this.audioRecordingService.startRecording();
    }
  }
}
