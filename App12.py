#short circuit evaluation

high_income = False
good_credit=True
student=False

#evaluation stops as soon as one of the condition is false
# for high income and good credit
# f it (or logical opp) the the condition is evaluated


if high_income or good_credit or not student:
    print("Eligible for loan")