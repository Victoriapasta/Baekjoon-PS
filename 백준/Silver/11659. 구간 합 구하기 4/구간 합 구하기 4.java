import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Integer> numbers = Arrays.stream(br.readLine().split(" "))
                .map(c -> Integer.valueOf(c))
                .collect(Collectors.toList());

        List<Integer> prefixSum = new ArrayList<>();

        prefixSum.add(numbers.get(0));

        for (int i = 1; i < n; i++) {
            prefixSum.add(numbers.get(i) + prefixSum.get(i - 1));
//            System.out.println("prefixSum = " + prefixSum);
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int startNum = Integer.parseInt(st.nextToken());
            int endNum = Integer.parseInt(st.nextToken());

            System.out.println(prefixSum.get(endNum - 1) - prefixSum.get(startNum - 1) + numbers.get(startNum - 1));
        }
    }
}