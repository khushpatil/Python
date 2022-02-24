import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))

# print(temp)

# data = pandas.read_csv("weather_data.csv")
# temp_data = data["temp"].to_list()
# avg_temp = sum(temp_data)/len(temp_data)
# print(round(avg_temp,3))
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp*1.8 + 32)

squirrel_data = pandas.read_csv("squirrel_data.csv")
Fur_color = squirrel_data["Primary Fur Color"]
gray_num =0 
black_num=0 
cin_num =0
for color in Fur_color.to_list():
    if color == "Gray":
        gray_num += 1
    elif color == "Cinnamon":
        cin_num += 1
    else:black_num += 1
number = []
number.extend((gray_num,black_num,cin_num))
color_list = ["Gray", "Black","Cinnamon"]
frame = {"Fur Color":color_list, "Count":number}
squirerl_count = pandas.DataFrame(frame)
squirerl_count.to_csv("./squirrel_count.csv")