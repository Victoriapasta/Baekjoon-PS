import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String numbers = br.readLine();
        StringTokenizer st = new StringTokenizer(numbers);
        int pokeMonCount = Integer.parseInt(st.nextToken());
        int problemCount = Integer.parseInt(st.nextToken());

        Map<String, Integer> pokeDex1 = new HashMap<>(); //Key = String
        Map<Integer, String> pokeDex2 = new HashMap<>(); //Key = Integer
        for (int i = 1; i < pokeMonCount + 1; i++) {
            String pokeMons = br.readLine();
            pokeDex1.put(pokeMons, i);
            pokeDex2.put(i, pokeMons);
        }
        for (int i = 0; i < problemCount; i++) {
            String problem = br.readLine();
            try {
                System.out.println(pokeDex2.get(Integer.parseInt(problem)));
            } catch (NumberFormatException e) {
                System.out.println(pokeDex1.get(problem));
            }
        }
    }
}