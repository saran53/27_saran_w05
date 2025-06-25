from datetime import datetime, date, timedelta
import time

today = date.today()

# print(f"วันที่ {today}")
# print(f"วัน {today.day}")
# print(f"เดือน {today.month}")
# print(f"ปี {today.year}")

now = datetime.now()
print(now)
# print(f"เวลาปัจจุบัน Hr : {now.hour}")
# print(f"เวลาปัจจุบัน m : {now.minute}")
# print(f"เวลาปัจจุบัน s : {now.second}")

# จัด Format ว ด ป 
formatted_date = now.strftime("%d/%m/%y")

formatted_date = now.strftime("%H-%M")
print(formatted_date,formatted_date)

# คำนวณวันที่ 
tomorow = today + timedelta(days=1)
yesyerday = today -timedelta(days=1)
next_week = today +timedelta(days=7)
next_mount = today + timedelta(days=30)


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    return age
 
day = int(input("Day : "))
mount = int(input("Mount : "))
year = int(input("Year : "))
birth_date = date(2000,2,29)

age = calculate_age(birth_date)
print(age)