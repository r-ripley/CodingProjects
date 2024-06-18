def format_duration(time):
    # 3600 seconds in an hour
    # 86400 seconds in a day
    # 31536000 seconds in a year
    
    timeStr = ""
    count = 0

    if time == 0:
        return "now"
    else:
        # time conversions
        years = time // 31536000
        days = (time - years * 31536000) // 86400
        hours = (time - years * 31536000 - days * 86400) // 3600
        minutes = (time - years * 31536000 - days * 86400 - hours * 3600) // 60
        seconds = (time - years * 31536000 - days * 86400 - hours * 3600 - minutes * 60)
        
        timeDict = {"year": years, 
                    "day": days, 
                    "hour": hours, 
                    "minute": minutes, 
                    "second": seconds
                    }
        
    def plural(time: str, value: int) -> str:
        if value > 1:
            return f'{value} ' + time + 's'
        elif value == 1:
            return f'{value} ' + time
    
    # create a list to add each time value
    timeTracker = []
    for item in timeDict:
        if timeDict[item] > 0:
            timeTracker.append([item, timeDict[item]])
    
    # write out expanded time string, add to string each time through loop
    for item in timeTracker:
        count += 1
        if len(timeTracker) == 1:
            return plural(item[0], item[1])
        if count == len(timeTracker):
            timeStr = timeStr + " and " + plural(item[0], item[1])
        elif count == len(timeTracker) - 1:
            timeStr = timeStr + plural(item[0], item[1])
        else:
            timeStr = timeStr + plural(item[0], item[1]) + ', '
            

    return timeStr
