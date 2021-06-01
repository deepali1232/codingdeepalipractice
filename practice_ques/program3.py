#Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting to be 18. )
def eligible_vote(num):
    if num>=18:
        print("eligible for vote")
    else:
        print("sry can't eligible for vote.")
eligible_vote(14)
eligible_vote(18)
eligible_vote(25)