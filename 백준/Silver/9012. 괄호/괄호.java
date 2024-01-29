import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCases = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCases; i++) {
            Stack<Character> psStack = new Stack<>();
            String ps = br.readLine();

            boolean answer = isTmp(i, psStack, ps);

            if (answer == true) {
                System.out.println("YES");
                continue;
            }
            System.out.println("NO");
        }
    }

    private static boolean isTmp(int i, Stack<Character> psStack, String ps) {
        for (int j = 0; j < ps.length(); j++) {
            if (ps.charAt(j) == '(') {
                psStack.push(ps.charAt(j));
            }
            if (psStack.isEmpty() && ps.charAt(j) == ')') {
                return false;
            }
            if (!psStack.isEmpty() && ps.charAt(j) == ')') {
                psStack.pop();
            }
        }

        if (psStack.isEmpty()) {
            return true;
        }
        return false;
    }
}