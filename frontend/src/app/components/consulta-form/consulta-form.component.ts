import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Consulta } from '../../models/interfaces';

@Component({
  selector: 'app-consulta-form',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './consulta-form.component.html',
  styleUrl: './consulta-form.component.scss'
})
export class ConsultaFormComponent {
  @Input() clienteId: string = '';
  @Input() cargando: boolean = false;
  @Output() submitConsulta = new EventEmitter<Consulta>();

  pregunta: string = '';

  onSubmit(): void {
    if (this.clienteId && this.pregunta.trim()) {
      this.submitConsulta.emit({
        cliente_id: this.clienteId,
        pregunta: this.pregunta.trim()
      });
      this.pregunta = '';
    }
  }
}
