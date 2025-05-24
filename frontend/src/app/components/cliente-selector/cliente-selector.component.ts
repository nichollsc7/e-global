import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-cliente-selector',
  templateUrl: './cliente-selector.component.html',
  styleUrls: ['./cliente-selector.component.scss'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class ClienteSelectorComponent implements OnInit {
  clientes = [
    { id: 'cliente1', nombre: 'Cliente 1' },
    { id: 'cliente2', nombre: 'Cliente 2' },
    { id: 'cliente3', nombre: 'Cliente 3' }
  ];
  clienteSeleccionado: string = '';
  @Output() clienteChange = new EventEmitter<string>();

  constructor() { }

  ngOnInit(): void {
  }

  onClienteChange(event: Event): void {
    const select = event.target as HTMLSelectElement;
    this.clienteSeleccionado = select.value;
    this.clienteChange.emit(this.clienteSeleccionado);
  }
}
