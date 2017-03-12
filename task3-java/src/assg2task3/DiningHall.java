package assg2task3;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author kenchan
 */
public class DiningHall extends Room {
    protected double dinner_price;
    public DiningHall(String Name, int Position, double Dinner_price){
        super(Name, Position);
        this.dinner_price = Dinner_price;
    }
    public void ServerDinnerTo(Attendant Obj){
        if (Obj.GetPosition()==this.position){
            if (Obj.Pay(this.dinner_price)>=0){
                System.out.println(Obj.GetName() + " finished the dinner.");
            }
            else{
                System.out.println(Obj.GetName() + " didn't have enough money.");
            }
        }
        else{
            System.out.println(Obj.GetName() + " was too far away to be served.");
        }
    }
}
