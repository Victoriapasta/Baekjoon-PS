#include <iostream>
#include <vector>

using namespace std;

int n, m, found = 0, cnt = 0;
vector<int> graph;
vector<int> great;

int find(int node) {
    if(graph[node] < 0) return node;
    else return find(graph[node]);
}

void merge(int a, int b, int f) {
    a = find(a);
    b = find(b);
    if (a == b) {
        cnt = f;
        great.push_back(cnt);
        return;
    }
    if (graph[a] <= graph[b]) {
        graph[a] += graph[b];
        graph[b] = a;
    }
    else {
        graph[b] += graph[a];
        graph[a] = b;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        graph.push_back(-1);
    }
    for(int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        merge(a, b, i+1);
    }
    if(great.size())
    cout<<great[0];
    else cout<<0;

    /*for(int i = 1; i <= n; i++) {
        if(graph[i] < 0) {
            cnt++;
            great.push_back(graph[i] * -1);
        }
    }
    int maxi = great[0];
    for(int i = 1; i < great.size(); i++) maxi = max(maxi, great[i]);
    if(found)cout<<"Found\n";
    else cout<<"Not found\n";
    cout<<cnt<<"\n";
    cout<<maxi; */

    return 0;
}