import { Component, signal, Signal } from '@angular/core';
import { ActivatedRoute, RouterLink } from "@angular/router";
import { Vino } from '../model/vino';
import { ServicioTienda } from '../servicio-tienda';

@Component({
  selector: 'app-detalles',
  imports: [RouterLink],
  templateUrl: './detalles.html',
  styleUrl: './detalles.css',
})
export class Detalles {

  id:number = -1
  vino = signal<Vino>({})

  constructor(private servicioTienda:ServicioTienda, private activatedRoute:ActivatedRoute){}

  ngOnInit():void{
    // Lo que queremos es recibir la id del vino seleccionado
    // en el listado de productos
    this.id = Number(this.activatedRoute.snapshot.paramMap.get("id"))
    //alert("id recibido: " + this.id)
    // pedir al servidor los datos del registro de id del vino
    this.servicioTienda.obtenerVinoPorId(this.id).subscribe(res => {
      this.vino.set(res)
    })
  }
  agregarProductoAlCarrito() {
    this.servicioTienda.agregarAlCarrito(this.vino().id, 1).subscribe(res => {
      alert(res)
    })
  }
  

}
