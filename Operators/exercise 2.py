def checkYear(year):

    import calendar
    return(calendar.isleap(year))

year=1995
if (checkYear(year)):
    print("True")
else:
    print("False")


