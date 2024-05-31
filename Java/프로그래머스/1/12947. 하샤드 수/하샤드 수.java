import java.util.Arrays;

public class Solution {
    boolean solution(int x) {
        String stx = String.valueOf(x);
        int[] arr = new int[stx.length()];
        for (int i = 0; i < stx.length(); i++) {
            arr[i] = Integer.parseInt(String.valueOf(stx.charAt(i)));
            System.out.println(arr[i]);
        }
        int summary = Arrays.stream(arr).sum();
        if (x % summary == 0) {
            return true;
        }
        return false;
    }
}
