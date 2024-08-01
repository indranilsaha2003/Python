n=int(input("Enter a year you want to check Leap Year or not\n"))
isLeapYear="Not Leap Year"

if(n%400==0 or( n%100!=0 and n%4==0)):
    isLeapYear="Leap Year"

print(n,"is",isLeapYear)