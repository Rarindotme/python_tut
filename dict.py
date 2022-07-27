# Dictionary 
from calendar import month


month_conversions = {
  "Jan": "January",
  "feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  7: "July",
  "Aug": "August",
  "Sept": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December"
}
print(month_conversions["Oct"])
print(month_conversions.get("Dec"))
print(month_conversions.get("luv", "Not a valid Key"))

print(month_conversions[7])

i = 1
while i <= 10:
  print(i)
  i += 1
