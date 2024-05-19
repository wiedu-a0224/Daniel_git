package Trojan;

import java.util.Arrays;

public class test {
	 public static void rightRotateByOne(int[] A)
	    {
		    A[0] = (int)Math.round(Math.random()*3);
	        for (int i = A.length - 2; i >= 0; i--) {
	            A[i + 1] = A[i];
	        }
	        
	    }
	 
	    // 將數組右旋 `k` 個位置的函數
	    public static void rightRotate(int[] A, int k)
	    {
	        // 基本情況：無效輸入
	        if (k < 0 || k >= A.length) {
	            return;
	        }
	 
	        for (int i = 0; i < k; i++) {
	            rightRotateByOne(A);
	        }
	    }
	 
	    public static void main(String[] args)
	    {
	        int[] A = new int[12];
	        int k = 100000;
	 
	        rightRotate(A, k);
	 
	        System.out.println(Arrays.toString(A));
	    }
	
       
}
