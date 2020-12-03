def rob(nums):
    mx_nonadj = mx_adj = 0
    for i in nums:
        mx_adj, mx_nonadj = max(mx_adj, mx_nonadj+i), max(mx_adj, mx_nonadj)
    return  max(mx_adj, mx_nonadj)