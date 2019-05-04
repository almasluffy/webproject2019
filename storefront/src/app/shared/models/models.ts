

export interface IAuthResponse{
    token: string;
 }

 export interface Country{
     id: number;
     name: string;
     capital: string;
     currency: string;

 }

 export interface City{
    id: number;
    name: string;

}
export interface Store{
    id: number;
    name: string;

}
export interface Category{
    id: number;
    name: string;
    description: Text;

}
export interface Supplier{
    id: number;
    name: string;
    s_name: string;
    phone_number: string;
    company_name: string;
}
export interface Delivery{
    id: number;
    name: string;
    s_name: string;
    company_name: String;

}
export interface Customer {
    id: number;
    name: string;
    s_name: string;
    phone_number: string;
    qiwi_card: string;
    credit_cad: string;
    address: string;
}

export interface My_Order {
    id: number;
    order_price: number;
    item_count: number;
    ship_date: Date;
    status: String;
    transportaion_cost: number;
}

export interface My_Item {
    id: number;
    name: string;
    description: Text;
    count: number;
    added_date: Date;
    price: number;
}