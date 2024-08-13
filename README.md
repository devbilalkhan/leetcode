# LeetCode Challenges

This folder contains solutions to various LeetCode problems. Each solution is implemented in Python and includes detailed comments to explain the logic.

## Solutions

### 1. Two Sum

- **File:** `1_two_sum.py`
- **Description:** This solution finds two numbers in an array that add up to a specific target. It uses a hash map to store the indices of the numbers and checks if the complement of the current number exists in the hash map.
- **LeetCode Problem:** [Two Sum](https://leetcode.com/problems/two-sum/)



### 2. Best Time to Buy and Sell Stock

- **File:** `2_buy_sell_stock.py`
- **Description:** This solution calculates the maximum profit that can be achieved from a single buy and sell transaction of a stock. It uses a two-pointer technique to find the optimal buy and sell days.
- **LeetCode Problem:** [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### 3. Contains Duplicate

- **File:** `3_contains_duplicate.py`
- **Description:** This solution checks if there are any duplicates in the list. It uses a set to store unique items and checks if an item is already in the set to determine if a duplicate exists.
- **LeetCode Problem:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

### 4. Product of Array Except Self

- **File:** `4_product_except_self.py`
- **Description:** This solution calculates the product of all elements in the array except the current element. It uses prefix and suffix products to achieve this in O(n) time complexity without using division.
- **LeetCode Problem:** [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

### 5. Maximum Subarray

- **File:** `5_maximum_subarray.py`
- **Description:** This solution finds the subarray with the largest sum within an integer array `nums` and returns its sum. It uses Kadane's Algorithm to achieve this in O(n) time complexity.
- **LeetCode Problem:** [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

## How to Run

To run any of the solutions, navigate to the folder and execute the Python file. For example:

```bash
python 3_contains_duplicate.py