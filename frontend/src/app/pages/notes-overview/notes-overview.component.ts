import { Component } from '@angular/core';
import { CardModule } from 'primeng/card';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { Note, NoteMetaData, NoteService } from '../../generated';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-notes-overview',
  standalone: true,
  imports: [CardModule, CommonModule, RouterModule],
  templateUrl: './notes-overview.component.html',
  styleUrl: './notes-overview.component.scss',
})
export class NotesOverviewComponent {
  notes$: Observable<NoteMetaData[]>;

  constructor(public noteService: NoteService) {
    this.notes$ = noteService.getAllNotes();
  }

  trackByNoteId(index: number, note: NoteMetaData): number | undefined {
    return note.id;
  }
}
