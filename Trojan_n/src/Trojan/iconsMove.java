package Trojan;

public class iconsMove {


	public static void main(String[] args)
	{
		int a[]= {1,2,3,4,5,6,7}
		
		void rightRotateByOne(int A[], int n)
		{
		    int last = A[n - 1];
		    for (int i = n - 2; i >= 0; i--) {
		        A[i + 1] = A[i];
		    }
		 
		    A[0] = last;
		}  
	}	

}
