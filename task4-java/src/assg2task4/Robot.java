/*
 * # CSCI3180 Principles of Programming Languages
 * #
 * # --- Declaration ---
 * #
 * # I declare that the assignment here submitted is original except for source
 * # material explicitly acknowledged. I also acknowledge that I am aware of
 * # University policy and regulations on honesty in academic work, and of the
 * # disciplinary guidelines and procedures applicable to breaches of such policy
 * # and regulations, as contained in the website
 * # http://www.cuhk.edu.hk/policy/academichonesty/
 * #
 * # Assignment 2
 * # Name : Ling Leong
 * # Student ID : 1155062557
 * # Email Addr : alanalan0124@yahoo.com.hk
 */

package assg2task4;

/**
 * Created by Energy on 3/12/2017.
 */
public class Robot {
    protected String name;
    protected double weight;
    protected double battery_capacity;
    protected double battery_remaining;
    protected int position;

    public Robot(String Name, double Weight, int Position, double Battery_capacity) {
        this.name = Name;
        this.weight = Weight;
        this.battery_capacity = Battery_capacity;
        this.battery_remaining = Battery_capacity;
        this.position = Position;
    }

    public double MoveTo(Room Destination) {
        int distance = Math.abs(this.position - Destination.GetPosition());
        double battery_consumed = distance * this.weight;
        if (this.ConsumeBattery(battery_consumed) > 0) {
            this.position = Destination.GetPosition();
            System.out.println(this.name + " moved to " + Destination.GetName() + ".");
        } else {
            System.out.println("Not enough battery to move!");
        }
        return battery_consumed;
    }

    public double MoveTo(Fixture Destination) {
        int distance = Math.abs(this.position - Destination.GetPosition());
        double battery_consumed = distance * this.weight;
        if (this.ConsumeBattery(battery_consumed) > 0) {
            this.position = Destination.GetPosition();
            System.out.println(this.name + " moved to " + Destination.GetName() + ".");
        } else {
            System.out.println("Not enough battery to move!");
        }
        return battery_consumed;
    }

    public double MoveTo(Room Destination, Fixture Obj) {
        int distance = Math.abs(Obj.GetPosition() - Destination.GetPosition());
        double battery_consumed = distance * Obj.GetWeight();
        if (this.ConsumeBattery(battery_consumed) > 0) {
            Obj.position = Destination.GetPosition();
            System.out.println(Obj.name + " was moved to " + Destination.GetName() + ".");
        } else {
            System.out.println("Not enough battery to move!");
        }
        return battery_consumed;
    }

    public void CarryTo(Fixture Obj, Room Destination) {
        double battery_consumed = 0;
        int robot_distance = Math.abs(this.position - Obj.GetPosition()) + Math.abs(Obj.GetPosition() - Destination.GetPosition());
        battery_consumed += robot_distance * this.weight;
        int obj_distance = Math.abs(Obj.GetPosition() - Destination.GetPosition());
        battery_consumed += obj_distance * Obj.GetWeight();
        if(battery_consumed >= this.battery_remaining){
            System.out.println("Not enough battery to move!");
        }else {
            battery_consumed = 0;
            //Move the attendant to the object first
            battery_consumed += this.MoveTo(Obj);
            //Move the attendant to the destination
            battery_consumed += this.MoveTo(Destination);
            //Move the object to the destination
            battery_consumed += this.MoveTo(Destination, Obj);
            //Print calories consumed
            System.out.println(this.name + " consumed " + battery_consumed + " units of battery.");
        }
    }

    public double ConsumeBattery(double Amount) {
        if (Amount >= this.battery_remaining) {
            return -1;
        } else {
            this.battery_remaining -= Amount;
            return this.battery_remaining;
        }
    }

    public void ChargeBattery(double Amount) {
        this.battery_remaining += Amount;
        if (this.battery_remaining > this.battery_capacity) {
            this.battery_remaining = this.battery_capacity;
        }
        System.out.println(this.name + " charged " + Amount + " units of battery.");
    }

    public String GetName() {
        return this.name;
    }

    public int GetPosition() {
        return this.position;
    }

    public double GetWeight() {
        return this.weight;
    }

}
