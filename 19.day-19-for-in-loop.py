loan = 1000
for years in range(10):
    loan += loan * 0.05
    print("Year", years + 1, ": ", round(loan, 2), "$")
