import { Component, OnInit, HostListener } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule, RouterOutlet } from '@angular/router';
import { ClienteSelectorComponent } from './components/cliente-selector/cliente-selector.component';
import { ConsultaFormComponent } from './components/consulta-form/consulta-form.component';
import { RespuestaViewComponent } from './components/respuesta-view/respuesta-view.component';
import { ConsultaService } from './services/consulta.service';
import { Consulta, Respuesta } from './models/interfaces';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    RouterModule,
    RouterOutlet,
    ClienteSelectorComponent,
    ConsultaFormComponent,
    RespuestaViewComponent
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  clienteId: string = '';
  cargando: boolean = false;
  error: string | null = null;
  respuesta: Respuesta | null = null;

  constructor(private consultaService: ConsultaService) {}

  @HostListener('document:mousemove', ['$event'])
  onMouseMove(event: MouseEvent) {
    const x = event.clientX;
    const y = event.clientY;
    document.documentElement.style.setProperty('--mouse-x', `${x}px`);
    document.documentElement.style.setProperty('--mouse-y', `${y}px`);
  }

  ngOnInit() {
    // Inicializar la posición del mouse en el centro
    document.documentElement.style.setProperty('--mouse-x', '50%');
    document.documentElement.style.setProperty('--mouse-y', '50%');
  }

  onClienteChange(clienteId: string): void {
    this.clienteId = clienteId;
    this.resetConsulta();
  }

  async onSubmitConsulta(consulta: Consulta): Promise<void> {
    this.cargando = true;
    this.error = null;
    this.respuesta = null;

    try {
      const respuesta = await this.consultaService.consultar(consulta);
      this.respuesta = respuesta;
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
