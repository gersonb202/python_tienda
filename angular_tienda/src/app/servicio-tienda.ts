import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Vino } from './model/vino';
import { PedidoUsuario } from './model/pedidoUsuario';

@Injectable({
  providedIn: 'root',
})
export class ServicioTienda {

  ruta_servicios_rest = "http://localhost:5000/rest/"

  // aquí vamos a lanzar todas las comunicaciones con el servidor

  // estoy pidiendo un recurso ya preparado que me permite hacer ajax
  // para comunicarse con un servidor
  constructor(private http: HttpClient) { }

  obtenerVinos() {
    return this.http.get(this.ruta_servicios_rest + "vinos")
  }

  obtenerUsuarios() {
    return this.http.get(this.ruta_servicios_rest + "usuarios")
  }

  obtenerVinoPorId(id: number): Observable<Vino> {
    return this.http.get<Vino>(this.ruta_servicios_rest + "obtener_vino_por_id?id=" + id)
  }

  agregarAlCarrito(id: number | undefined, cantidad: number) {
    return this.http.post<any>(this.ruta_servicios_rest + "agregar_producto_a_carrito",
      {
        "id": id,
        "cantidad": cantidad
      }, { withCredentials: true })
  }

  obtenerProductosCarrito() {
    return this.http.get<any>(this.ruta_servicios_rest + "obtener_productos_carrito", { withCredentials: true })
  }

  obtenerProductosCarritoParaListado() {
    return this.http.get<any>(this.ruta_servicios_rest + "obtener_productos_carrito_para_listado", { withCredentials: true })
  }

  vaciarCarrito(): Observable<string> {
    return this.http.get<string>(this.ruta_servicios_rest + "vaciar_carrito", { withCredentials: true })
  }

  registrarPedido(pedido: PedidoUsuario): Observable<any> {
    return this.http.post<any>(this.ruta_servicios_rest + "registrar_pedido", pedido, { withCredentials: true })
  }

}
