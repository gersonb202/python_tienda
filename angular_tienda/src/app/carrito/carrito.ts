import { Component, signal } from '@angular/core';
import { ServicioTienda } from '../servicio-tienda';
import { VinoCarrito } from '../model/vinoCarrito';
import { Router, RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-carrito',
  imports: [CommonModule, RouterLink],
  templateUrl: './carrito.html',
  styleUrl: './carrito.css',
})
export class Carrito {
  // Pedir los productos del carrito al servidor
  // y mostrarlos en carrito.html

  vinosCarrito = signal<VinoCarrito[]>([]);

  constructor(private router: Router, private servicioTienda: ServicioTienda) { }

  ngOnInit(): void {
    this.listarProductosCarrito()
  }

  listarProductosCarrito() {
    this.servicioTienda.obtenerProductosCarritoParaListado().subscribe(res => {
      console.log('Productos del carrito:', res);
      this.vinosCarrito.set(res);
    });
  }

  vaciarCarrito() {
    this.servicioTienda.vaciarCarrito().subscribe(res => {
      alert(res)
      this.listarProductosCarrito()
    })
  }

  realizarPedido() {
    if (this.vinosCarrito().length > 0) {
      this.router.navigate(["pedido"])
    } else {
      alert("Debes agregar productos al carrito para poder hacer un pedido")
    }
  }

  calcularSubtotal(): number {
    return this.vinosCarrito().reduce((total, item) => {
      return total + ((item.vino.precio || 0) * item.cantidad);
    }, 0);
  }

}
