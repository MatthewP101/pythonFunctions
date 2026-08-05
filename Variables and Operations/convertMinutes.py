def convertMintues(totalMinutes):
    hours = totalMinutes // 60
    minutes = totalMinutes % 60
    return hours, minutes

time = convertMintues(200)

print ("The hours and minutes are:")
print(time)