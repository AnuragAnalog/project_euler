import java.lang.Math;
public class Eular06 {

	public static void main(String[] args) {
		
		double sq = 0, sum = 0;
	    for (int i = 0; i < 101; i++)
	    {
	        double  m = Math.pow(i,2);
	        sq = sq + m;
	        sum = sum + i;
	    }
	    double k = Math.pow(sum, 2)-sq;
	    System.out.println(k); 

	}

}