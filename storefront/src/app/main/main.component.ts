import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { Country, City, Store, Category, My_Item, My_Order, Supplier, Delivery, Customer} from '../shared/models/models';
@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public login: any = '';
  public password: any = '';

  public logged = false;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
  }

  auth(){
    if(this.login !== '' && this.password !==''){
      this.provider.auth(this.login, this.password).then(r=>{
        localStorage.setItem('token', r.token);
        this.logged = true;
      });
    }
  }

  logout(){
    this.provider.logout().then(res=>{
      localStorage.clear();
      this.logged = false;
    })
  }

}
