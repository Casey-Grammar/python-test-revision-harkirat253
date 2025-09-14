def soccer_match_outcome(italy_score, brazil_score):
    if italy_score > brazil_score:
        return "Italy won the match."
    elif brazil_score > italy_score:
        return "Brazil won the match."
    else:
        return "The match was a draw."

print("Enter the scores for the latest soccer match between Brazil and Italy:")
italy_score = int(input("Italy score: "))
brazil_score = int(input("Brazil score: "))

outcome = soccer_match_outcome(italy_score, brazil_score)
print(outcome)
