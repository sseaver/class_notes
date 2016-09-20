import csv


with open("data.csv") as open_file:
    contents = open_file.readlines()
# print (contents[2].split(",")[2])


# clean_data = [row.replace("\n", "").split(",") for row in contents]
# print (clean_data[11][4])


# import csv
with open("data.csv") as open_file:
    # contents = csv.reader(open_file, deliminater=",")
    contents = csv.DictReader(open_file)
    print (list(contents)[1]["Water Temp"])
