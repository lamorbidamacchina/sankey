import csv
import json

with open('sample_data.csv', newline='') as csvfile:
  data = list(csv.reader(csvfile))
  targets = data[0]
  del targets[0]
  senders = data
  del senders[0]
  y_length = len(senders)
  x_length = len(senders[0])
  sankey_list = []
  sankey_list_2 = []
  for i in range(y_length):
    #print(senders[i][0])
    sender = senders[i][0]
    for x in range(len(targets)):
      target = targets[x]
      value = int(senders[i][x+1])
      sankey_list.append([sender,target,value])
      sankey_list_2.append({"from":sender,"to":target,"value":value})


print("Generating files...")
with open('sankey_for_googlecharts.txt', 'w') as f:
    for item in sankey_list:
        f.write("%s,\n" % item)
with open('sankey_for_amcharts.txt', 'w') as f:
    for item2 in sankey_list_2:
        f.write("%s,\n" % item2)
print("Done!")