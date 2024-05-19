package Trojan;

import java.util.Arrays;

public class teatIf {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] n = new int[18];
        int[] d = new int[18];
		int k=0;
		while (true) {
			if (k>12) {
				break;
			}
			
			for (int i=1;i>=17;i++) {
						
				 n[i]=d[i];
				 d[i]=n[i+1];
				 n[i+1]=n[i];
			}
		    n[0] = (int)Math.round(Math.random()*3);
		    k++;
        System.out.println(k+','+Arrays.toString(n));
		}
				
 System.out.println("=====================");
		}    
	}


