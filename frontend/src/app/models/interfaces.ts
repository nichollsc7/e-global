export interface Cliente {
  id: string;
  nombre: string;
}

export interface Consulta {
  cliente_id: string;
  pregunta: string;
}

export interface ResponseMetadata {
  prompt_feedback?: any;
  finish_reason?: string;
  model_name?: string;
  safety_ratings?: any[];
}

export interface Respuesta {
  content: string;
  response_metadata?: ResponseMetadata;
  type?: string;
  name?: string | null;
  id?: string;
  example?: boolean;
  tool_calls?: any[];
  invalid_tool_calls?: any[];
  usage_metadata?: any;
  additional_kwargs?: any;
}

export interface EstadoConsulta {
  cargando: boolean;
  error: string | null;
  respuesta: Respuesta | null;
} 