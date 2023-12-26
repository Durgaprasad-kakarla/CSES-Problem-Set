#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<long long> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }

    unordered_map<long long, long long> prefix_sums;
    prefix_sums[0] = 1;
    long long pref = 0, res = 0;

    for (int i = 0; i < n; ++i) {
        pref += nums[i];
        res += prefix_sums[pref - k];
        prefix_sums[pref]++;
    }

    cout << res << endl;

    return 0;
}
