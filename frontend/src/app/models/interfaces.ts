export interface Cliente {
  id: string;
  nombre: string;
}

export interface Consulta {
  cliente_id: string;
  pregunta: string;
}

export interface Respuesta {
  respuesta: string;
  documento_fuente?: string;
  timestamp: string;
}

export interface EstadoConsulta {
  cargando: boolean;
  error: string | null;
  respuesta: Respuesta | null;
} 