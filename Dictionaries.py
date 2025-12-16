def average_score(scores):
    return sum(scores.values()) / len(scores)

def team_average(teams):
    total = []
    for i in teams:
        for n in i:
            total.append(n)
    return (sum(total)) / (len(total))