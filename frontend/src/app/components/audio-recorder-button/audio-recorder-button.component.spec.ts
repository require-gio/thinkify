import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AudioRecorderButtonComponent } from './audio-recorder-button.component';

describe('AudioRecorderButtonComponent', () => {
  let component: AudioRecorderButtonComponent;
  let fixture: ComponentFixture<AudioRecorderButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AudioRecorderButtonComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AudioRecorderButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
