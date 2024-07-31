with open("/Users/nrcase/research/cc/processing/partcipation.txt", "r") as file:
   unityIDs = file.read().splitlines()
   
with open("/Users/nrcase/research/cc/processing/anon.txt", "w") as file:
    count = 0
    for id in unityIDs:
        file.write(id + "," + "ncsu" + str(count) + "\n")
        count += 1
