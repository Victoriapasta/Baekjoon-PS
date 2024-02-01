import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = sc.nextInt();
        long dp[] = new long[n+1];

        dp[0] = 0;
        dp[1] = 1;

        if (n == 1) {
            System.out.println(1);
            return;
        }
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i-2] + dp[i-1];
        }

        System.out.println(dp[n]);
    }
}