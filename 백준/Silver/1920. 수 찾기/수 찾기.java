import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Integer> numbers = Arrays.stream(br.readLine().split(" "))
                .map(c -> Integer.valueOf(c))
                .collect(Collectors.toList());

        HashMap<Integer, Integer> numberListHashMap = new HashMap<>();

        for (int i :
                numbers) {
            numberListHashMap.put(i, 1);
        }

        int m = Integer.parseInt(br.readLine());
        List<Integer> findNumbers = Arrays.stream(br.readLine().split(" "))
                .map(c -> Integer.valueOf(c))
                .collect(Collectors.toList());

        for (int i :
                findNumbers) {
            if (numberListHashMap.containsKey(i)) {
                System.out.println(1);
                continue;
            }
            System.out.println(0);
        }
    }
}