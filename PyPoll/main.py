import os
import csv
import pandas as pd

udemy_csv = os.path.join( "election_data.csv")

VoterID = []
County = []
Candidate = []

AcmVoterID = []
AcmCounty = []
AcmCandidate = []
data_series2 = []

with open(udemy_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

AcmCandidate.append(0)
AcmVoterID.append(0)
for x in range(len(VoterID)):
    for y in range(len(AcmVoterID)):   
        if Candidate[x] == AcmCandidate[y]:
            AcmVoterID[y] = AcmVoterID[y] + 1
            break
        elif y == len(AcmVoterID)-1:
            AcmCandidate.append(Candidate[x])
            AcmVoterID.append(1)

Percentage= [ x/len(VoterID) for x in AcmVoterID ]
Max=round(max(Percentage),2)
MaxVoter=str(AcmCandidate[Percentage.index(max(Percentage))])

for j in range(1,len(AcmCandidate)) :
    #data_series= pd.DataFrame([{"Candidate " : str(AcmCandidate[j]) ,"Percentage " : str(Percentage[j]) ,"Total " : str(AcmVoterID[j])}])
    data_series2.append({"Candidate":str(AcmCandidate[j]),"Percentage": str("{:.3%}".format(Percentage[j])),"Total":"( "+str(AcmVoterID[j])+" )"})
    data_series3=pd.DataFrame(data_series2)
    data_series4=data_series3[["Candidate","Percentage","Total"]]
    data_series4=data_series3.set_index("Candidate")
print("Election Results")
print("----------------------------")
print("Total Votes : ", str(len(VoterID)))
print("----------------------------")
print(data_series4)
print("----------------------------")
print("Winner : ",str(MaxVoter),str("{:.3%}".format(Max)))
print("----------------------------")

tfile = open('Output_Candidate.txt', 'a')
tfile.write("Election Results"+ '\n')
tfile.write("----------------------------"+'\n')
tfile.writelines(["Total Votes : ", str(len(VoterID))])
tfile.writelines('\n')
tfile.write("----------------------------"+'\n')
tfile.write(data_series4.to_string())
tfile.writelines('\n')
tfile.write("----------------------------"+'\n')
tfile.writelines(["Winner : ",str(MaxVoter)," ",str("{:.3%}".format(Max))])
tfile.writelines('\n')
tfile.write("----------------------------"+'\n')
tfile.close()
