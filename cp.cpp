#include <bits/stdc++.h>
using namespace std;

// Macro for a for-loop from l to r-1
#define fore(i, l, r) for(int i = int(l); i < int(r); i++)
// Macro to get the size of a container
#define sz(a) int((a).size())

const int N = int(2e5) + 5; // Maximum number of nodes

int n;
vector<int> g[N]; // Adjacency list for the graph

// Reads the input for one test case and builds the graph
inline bool read() {
    if(!(cin >> n))
        return false;
    fore (i, 0, n)
        g[i].clear(); // Clear previous graph data
    
    fore (i, 0, n - 1) {
        int u, v;
        cin >> u >> v;
        u--, v--; // Convert to 0-based indexing
        g[u].push_back(v);
        g[v].push_back(u);
    }
    return true;
}

vector<int> used; // Marks visited nodes
vector<pair<int, int>> ans; // Stores the answer as pairs of edges

// DFS traversal to build the answer with alternating directions
void dfs(int v, bool in) {
    used[v] = 1;
    for (int to : g[v]) {
        if (used[to])
            continue;
        if (in)
            ans.emplace_back(to, v); // Edge direction depends on 'in'
        else
            ans.emplace_back(v, to);
        dfs(to, !in); // Alternate direction for next level
    }
}

// Solves one test case
inline void solve() {
    int r = 0;
    // Find a node with degree 2
    while (r < n && sz(g[r]) != 2)
        r++;
    if (r >= n) {
        cout << "NO\n"; // No such node, output NO
        return;
    }

    used.assign(n, 0); // Reset visited array
    ans.clear(); // Clear previous answers

    // Start with the two neighbors of node r
    ans.emplace_back(r, g[r][0]);
    ans.emplace_back(g[r][1], r);
    used[r] = 1;

    dfs(g[r][0], true);  // DFS from first neighbor
    dfs(g[r][1], false); // DFS from second neighbor

    cout << "YES\n";
    sort(ans.begin(), ans.end()); // Sort the answer for consistent output
    for (auto [u, v] : ans)
        cout << u + 1 << " " << v + 1 << '\n'; // Output in 1-based indexing
}

int main() {
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    int tt = clock();
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    cout << fixed << setprecision(15);
    
    int t; cin >> t;
    while (t--)  {
        if (!read()) break; // Read input, break if failed
        solve();
        
#ifdef _DEBUG
        cerr << "TIME = " << clock() - tt << endl;
        tt = clock();
#endif
    }
    return 0;
}