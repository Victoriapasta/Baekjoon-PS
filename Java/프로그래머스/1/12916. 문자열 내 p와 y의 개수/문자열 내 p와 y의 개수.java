public class Solution {
    boolean solution(String s) {
        int cntP = 0;
        int cntY = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'p' || s.charAt(i) == 'P') {
                cntP++;
                continue;
            }
            if (s.charAt(i) == 'y' || s.charAt(i) == 'Y') {
                cntY++;
                continue;
            }
        }
        if (cntP == cntY) return true;

        return false;
    }
}