import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

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

  consultar(data: { cliente_id: string; pregunta: string }): Observable<any> {
    if (!this.CLIENTES_VALIDOS.includes(data.cliente_id)) {
      return throwError(() => new Error('El cliente_id debe ser uno de: cliente1, cliente2, cliente3'));
    }

    return this.http.post(this.apiUrl, data, this.httpOptions).pipe(
      catchError(error => {
        console.error('Error en la consulta:', error);
        return throwError(() => new Error(error.error?.message || 'Error al procesar la consulta'));
      })
    );
  }
}
