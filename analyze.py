import csv

f = open('data/clean_data.csv', 'r')
csv_reader = csv.DictReader(f)
years = list()
totals = list()
averages = list()

for line in csv_reader:
    years.append(line["Year"])
    totals.append(float(line["J-D"]))
total = 0
decades = list()
f.close()

for i in range(9, len(totals), 10):
    averages.append(sum(map(float, totals[i-9:i+1])) / 10)
    decades.append(f"{years[i-9]}-{years[i]}")

print("Decade:       Average Temperature Anamoly:")
for i in range(len(decades)):
    print(str(decades[i])+"                "  + str(format(averages[i],'.1f')) + " °F")
