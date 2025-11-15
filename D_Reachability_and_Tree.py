using namespace std;

#define fore(i, l, r) for(int i = int(l); i < int(r); i++)
#define sz(a) int((a).size())

const int N = int(2e5) + 5;

int n;
vector<int> g[N];

inline bool read() {
	if(!(cin >> n))
		return false;
	fore (i, 0, n)
		g[i].clear();
	
	fore (i, 0, n - 1) {
		int u, v;
		cin >> u >> v;
		u--, v--;
		g[u].push_back(v);
		g[v].push_back(u);
	}
	return true;
}

vector<int> used;
vector<pair<int, int>> ans;

void dfs(int v, bool in) {
	used[v] = 1;
	for (int to : g[v]) {
		if (used[to])
			continue;
		if (in)
			ans.emplace_back(to, v);
		else
			ans.emplace_back(v, to);
		dfs(to, !in);
	}
}

inline void solve() {
	int r = 0;
	while (r < n && sz(g[r]) != 2)
		r++;
	if (r >= n) {
		cout << "NO\n";
		return;
	}

	used.assign(n, 0);
	ans.clear();

	ans.emplace_back(r, g[r][0]);
	ans.emplace_back(g[r][1], r);
	used[r] = 1;

	dfs(g[r][0], true);
	dfs(g[r][1], false);

	cout << "YES\n";
	sort(ans.begin(), ans.end());
	for (auto [u, v] : ans)
		cout << u + 1 << " " << v + 1 << '\n';
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
		read();
		solve();
		
#ifdef _DEBUG
		cerr << "TIME = " << clock() - tt << endl;
		tt = clock();
#endif
	}
	return 0;