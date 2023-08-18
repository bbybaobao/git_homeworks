year = int(input("Enter year: "))

if year <= 1900 or year >= 1_000_000:
    print("Year not eligible.")
elif year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
