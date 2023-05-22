#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int n, m;
vector <vector<int>> graph(100001);
int dist[100001];

void topologySort() {
    queue<int> que;
    for(int i = 1; i <= n; i++) {
        if(!dist[i])que.push(i);
    }
    for(int i = 0; i < n; i++) {
        if(que.empty()){
            return;
        }
        int node = que.front();
        que.pop();
        for(int i = 0; i< graph[node].size(); i++) {
            int nextNode = graph[node][i];
            dist[nextNode]--;
            if(!dist[nextNode])que.push(nextNode);
        }
        cout<<node<<" ";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    for(int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        dist[b]++;
    }
    topologySort();

    return 0;
}