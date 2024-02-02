import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    static int[] dx = {0, -1, 0, 1};
    static int[] dy = {-1, 0, 1, 0};
    static int[][] graph;
    static int[][] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for (int testCase = 0; testCase < t; testCase++) {
            int m = sc.nextInt();
            int n = sc.nextInt();
            int k = sc.nextInt();

            graph = new int[m][n]; // 0으로 자동 초기화

            for (int i = 0; i < k; i++) {
                int graphX = sc.nextInt();
                int graphY = sc.nextInt();

                graph[graphX][graphY] = 1;
            }

            int answer = 0;
            visited = new int[m][n];

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (graph[i][j] == 1 && visited[i][j] == 0) {
                        bfs(i, j, m, n);
                        answer++;
                    }
                }
            }
            System.out.println(answer);
        }
    }

    private static void bfs(int startx, int starty, int m, int n) {

        Queue<List<Integer>> que = new LinkedList<>();
        que.add(List.of(startx, starty));

        while (!que.isEmpty()) {
            List<Integer> nowGraph = que.poll();
            for (int i = 0; i < 4; i++) {
                int nowX = nowGraph.get(0) + dx[i];
                int nowY = nowGraph.get(1) + dy[i];

                if (m > nowX && nowX >= 0 && n > nowY && nowY >= 0) {
                    if (visited[nowX][nowY] == 0 && graph[nowX][nowY] == 1) {
                        visited[nowX][nowY] = 1;
                        que.add(List.of(nowX, nowY));
                    }
                }
            }
        }
    }
}