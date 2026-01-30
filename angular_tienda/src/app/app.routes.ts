import { Routes } from '@angular/router';
import { Vinos } from './vinos/vinos';
import { Carrito } from './carrito/carrito';
import { Usuarios } from './usuarios/usuarios';
import { Detalles } from './detalles/detalles';
import { Pedido } from './pedido/pedido';

export const routes: Routes = [
    {path: "", redirectTo: "vinos", pathMatch: "full"},
    { path: "vinos", component : Vinos },
    { path: "carrito", component : Carrito },
    { path: "usuarios", component : Usuarios },
    { path: "detalles/:id", component : Detalles },
    { path: "pedido", component : Pedido }
];
