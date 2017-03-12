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
public class Chair extends DumbFixture {
    protected Boolean seat_back;
    public Chair(String Name, double Weight, int Position, Attendant Person_in_charge, Boolean Seat_back){
        super(Name, Weight, Position, Person_in_charge);
        this.seat_back = Seat_back;
    }
}
