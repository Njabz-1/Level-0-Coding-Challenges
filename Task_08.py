def number_to_time(number):
    hours = number // 60
    minutes = number % 60
    result = ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") +\
    ("{0} minute{1}".format(minutes, "s" if minutes!=1 else "") if minutes else "")
    return result

number_to_time(122)