import java.util.ArrayList;

/**
 * Created by tulio on 12/12/15.
 */
public class PrimeFactors {

    public static void main(String[] args) {
        System.out.println(generate(1));
        System.out.println(generate(5));
        System.out.println(generate(30));
        System.out.println(generate(50));
        System.out.println(generate(80));

    }

    private static ArrayList generate(int n) {
        ArrayList<Integer> factors = new ArrayList<>();

        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }

        return factors;
    }
}
