import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ConsultaService } from '../../services/consulta.service';
import { ClienteSelectorComponent } from '../cliente-selector/cliente-selector.component';
import { ConsultaFormComponent } from '../consulta-form/consulta-form.component';
import { RespuestaViewComponent } from '../respuesta-view/respuesta-view.component';
import { Respuesta } from '../../models/interfaces';

@Component({
  selector: 'app-consulta',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    ClienteSelectorComponent,
    ConsultaFormComponent,
    RespuestaViewComponent
  ],
  templateUrl: './consulta.component.html',
  styleUrls: ['./consulta.component.scss']
})
export class ConsultaComponent {
  clienteId: string = '';
  cargando: boolean = false;
  error: string | null = null;
  respuesta: Respuesta | null = null;

  constructor(private consultaService: ConsultaService, private cdr: ChangeDetectorRef) {}

  onClienteChange(clienteId: string): void {
    this.clienteId = clienteId;
    this.resetConsulta();
  }

  async onSubmitConsulta(consulta: { cliente_id: string; pregunta: string }): Promise<void> {
    console.log('Consulta enviada:', consulta);
    this.cargando = true;
    this.error = null;
    this.respuesta = null;

    try {
      const respuesta = await this.consultaService.consultar(consulta);
      console.log('Respuesta recibida:', respuesta);
      this.respuesta = respuesta;
      console.log('Respuesta:', this.respuesta);
      this.cdr.detectChanges();
      this.cargando = false;
    } catch (error: any) {
      console.error('Error completo:', error);
      if (error.status === 0) {
        this.error = 'No se pudo conectar con el servidor. Verifique que el backend esté corriendo.';
      } else if (error.status === 403) {
        this.error = 'Error de CORS. Verifique la configuración del backend.';
      } else {
        this.error = error.message || 'Error al procesar la consulta. Por favor, intente nuevamente.';
      }
      this.cargando = false;
    }
  }

  private resetConsulta(): void {
    this.cargando = false;
    this.error = null;
    this.respuesta = null;
  }
}
