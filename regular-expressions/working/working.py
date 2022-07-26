import re

def main():
    value = convert(input("Hours: "))
    print(value)


def convert(s):
    converted = None
    hours = re.search("^([0-9])*:?([0-9])+ (AM|PM)? to ([0-9])*:?([0-9])+ (AM|PM)?$", s.strip())
    if hours:
        if not re.search(r'\d', s):
            raise ValueError
    else:
        raise ValueError
    converted = hours.group(0).split(" to ")
    for item in converted:
        if "AM" in item: # AM
            am_index = converted.index(item)
            item = item.replace("AM", "").strip()
            if ":" in item:
                hour, minute = item.split(":")
                if int(minute) >= 60 or int(minute) < 0 or int(hour) > 12 or int(hour) < 0:
                    raise ValueError
                if int(hour) == 12:
                    hour = "00"
                if len(hour) == 1:
                    hour = f"0{hour}"
                final_hour1 = f"{hour}:{minute}"
            else:
                hour = item
                if int(hour) == 12:
                    hour = "00"
                if len(hour) == 1:
                    hour = f"0{hour}"
                if int(hour) > 12 or int(hour) < 0:
                    raise ValueError
                final_hour1 = f"{hour}:00"
        else: # PM
            pm_index = converted.index(item)
            item = item.replace("PM", "").strip()
            if ":" in item:
                hour, minute = item.split(":")
                if int(minute) >= 60:
                    raise ValueError
                if int(hour) == 12:
                    final_hour2 = f"{hour}:{minute}"
                else:
                    final_hour2 = f"{int(hour) + 12}:{minute}"
            else:
                hour = item
                if int(hour) == 12:
                    final_hour2 = f"{hour}:00"
                else:
                    final_hour2 = f"{int(hour) + 12}:00"

    if am_index < pm_index:
        return f"{final_hour1} to {final_hour2}"
    else:
        return f"{final_hour2} to {final_hour1}"

if __name__ == "__main__":
    main()