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
        List<Integer> array = Arrays.stream(br.readLine().split(" "))
                .map(c -> Integer.valueOf(c))
                .collect(Collectors.toList());

        if (array.get(0) == array.get(1) && array.get(1) == array.get(2)) {
            System.out.println(10000 + array.get(0) * 1000);
        } else if (array.get(0) == array.get(1) || array.get(0) == array.get(2) || array.get(1) == array.get(2)) {
            array.sort(Comparator.naturalOrder());
            System.out.println(1000 + (array.get(1) * 100));
        } else {
            System.out.println(100 * (array.stream().mapToInt(c -> c).max().orElse(0)));
        }
    }
}