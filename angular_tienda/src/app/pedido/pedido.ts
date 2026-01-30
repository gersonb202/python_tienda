import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { PedidoUsuario } from '../model/pedidoUsuario';
import { Router } from '@angular/router';
import { ServicioTienda } from '../servicio-tienda';

@Component({
  selector: 'app-pedido',
  imports: [FormsModule, CommonModule],
  templateUrl: './pedido.html',
  styleUrl: './pedido.css',
})
export class Pedido {

  pedido: PedidoUsuario = {}

  constructor(private router: Router, private servicioTienda: ServicioTienda) { }

  finalizarPedido() {
    const form = document.querySelector('form') as HTMLFormElement
    if (form.checkValidity()) {

      this.servicioTienda.registrarPedido(this.pedido).subscribe({
        next: (res) => {
          console.log('Respuesta del servidor:', res);
          if (res == "ok") {
            alert("✅ Pedido registrado exitosamente");
            this.router.navigate(["vinos"]);
          } else if (res.error) {
            alert("❌ Error: " + res.error);
          } else {
            alert("Respuesta inesperada del servidor");
          }
        },
        error: (err) => {
          console.error('Error al registrar pedido:', err);
          alert("❌ Error al procesar el pedido. Por favor, intenta de nuevo.");
        }
      });

    } else {
      form.reportValidity()
    }
  }

}
