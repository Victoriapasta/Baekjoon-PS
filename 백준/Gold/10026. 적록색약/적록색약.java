import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {-1, 0, 1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String buffer = br.readLine();

        int count = 0;
        int countOddity = 0;
        int n = Integer.parseInt(buffer);

        char[][] graph = new char[n][n];
        boolean[][] visit = new boolean[n][n];
        boolean[][] visitOddity = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            graph[i] = br.readLine().toCharArray();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visit[i][j]) {
                    bfs(n, graph, i, j, visit);
                    count++;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 'G') {
                    graph[i][j] = 'R';
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visitOddity[i][j]) {
                    bfs(n, graph, i, j, visitOddity);
                    countOddity++;
                }
            }
        }
        System.out.println(count + " " + countOddity);
    }

    public static void bfs(int n, char[][] graph, int startX, int startY, boolean[][] visit) {
        Queue<List<Integer>> que = new LinkedList<>();

        que.add(List.of(startX, startY));
        while (!que.isEmpty()) {
            List<Integer> nowGraph = que.poll();

            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + nowGraph.get(0);
                int ny = dy[i] + nowGraph.get(1);

                if (0 <= nx && nx < n && 0 <= ny && ny < n && !visit[nx][ny]) {
                    if (graph[nx][ny] == graph[nowGraph.get(0)][nowGraph.get(1)]) {
                        que.add(List.of(nx, ny));
                        visit[nx][ny] = true;
                    }
                }
            }
        }
    }
}