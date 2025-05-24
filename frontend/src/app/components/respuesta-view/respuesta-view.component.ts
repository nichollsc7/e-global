import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Respuesta } from '../../models/interfaces';

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
}
