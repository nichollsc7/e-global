import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of, throwError, firstValueFrom } from 'rxjs';
import { catchError, switchMap, tap } from 'rxjs/operators';
import { Respuesta } from '../models/interfaces';

@Injectable({
  providedIn: 'root'
})
export class ConsultaService {
  private apiUrl = 'http://localhost:8000/api/v1/consulta';
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    })
  };

  private readonly CLIENTES_VALIDOS = ['cliente1', 'cliente2', 'cliente3'];

  constructor(private http: HttpClient) {}

  async consultar(data: { cliente_id: string; pregunta: string }): Promise<Respuesta> {
    if (!this.CLIENTES_VALIDOS.includes(data.cliente_id)) {
      throw new Error('El cliente_id debe ser uno de: cliente1, cliente2, cliente3');
    }
    const response = await firstValueFrom(
      this.http.post<{ respuesta: Respuesta }>(this.apiUrl, data, this.httpOptions)
    );
    console.log('Respuesta de la API:', response);
    return response.respuesta;
  }
}
