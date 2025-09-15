import datetime
x=datetime.datetime.now()
y=datetime.datetime(2025,9,23)

# %A = Weekday
# %a = short Weekday
# %B = Month name
# %b = short Month name
# %y = Year short name
# %Y = Year full name
# strftime = string + format + time
print(x,"\n")
print(x.year,"\n")
print(x.strftime("%A"),"\n")
print(x.second,"\n")
print(x.strftime("%b"),"\n")
print(y.strftime("%Y"))
