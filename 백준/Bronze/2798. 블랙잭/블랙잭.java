import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int answer = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Integer> numbers = Arrays.stream(br.readLine().split(" "))
                .map(c -> Integer.valueOf(c))
                .collect(Collectors.toList());

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1 ; k < n; k++) {
                    int temp = numbers.get(i) + numbers.get(j) + numbers.get(k);
                    if (temp <= m && temp > answer) {
                        answer = temp;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}