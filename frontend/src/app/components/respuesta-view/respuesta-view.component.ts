import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Respuesta } from '../../models/interfaces';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

@Component({
  selector: 'app-respuesta-view',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './respuesta-view.component.html',
  styleUrl: './respuesta-view.component.scss'
})
export class RespuestaViewComponent {
  @Input() respuesta: Respuesta | null = null;
  @Input() error: string | null = null;
  @Input() cargando: boolean = false;

  constructor(private sanitizer: DomSanitizer) {}

  get modelName(): string | undefined {
    return this.respuesta && this.respuesta.response_metadata
      ? this.respuesta.response_metadata.model_name
      : undefined;
  }

  get safeContent(): SafeHtml | null {
    console.log('Respuesta:', this.respuesta);
    if (!this.respuesta?.content) return null;
    const contentWithBreaks = this.respuesta.content.replace(/\n/g, '<br>');
    return this.sanitizer.bypassSecurityTrustHtml(contentWithBreaks);
  }
}
