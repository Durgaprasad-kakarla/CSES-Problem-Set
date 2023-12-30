#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, m;
    cin >> n >> m;

    multiset<long long, greater<int>> tickets;

    while (n--) {
        long long ticket;
        cin >> ticket;
        tickets.insert(ticket);
    }

    while (m--) {
        long long curr;
        cin >> curr;
        auto it = tickets.lower_bound(curr);

        if (it == tickets.end()) {
            cout << -1 << endl;
        } else {
            cout << *it << endl;
            tickets.erase(it);
        }
    }

    return 0;
}
