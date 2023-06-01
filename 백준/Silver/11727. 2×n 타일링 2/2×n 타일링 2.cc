#include <iostream>
using namespace std;

int t;
int dp[1001] = {0, 1, 3};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> t;
    for(int i = 3; i < 1001; i++) {
        dp[i] = (dp[i-1] + dp[i-2] * 2)%10007;
    }
    cout<<dp[t];
}