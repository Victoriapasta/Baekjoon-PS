import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String buffer = br.readLine();

        StringTokenizer st = new StringTokenizer(buffer);
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int count = 0;
        int coin = n-1;

        while (k != 0) {
            if (arr[coin] <= k) {
                count++;
                k -= arr[coin];
                continue;
            }
            coin--;
        }
        System.out.println(count);
    }
}