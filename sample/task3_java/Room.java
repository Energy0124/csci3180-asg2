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
public class Room {
    protected String name;
    protected int position;
    public Room(String Name, int Position){
        this.name = Name;
        this.position = Position;
    }
    public String GetName(){
        return this.name;
    }
    public int GetPosition(){
        return this.position;
    }
}
