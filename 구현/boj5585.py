N = int(input())
S = 1000 - N
moneys = [500, 100, 50, 10, 5, 1]
count = 0

for money in moneys:
    if S >= money:
        count += S // money
        S = S % money

print(count)
