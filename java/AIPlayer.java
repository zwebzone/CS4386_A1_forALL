package com;
import java.util.ArrayList;
public class AIPlayer {
	String name="AI2";
	String symbole;
	boolean isAI=true;
    int score=0;

	public boolean get_isAI(){
		return isAI;
	}
	public void add_symbole(String symbole1){
		symbole=symbole1;
	}
	public void add_isAI(boolean isAI1){
		isAI=isAI1;
	}
	public String get_symbole(){
		return symbole;
	}
	
	public void add_score(int score1){
		score=score+score1;
	
	}
	public int get_score(){
		return score;
	}

    public int[] get_move(ArrayList state, String symbole){

    	ArrayList moveList= new ArrayList();
	    for (int row=0;row<6;row++){
            for (int column=0;column<6;column++){	
            	ArrayList this_row=(ArrayList)state.get(row);
            	if (this_row.get(column)==null){
            		int[] move = new int[2];
					move[0]=row;
					move[1]=column;
					moveList.add(move);
                }
            }
        }
        int rand = (int)(Math.random() * moveList.size());
        return (int[]) moveList.get(rand);
    }
}