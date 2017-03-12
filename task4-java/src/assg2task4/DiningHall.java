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
public class DiningHall extends Room {
    protected double dinner_price;
    public DiningHall(String Name, int Position, double Dinner_price){
        super(Name, Position);
        this.dinner_price = Dinner_price;
    }
    public void ServerDinnerTo(Attendant Obj){
        if (Obj.GetPosition()==this.position){
            if (Obj.Pay(this.dinner_price)>=0){
                System.out.println(Obj.GetName() + " finished the dinner.");
            }
            else{
                System.out.println(Obj.GetName() + " didn't have enough money.");
            }
        }
        else{
            System.out.println(Obj.GetName() + " was too far away to be served.");
        }
    }
}
