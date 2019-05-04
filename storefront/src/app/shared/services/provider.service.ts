import { Injectable, EventEmitter } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { Country, City, Store, Category, My_Item, My_Order, Supplier, Delivery, Customer, IAuthResponse} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService  extends MainService{

  constructor(http: HttpClient) {
    super(http);
   }
   


   auth(login: any, password: any):Promise<IAuthResponse>{
    return this.post('http://127.0.0.1:8000/api/login/',{
   username: login,
   password: password
    });
  }

  logout(): Promise<any>{
    return this.post('http://127.0.0.1:8000/api/logout/',{

    });
  }
}
