import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String buffer = br.readLine();

        int n = Integer.parseInt(buffer);
        List<Integer> arr = Arrays.stream(br.readLine().split(" "))
                .map(c -> Integer.valueOf(c))
                .collect(Collectors.toList());

        arr.sort(Comparator.naturalOrder());

        int[] sufSum = new int[n];
        sufSum[0] = arr.get(0);

        for (int i = 1; i < n; i++) {
            sufSum[i] = sufSum[i-1] + arr.get(i);
        }

        System.out.println(Arrays.stream(sufSum).sum());
    }
}