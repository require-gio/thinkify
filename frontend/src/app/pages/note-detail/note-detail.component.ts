import {
  Component,
  ChangeDetectorRef,
  ViewEncapsulation,
  ChangeDetectionStrategy,
  OnDestroy,
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
import { ActivatedRoute } from '@angular/router';
import { Note, NoteService } from '../../generated';
import {
  Observable,
  Subscription,
  debounceTime,
  distinctUntilChanged,
  map,
} from 'rxjs';

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
export class NoteDetailComponent implements OnDestroy {
  id: string | null = null;
  public note$: Observable<Note> | null = null;

  public formGroupSubscription: Subscription | null = null;
  formGroup: FormGroup = new FormGroup({
    rawText: new FormControl(),
  });

  constructor(
    private cdRef: ChangeDetectorRef,
    private noteService: NoteService,
    private audioRecordingService: AudioRecordingService,
    private sanitizer: DomSanitizer,
    private route: ActivatedRoute,
  ) {}

  ngOnInit() {
    this.id = this.route.snapshot.paramMap.get('id') ?? '';
    this.note$ = this.noteService.getNoteById(this.id).pipe(
      map((note: Note) => {
        this.formGroup.controls['rawText'].setValue(note.rawText);
        return note;
      }),
    );

    // save raw note in backend every 3 seconds, only if changed
    this.formGroupSubscription = this.formGroup.valueChanges
      .pipe(debounceTime(3000), distinctUntilChanged())
      .subscribe((data) => {
        console.log(data['rawText']);
        this.noteService
          .updateNoteById(this.id!, { rawText: data['rawText'] })
          .subscribe((val) => {
            console.log(val);
          });
      });
  }

  ngOnDestroy(): void {
    this.formGroupSubscription?.unsubscribe();
  }
}
