seconds = int(input())
sec_to_hour = seconds / 3600
remain_sec = seconds % 3600
sec_to_mints = remain_sec / 60

remaining_second = seconds % 60
print(f"{int(sec_to_hour)}:{int(sec_to_mints)}:{int(remaining_second)}")