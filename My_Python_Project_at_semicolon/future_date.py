def future_date(day, future):
    time = day + future
    while time > 7:
        time -= 7
        match time:
            case 1:
                return "Monday"
            case 2:
                return "Tuesday"
            case 3:
                return "Wednesday"
            case 4:
                return "Thursday"
            case 5:
                return "Friday"
            case 6:
                return "Saturday"
            case _:
                return "sunday"


user_day = int(input("Enter today's day "))
user_future_day = int(input("Enter the number of days elapsed since today future "))
print(f"Today is {future_date(user_day, 0)} and the future day is {future_date(user_future_day, user_future_day)}")
