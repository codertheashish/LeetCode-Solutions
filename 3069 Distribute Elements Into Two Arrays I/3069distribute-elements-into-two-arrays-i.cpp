class Solution {
public:
    vector<int> resultArray(vector<int>& nums) {
        vector<int> arr1;
        vector<int> arr2;

        arr1.push_back(nums[0]);
        arr2.push_back(nums[1]);

        int k = 2;

        while (k < nums.size()) {
            if (arr1.back() > arr2.back()) {
                arr1.push_back(nums[k]);
            } else {
                arr2.push_back(nums[k]);
            }
            k++;
        }

        vector<int> result;

        for (int x : arr1) {
            result.push_back(x);
        }

        for (int x : arr2) {
            result.push_back(x);
        }

        return result;
    }
};