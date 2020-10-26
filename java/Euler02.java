package euler;

public class Euler02 {

	public static void main(String[] args) {
		Integer a = 1, b = 2, cont = 0, c;
		
		while (a < 4000000) {
			if (a % 2 == 0) {
				cont += a;
			}
			c = a + b;
			a = b;
			b = c;
		}
		System.out.println(cont);

	}

}
