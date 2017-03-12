package assg2task4;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author kenchan
 */
public class Attendant {
    protected String name;
    protected double weight;
    protected double wealth;
    protected int position;
    public Attendant(String Name, double Weight, double Wealth, int Position){
        this.name = Name;
        this.weight = Weight;
        this.wealth = Wealth;
        this.position = Position;
    }
    public double MoveTo(Room Destination){
        int distance = Math.abs(this.position - Destination.GetPosition());
        double calories_consumed = distance * this.weight;
        this.position = Destination.GetPosition();
        System.out.println(this.name + " moved to " + Destination.GetName() + "." );
        return calories_consumed;
    }
    public double MoveTo(Fixture Destination){
        int distance = Math.abs(this.position - Destination.GetPosition());
        double calories_consumed = distance * this.weight;
        this.position = Destination.GetPosition();
        System.out.println(this.name + " moved to " + Destination.GetName() + "." );
        return calories_consumed;
    }
    public double MoveTo(Room Destination, Fixture Obj){
        int distance = Math.abs(Obj.GetPosition() - Destination.GetPosition());
        double calories_consumed = distance * Obj.GetWeight();
        Obj.position = Destination.GetPosition();
        System.out.println(Obj.name + " was moved to " + Destination.GetName() + "." );
        return calories_consumed;
    }
    public void CarryTo(Fixture Obj, Room Destination){
        double calories_consumed = 0;
        //Move the attendant to the object first
        calories_consumed += this.MoveTo(Obj);
        //Move the attendant to the destination
        calories_consumed += this.MoveTo(Destination);
        //Move the object to the destination 
        calories_consumed += this.MoveTo(Destination, Obj);
        //Print calories consumed
        System.out.println(this.name + " consumed " + calories_consumed + " calories." );
    }
    public String GetName(){
        return this.name;
    }
    public int GetPosition(){
        return this.position;
    }
    public double GetWeight(){
        return this.weight;
    }
    public double Pay(double Amount){
        if (Amount <= this.wealth){
            this.wealth -= Amount;
            System.out.println(this.name + " paid " + Amount + " dollars.");
            return Amount;
        }
        else{
            return -1;
        }
    }
}
