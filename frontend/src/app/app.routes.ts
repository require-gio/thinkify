import { Routes } from '@angular/router';
import { LayoutComponent } from './layout/layout.component';
import { NotesOverviewComponent } from './pages/notes-overview/notes-overview.component';
import { NoteDetailComponent } from './pages/note-detail/note-detail.component';

export const routes: Routes = [
  {
    path: '',
    component: LayoutComponent,
    children: [
      {
        path: '',
        component: NotesOverviewComponent,
      },
      {
        path: 'note',
        children: [
          {
            path: 'detail/:id',
            component: NoteDetailComponent,
          },
        ],
      },
    ],
  },
];
