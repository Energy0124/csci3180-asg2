
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
public class Refrigerator extends SmartFixture {
    protected double temperature;
    public Refrigerator(String Name, double Weight, int Position, double Battery_capacity, double Initial_temperature){
        super(Name, Weight, Position, Battery_capacity);
        this.temperature = Initial_temperature;
    }
    public void SetTemperature(double New_temperature){
        this.temperature = New_temperature;
        System.out.println(this.name + " was set to " + New_temperature + " degrees Celsius.");
    }
}
