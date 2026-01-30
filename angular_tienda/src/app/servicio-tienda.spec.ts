import { TestBed } from '@angular/core/testing';

import { ServicioTienda } from './servicio-tienda';

describe('ServicioTienda', () => {
  let service: ServicioTienda;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ServicioTienda);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
