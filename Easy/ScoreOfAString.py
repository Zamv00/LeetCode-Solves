def scoreOfString(s):
    score = 0
    for i in range(len(s) - 1):
        adjacent_score = abs((ord(s[i]) - ord(s[i+1])))
        score += adjacent_score

    return score

