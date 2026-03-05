"""
Captain Dread is keeping track of the crew's activities using a log. The logs are represented by a 2D integer
array logs where each logs[i] = [pirateID, time] indicates that the pirate with pirateID performed an action
at the minute time.

Multiple pirates can perform actions simultaneously, and a single pirate can perform multiple actions in the
same minute.

The pirate action minutes (PAM) for a given pirate is defined as the number of unique minutes in which the pirate
performed an action. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number
of pirates whose PAM equals j.

Return the array answer as described above.
给你一堆日志，每条日志是 [pirateID, time]，表示某个海盗在某分钟做了一件事。
PAM（海盗行动分钟数） = 某个海盗出现过的不同分钟数。比如海盗0出现在第5、2、5分钟，去重后是 {2, 5}，所以 PAM = 2。
返回值：一个长度为 k 的数组，answer[j] 表示 PAM 恰好等于 j 的海盗有几个（1-indexed，所以 j 从1开始）。
用 logs1 举例：

海盗0：出现在第5、2、5分钟 → 去重 {2,5} → PAM = 2
海盗1：出现在第2、3分钟 → 去重 {2,3} → PAM = 2
PAM=1 的海盗有0个，PAM=2 的海盗有2个，所以返回 [0, 2, 0, 0, 0]
"""
from collections import defaultdict


def counting_pirates_action_minutes(logs, k):
    """
    Understand:
        - input a list of 2-element lists
        - output a list of k elements
    Match:
        - hashmap
    Plan:
        - count unique number of pirates in each minute
        - hashmap {pirateID, set of unique minutes}
        - fill result list
    """
    cnt = defaultdict(set)
    for id, time in logs:
        cnt[id].add(time)

    res = [0] * k
    for _, unique_minutes in cnt.items():
        res[len(unique_minutes) - 1] += 1

    return res


if __name__ == "__main__":
    logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
    k1 = 5
    logs2 = [[1, 1], [2, 2], [2, 3]]
    k2 = 4

    print(counting_pirates_action_minutes(logs1, k1))  # [0, 2, 0, 0, 0]
    print(counting_pirates_action_minutes(logs2, k2))  # [1, 1, 0, 0]
