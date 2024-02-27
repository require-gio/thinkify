import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { ToolbarModule } from 'primeng/toolbar';
import { ButtonModule } from 'primeng/button';
import { InputTextModule } from 'primeng/inputtext';
import { Note, NoteService } from '../generated';

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [ButtonModule, InputTextModule, ToolbarModule, RouterModule],
  templateUrl: './layout.component.html',
  styleUrl: './layout.component.scss',
})
export class LayoutComponent {
  constructor(
    private noteService: NoteService,
    private router: Router,
  ) {}

  public addNewNote() {
    const note: Note = { name: 'Unnamed Note' };
    this.noteService.createNewNote(note).subscribe((res: string) => {
      console.log('New note created:', res);
      // route to the new note
      this.router.navigate(['/note/detail', res]);
    });
  }
}
