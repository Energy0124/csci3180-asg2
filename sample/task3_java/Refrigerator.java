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
