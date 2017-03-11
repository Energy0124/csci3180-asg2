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
public class Table extends DumbFixture {
    protected Boolean extendable;
    public Table(String Name, double Weight, int Position, Attendant Person_in_charge, Boolean Extendable){
        super(Name, Weight, Position, Person_in_charge);
        this.extendable = Extendable;
    }
}
