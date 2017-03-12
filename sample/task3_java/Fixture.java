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
public abstract class Fixture {
    protected String name;
    protected double weight;
    public int position;
    
    public Fixture(String Name, double Weight, int Position){
        this.name = Name;
        this.weight = Weight;
        this.position = Position;
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
    public abstract void MoveTo(Room Destination);
}

