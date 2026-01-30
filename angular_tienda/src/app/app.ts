import { Component, signal } from '@angular/core';
import { Router, RouterOutlet, RouterLink } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {

  // En angular tenemos los servicios,
  // un servicio es un recurso que se puede pedir
  // desde cualquier compone
  constructor(private router:Router){

  }
  
  mostrar_vinos(){
    this.router.navigate(["vinos"])
  }
  mostrar_carrito(){
    this.router.navigate(["carrito"])
  }
  mostrar_usuarios(){
    this.router.navigate(["usurios"])
  }
}
