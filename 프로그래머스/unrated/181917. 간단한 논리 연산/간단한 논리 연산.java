class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = true;
        boolean a = x1 || x2;
        boolean b = x3 || x4;
        answer = a && b;
        return answer;
    }
}