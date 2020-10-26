package euler;

public class Euler01 {

	public static void main(String[] args) {
		Integer cont = 0;
		for (Integer i = 0; i < 1000; i++) {
			if (i % 3 == 0 || i % 5 == 0) {
				cont++;
			}
		}
		System.out.println(cont);
	}

}
