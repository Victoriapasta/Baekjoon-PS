#include <iostream>
using namespace std;

int t, sum;
int d[101], p[101];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> t;
    for(int i = 0; i < t; i++) {
        int a, b;
        cin >> a >> b;
        d[i] = a;
        p[i] = b;
    }
    for(int i = 0; i < t; i++) {
        sum += p[i] % d[i];
    }

    cout<<sum;
    

    return 0;
}