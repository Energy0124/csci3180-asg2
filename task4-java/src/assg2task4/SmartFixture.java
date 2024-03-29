/*
 *  CSCI3180 Principles of Programming Languages
 *
 *  --- Declaration ---
 *
 *  I declare that the assignment here submitted is original except for source
 *  material explicitly acknowledged. I also acknowledge that I am aware of
 *  University policy and regulations on honesty in academic work, and of the
 *  disciplinary guidelines and procedures applicable to breaches of such policy
 *  and regulations, as contained in the website
 *  http://www.cuhk.edu.hk/policy/academichonesty/
 *
 *  Assignment 2
 *  Name : Ling Leong
 *  Student ID : 1155062557
 *  Email Addr : alanalan0124@yahoo.com.hk
 */

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
public class SmartFixture extends Fixture {
    protected double battery_capacity;
    protected double battery_remaining;
    public SmartFixture(String Name, double Weight, int Position, double Battery_capacity){
        super(Name, Weight, Position);
        this.battery_capacity = Battery_capacity;
        this.battery_remaining = Battery_capacity;
    }
    public void ChargeBattery(double Amount){
        this.battery_remaining += Amount;
        if(this.battery_remaining >this.battery_capacity){
            this.battery_remaining = this.battery_capacity;
        }
        System.out.println(this.name + " was charged " + Amount + " units of battery." );
    }
    public double ConsumeBattery(double Amount){
        if(Amount >= this.battery_remaining){
            return -1;
        }
        else{
            this.battery_remaining -= Amount;
            return this.battery_remaining;
        }
    }
    public void MoveTo(Room Destination){
        int distance = Math.abs(this.position - Destination.GetPosition());
        double battery_consumed = distance * this.weight;
        if (this.ConsumeBattery(battery_consumed) > 0){
            this.position = Destination.GetPosition();
            System.out.println(this.name + " moved to " + Destination.GetName() + ".");
            System.out.println(this.name + " consumed " + battery_consumed + " battery." );
        }
        else{
            System.out.println("Not enough battery to move!");
        }
    }
}
