import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Cliente } from '../models/interfaces';

@Injectable({
  providedIn: 'root'
})
export class ClienteService {
  private clientes: Cliente[] = [
    { id: '1', nombre: 'Cliente A' },
    { id: '2', nombre: 'Cliente B' },
    { id: '3', nombre: 'Cliente C' }
  ];

  constructor() { }

  getClientes(): Observable<Cliente[]> {
    return of(this.clientes);
  }

  getClienteById(id: string): Observable<Cliente | undefined> {
    return of(this.clientes.find(cliente => cliente.id === id));
  }
} 