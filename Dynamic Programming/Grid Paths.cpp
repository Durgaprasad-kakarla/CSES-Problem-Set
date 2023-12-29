#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1000000007;

int func(int i, int j, vector<vector<char>>& grid, vector<vector<int>>& dp) {
    if (i < 0 || j < 0) {
        return 0;
    }
    if (i == 0 && j == 0) {
        if (grid[i][j] != '*') {
            return 1;
        }
        return 0;
    }
    if (dp[i][j] != -1) {
        return dp[i][j];
    }
    int l = 0, r = 0;
    if (grid[i][j] != '*') {
        l = func(i - 1, j, grid, dp);
        r = func(i, j - 1, grid, dp);
    }
    dp[i][j] = (l + r) % MOD;
    return dp[i][j];
}

int main() {
    int n;
    cin >> n;

    vector<vector<char>> grid(n, vector<char>(n, 0));
    vector<vector<int>> dp(n, vector<int>(n, -1));

    for (int i = 0; i < n; ++i) {
        string st;
        cin >> st;
        for (int j = 0; j < n; ++j) {
            grid[i][j] = st[j];
        }
    }

    cout << func(n - 1, n - 1, grid, dp) % MOD << endl;

    return 0;
}
/* Time Complexity--O(n*n)
   Space Complexity--O(n*n)*/
/* Same code doesn't work in python*/
/*def func(i,j,grid,dp):
    if i<0 or j<0:
        return 0
    if i==0 and j==0:
        if grid[i][j]!='*':
            return 1
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    l,r=0,0
    if grid[i][j]!='*':
        l=func(i-1,j,grid,dp)
        r=func(i,j-1,grid,dp)
    dp[i][j]=(l+r)%(10**9+7)
    return l+r
n=int(input())
grid=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    st=input()
    for j in range(n):
        grid[i][j]=st[j]
dp=[[-1 for i in range(n)] for j in range(n)]
print(func(n-1,n-1,grid,dp)%(10**9+7))*/
