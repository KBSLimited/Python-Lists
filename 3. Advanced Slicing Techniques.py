#Task 1: Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temperatures = temperatures[7:14]
print("Temperatures for the second week of the month:", second_week_temperatures)

#Task 2: Extract all the temperatures above 100.
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

above_100_temperatures = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100:", above_100_temperatures)

#Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Reverse the list
reversed_temperatures = temperatures[::-1]

# Extract temperatures from the 5th to the 10th day of the reversed list
extracted_temperatures = reversed_temperatures[4:10]

print("Temperatures from the 5th to the 10th day of the reversed list:", extracted_temperatures)