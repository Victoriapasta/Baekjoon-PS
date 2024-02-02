import java.io.IOException;
import java.util.Scanner;

public class Main {

    static int n;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        gugudan();
    }

    private static void gugudan() {
        for (int i = 1; i <= 9; i++) {
            System.out.println(n + " * " + i + " = " + i*n);
        }
    }
}