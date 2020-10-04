package euler;

public class Euler02 {

	public static void main(String[] args) {
		Integer a = 1;
		Integer b = 2;
		Integer cont = 0;
		Integer c;
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
