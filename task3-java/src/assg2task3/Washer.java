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
public class Washer extends SmartFixture {
    public Washer(String Name, double Weight, int Position, double Battery_capacity){
        super(Name, Weight, Position, Battery_capacity);
    }
    public void Wash(){
        System.out.println(this.name + " finished a wash procedure.");
    }
}
