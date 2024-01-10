import calendar

# Define a dictionary of motivational quotes
motivational_quotes = {
    1: "The only way to do great work is to love what you do.",
    2: "Believe you can and you're halfway there.",
    3: "Don't watch the clock; do what it does. Keep going.",
    4: "Strive not to be a success, but rather to be of value.",
    5: "You don't have to be great to start, but you have to start to be great.",
    6: "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    7: "The only limit to our realization of tomorrow will be our doubts of today.",
    8: "The only place where success comes before work is in the dictionary.",
    9: "You miss 100% of the shots you don't take.",
    10: "The harder you work, the harder it is to surrender.",
    11: "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.",
    12: "The only person you are destined to become is the person you decide to be.",
    13: "The best way to predict the future is to create it.",
    14: "Success is not how high you have climbed, but how you make a positive difference to the world.",
    15: "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    16: "The only person you are destined to become is the person you decide to be.",
    17: "The future belongs to those who believe in the beauty of their dreams.",
    18: "The expert in anything was once a beginner.",
    19: "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    20: "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    21: "The way to get started is to quit talking and begin doing.",
    22: "Success is stumbling from failure to failure with no loss of enthusiasm.",
    23: "The only person you are destined to become is the person you decide to be.",
    24: "The best way to find yourself is to lose yourself in the service of others.",
    25: "The only way to do great work is to love what you do.",
    26: "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    27: "The best way to predict the future is to create it.",
    28: "The only limit to our realization of tomorrow will be our doubts of today.",
    29: "The only way to do great work is to love what you do.",
    30: "Success is not how high you have climbed, but how you make a positive difference to the world.",
    31: "The only person you are destined to become is the person you decide to be."
}

# Print the calendar for the year 2024
print(calendar.TextCalendar(calendar.SUNDAY).formatyear(2024))

# Print a motivational quote for each day of the year
for month in range(1, 13):
    for day in range(1, calendar.monthrange(2024, month)[1] + 1):
        print(f"{day} {calendar.month_abbr[month]}: {motivational_quotes[day]}")