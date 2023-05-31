#include <iostream>
using namespace std;

int t;
long long dp[101] = {0, 1, 1, 1, 2};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> t;
    for(int i = 5; i < 101; i++) {
        dp[i] = dp[i-1] + dp[i-5];
    }
    for(int i = 0; i < t; i++) {
        int n;
        cin>>n;
        cout<<dp[n]<<endl;
    }
    return 0;
}