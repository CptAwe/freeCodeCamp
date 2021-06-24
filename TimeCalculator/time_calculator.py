# [...] Do not import any Python libraries. [...]
# CHALLENGE ACCEPTED!


def add_time(start: str, duration: str, startingDay: str = None):

    DAYS_OF_THE_WEEK = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ]

    def time12to24(time12: str) -> str:
        """
        Convert 12 hour format to 24 hour format
        """
        time12, part_of_day = time12.split(" ")
        hours, minutes = time12.split(":")
        hours = int(hours)
        minutes = int(minutes)

        if part_of_day == "PM":
            hours += 12
        
        return "{}:{:0>2}".format(hours, minutes)

    def time24to12(time24: str) -> str:
        """
        Convert 24 hour format to 12 hour format
        """
        hours, minutes = time24.split(":")
        hours = int(hours)
        minutes = int(minutes)

        part_of_day = "AM"
        if hours>=12:
            part_of_day = "PM"
            hours = hours-12 if hours-12>0 else hours
        elif hours == 0:
            hours = 12

        return "{}:{:0>2} {}".format(hours, minutes, part_of_day)
    
    start = time12to24(start)
    old_hours, old_minutes = start.split(":")
    old_hours = int(old_hours)
    old_minutes = int(old_minutes)

    hours2add, minutes2add = duration.split(":")
    hours2add = int(hours2add)
    minutes2add = int(minutes2add)

    days2add = hours2add//24# full days to add
    hours2add = hours2add%24# full hours to add

    # Make the addition
    new_minutes = old_minutes + minutes2add
    if new_minutes >= 60:
        new_minutes -= 60
        hours2add += 1

    new_hour = old_hours + hours2add
    if new_hour >= 24:
        new_hour -= 24
        days2add += 1
    
    # Format the result
    new_time = "{}:{}".format(new_hour, new_minutes)
    new_time = time24to12(new_time)

    full_new_time = new_time

    if startingDay:
        startingDay = startingDay.lower()

        startingDay_num = DAYS_OF_THE_WEEK.index(startingDay)
        endingDay_num = startingDay_num + days2add
        
        weeks2add = endingDay_num//7# full weeks to add
        endingDay_num = endingDay_num%7# days to add

        new_day = DAYS_OF_THE_WEEK[endingDay_num]
        full_new_time += ", {}".format(new_day.capitalize())

    
    if days2add == 1:
        full_new_time += " (next day)"
    elif days2add > 1:
        full_new_time += " ({} days later)".format(days2add)
    
    return full_new_time

