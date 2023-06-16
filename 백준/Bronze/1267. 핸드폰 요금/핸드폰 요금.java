import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n, Y = 0, M = 0;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        int[] a = new int[n];
        for(int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        for(var temp : a) {
            Y += (temp/30 + 1)*10;
            M += (temp/60 + 1)*15;
        }
        if(Y == M) {
            System.out.println("Y M " + Y);
        }
        else if (Y < M) {
            System.out.println("Y " + Y);
        }
        else if (Y > M) {
            System.out.println("M " + M);
        }
    }
}
