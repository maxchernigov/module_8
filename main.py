from datetime import date,datetime
from collections import defaultdict



def get_birthdays_per_week(users) -> dict:
    today = date.today()
    dict_birthday = defaultdict(list)
 
    if not users:
        return dict_birthday
    
    for i in users:
        value_day = i.get("birthday").replace(year = today.year)
        value_name = i.get("name")
        dif_date = value_day - today
    
        if dif_date.days < 0:
                value_day = i.get('birthday').replace(year=today.year + 1)
                dif_date = value_day - today
        
        if 0 < dif_date.days <= 6:
            if 4 < value_day.weekday() <= 6:
                dict_birthday["Monday"].append(value_name)
            else:
                day = datetime.strftime(value_day, '%A')
                dict_birthday[day].append(value_name)
    return dict_birthday
    
if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

