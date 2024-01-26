'''
Write some code that takes a human age and translates it into dog age.
Calculate age in dog years. Dogs live wild lives. As a result, 1 human year equals 7 dog years.
'''

human_age = float(input("Human Age = "))

dog_agein_years = human_age * 7
dog_agein_months = ((human_age * 7 % 1) * 12)
dog_agein_days = ((human_age * 7 % 1) * 360 % 30)


print(f" {(human_age)} in human years is {float(int(dog_agein_years))} in dog years, {float(int(dog_agein_months))} in dog months, and {float(int(dog_agein_days))} in dog days.")

cat_agein_years = (human_age / 9)
cat_agein_months = ((human_age / 9 % 1) * 12)
cat_agein_days = ((human_age / 9 % 1) * 360 % 30)

print(f" {human_age} in human years is {float(int(cat_agein_years))} in cat years, {float(int(cat_agein_months))} in cat months, {float(int(cat_agein_days))} in cat days.")

horse_agein_years = 3 * (((((human_age) ** 2) - 47) / 7) + 12 )
horse_agein_months = (((3 * (((((human_age) ** 2) - 47) / 7) + 12 )) % 1) * 12)
horse_agein_days = ((3 * (((((human_age) ** 2) - 47) / 7) + 12 ) % 1) * 360 % 30)

print(f" {human_age} in human years is {float(int(horse_agein_years))} in horse years, {float(int(horse_agein_months))} in horse months, and {float(int(horse_agein_days))} in horse days.")


