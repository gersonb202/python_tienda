import { Component, signal } from '@angular/core';
import { ServicioTienda } from '../servicio-tienda';
import { Vino } from '../model/vino';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-vinos',
  imports: [CommonModule],
  templateUrl: './vinos.html',
  styleUrl: './vinos.css',
})
export class Vinos {

  saludo:string = "hola"
  // asi se declara un array de objetos de la clase Vino en ts
  vinos = signal<Vino[]>([]) 

  constructor(private servicioTienda:ServicioTienda, private router:Router){}

  ngOnInit(){
    this.servicioTienda.obtenerVinos().subscribe((res: any) => {
      this.vinos.set(res)
    })
  }

  verDetalles(v:Vino){
    this.router.navigate(["detalles", v.id])
  }

}
