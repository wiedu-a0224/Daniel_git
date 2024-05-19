package Trojan;

import java.util.Arrays;

public class randomTest {

public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] A = new int[12];
        int k=0;
		while (true) {
			if (k>12) {
				break;
			}
			for (int i=10;i>=0;i--) {
				A[i+1]=A[i];
			}
		    A[0] = (int)Math.round(Math.random()*3);
		    k++;
        System.out.println(k+','+Arrays.toString(A));
		}
				
 System.out.println("=====================");
		}    
            
	    }
	


