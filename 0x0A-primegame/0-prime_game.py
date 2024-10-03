#!/usr/bin/python3
""" Python: Prime game solution """


def isWinner(x, nums):
    """ Prime Game """
    if not nums or x < 1:
        return None

    max_number = max(nums)
    checker = [True] * (max_number + 1)
    checker[0] = checker[1] = False
    prm_counter = [0] * (max_number + 1)

    prm_total = 0
    for i in range(2, max_number + 1):
        if checker[i]:
            prm_total += 1
            for cnt in range(i * 2, max_number + 1, i):
                checker[cnt] = False
        prm_counter[i] = prm_total

    wmaria = 0
    wben = 0

    for n in nums:
        if prm_counter[n] % 2 == 1:
            wmaria += 1
        else:
            wben += 1

    if wmaria > wben:
        return "Maria"
    elif wmaria < wben:
        return "Ben"
    else:
        return None
