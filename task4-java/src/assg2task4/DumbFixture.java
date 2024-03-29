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
 * @author kenchan
 */
public class DumbFixture extends Fixture {
    protected Attendant person_in_charge = null;
    protected Robot robot_in_charge = null;

    public DumbFixture(String Name, double Weight, int Position, Attendant Person_in_charge) {
        super(Name, Weight, Position);
        this.person_in_charge = Person_in_charge;
    }

    public DumbFixture(String Name, double Weight, int Position, Robot Robot_in_charge) {
        super(Name, Weight, Position);
        this.robot_in_charge = Robot_in_charge;
    }

    public void MoveTo(Room Destination) {
        if (person_in_charge != null) {
            this.person_in_charge.CarryTo(this, Destination);
        } else {
            this.robot_in_charge.CarryTo(this, Destination);
        }
    }

    public void AssignTo(Attendant Person_in_charge) {
        this.person_in_charge = Person_in_charge;
    }

    public void AssignTo(Robot Robot_in_charge) {
        this.robot_in_charge = Robot_in_charge;
    }
}
