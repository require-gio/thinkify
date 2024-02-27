export * from './ai.service';
import { AiService } from './ai.service';
export * from './cors.service';
import { CorsService } from './cors.service';
export * from './note.service';
import { NoteService } from './note.service';
export const APIS = [AiService, CorsService, NoteService];
