import { Component, signal } from '@angular/core';
import { ServicioTienda } from '../servicio-tienda';
import { Vino } from '../model/vino';

@Component({
  selector: 'app-usuarios',
  imports: [],
  templateUrl: './usuarios.html',
  styleUrl: './usuarios.css',
})
export class Usuarios {

  usuarios = signal<Vino[]>([])

  constructor(private servicioTienda:ServicioTienda){}

  ngOnInit(){
    this.servicioTienda.obtenerUsuarios().subscribe((res:any) => {
      this.usuarios.set(res)
    })
  }

}
