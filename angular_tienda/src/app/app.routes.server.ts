import { RenderMode, ServerRoute } from '@angular/ssr';

export const serverRoutes: ServerRoute[] = [
  
  { path: 'carrito', renderMode: RenderMode.Server},

  { path: 'detalles/:id', renderMode: RenderMode.Server},

  { path: 'pedido', renderMode: RenderMode.Server},

  { path: 'vinos', renderMode: RenderMode.Server},
  
  {

    path: '**',
    renderMode: RenderMode.Prerender
  }

];
