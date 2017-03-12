/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package assg2task3;

/**
 *
 * @author kenchan
 */
public class Hotel {
    
    public static void MoveRoom(Object[] Obj_list, Room Destination){
        for(Object obj: Obj_list){
            if(obj instanceof Fixture){
                ((Fixture) obj).MoveTo(Destination);
            }
            else if(obj instanceof Attendant){
                ((Attendant) obj).MoveTo(Destination);
            }
        }
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Attendant peter = new Attendant("Peter", 58, 10000, 7);
        // stuff in room 2046
        Attendant mary = new Attendant("Mary", 45, 90000, 1);
        Attendant tony = new Attendant("Tony", 60, 1000000, 1);
        Washer washer1 = new Washer("Washer 1", 55, 1, 5000);
        Refrigerator refrigerator1 = new Refrigerator("Refrigerator 1", 50, 1, 5000, 3);
        Table table1 = new Table("Table 1", 20, 1, peter, true);
        Chair chair1 = new Chair("Chair 1", 8, 1, peter, false);
        Object[] old_room_stuff = {mary, tony, washer1, refrigerator1, table1, chair1};
        // rooms
        Room old_room = new Room("Room 2046", 1);
        Room new_room = new Room("Room 2047", 5);
        DiningHall dining_hall_1 = new DiningHall("Dinning hall 1", 12, 80);
        // move all the stuff to the new room
        Hotel.MoveRoom(old_room_stuff, new_room);
        // Peter eat something
        peter.MoveTo(dining_hall_1);
        dining_hall_1.ServerDinnerTo(peter);
    }

    
}
