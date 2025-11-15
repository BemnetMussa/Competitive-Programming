

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    // Your code here
    int n;
    std::cin >> n;
    std::vector<int> nums(n);
    for (int &x : nums) std::cin >> x;

    std::vector<int> dp(n, 1);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[j] < nums[i] && std::gcd(nums[j], nums[i]) > 1) {
                dp[i] = std::max(dp[i], dp[j] + 1);
            }
        }
    }

    std::cout << *std::max_element(dp.begin(), dp.end()) << std::endl;
    return 0;
}
