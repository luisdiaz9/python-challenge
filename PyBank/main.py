import os
import csv
from statistics import mean
month = []
PAndL = []
PAndLChange = []
budget_csv = os.path.join( "budget_data.csv")
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        month.append(row[0])
        PAndL.append(float(row[1]))

PAndLChange =[x2 - x1 for (x1, x2) in zip(PAndL, PAndL[1:])]

print("Financial Analisis")
print("----------------------------")
print("Months Total : " + str(len(month)))
print("Total : $" + str(round(sum(PAndL))))
print("Average  Change : $" + str("{:.2f}".format(mean(PAndLChange))))
print("Greatest Increase in Profits: " +str(month[PAndLChange.index(max(PAndLChange))+1])+" ($"+ str(round(max(PAndLChange)))+")")
print("Greatest Decrease in Profits: " +str(month[PAndLChange.index(min(PAndLChange))+1])+" ($"+ str(round(min(PAndLChange)))+")")

tfile = open('output.txt', 'a')
tfile.write("Financial Analisis"+ '\n')
tfile.write("----------------------------"+'\n')
tfile.writelines("Months Total : " + str(len(month)))
tfile.writelines('\n')
tfile.write("Total : " + str(round(sum(PAndL))))
tfile.writelines('\n')
tfile.write("Average  Change : " + str("{:.2f}".format(mean(PAndLChange))))
tfile.writelines('\n')
tfile.write("Greatest Increase in Profits: " + str(month[PAndLChange.index(max(PAndLChange))+1]) + " ($"+ str(round(max(PAndLChange)))+")")
tfile.writelines('\n')
tfile.write("Greatest Decrease in Profits: " + str(month[PAndLChange.index(min(PAndLChange))+1]) + " ($"+ str(round(min(PAndLChange)))+")")
