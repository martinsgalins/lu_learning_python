seconds = input("Seconds:")
sec_value = int(seconds) % (24 * 3600)
hour_value = sec_value // 3600
sec_value %= 3600
min_value = sec_value // 60
sec_value %= 60

print(hour_value, "hours", min_value, "minutes", sec_value, "seconds")
