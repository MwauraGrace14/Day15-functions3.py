#functions with outputs

def format_name(f_name, l_name):
  if f_name =="" or l_name=="":
    return "Invalid input!"
  formattedfname = f_name.title()
  formattedlname = l_name.title()
  return f"{formattedfname} {formattedlname}"

formatted_string = format_name("","")
print(formatted_string)


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False



def days_in_month(year, month):
  """Print the no of days in that month whether it's a leap year or not"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap:
    return 29
  else:
    return month_days[month -1]

year = int(input("Enter your birthday year ")) # Enter a year
month = int(input("Enter your birthday month ")) # Enter a month
days = days_in_month(year, month)
print(days)

