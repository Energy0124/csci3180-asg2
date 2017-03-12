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
public class DumbFixture extends Fixture {
    protected Attendant person_in_charge;
    public DumbFixture(String Name, double Weight, int Position, Attendant Person_in_charge){
        super(Name, Weight, Position);
        this.person_in_charge = Person_in_charge;
    }
    public void MoveTo(Room Destination){
        this.person_in_charge.CarryTo(this, Destination);
    }
    public void AssignTo(Attendant Person_in_charge){
        this.person_in_charge = Person_in_charge;
    }
}
