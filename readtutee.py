tutee_department = list()
def readdata_tutee():
  file = open("Tutee Forms.csv", "r")
  lines = file.readlines()
  file.close()
  tutees = list()
  
  for line in lines[1:]:
    line = line.strip()
    line = line.split(",")
    tutee = list()
    for i in range (10):
      if line[i] == '' and i >= 7:
        continue
      else:
        tutee.append(line[i].strip('\"'))
    tutee_department.append(tutee[4])
    tutees.append(tutee)
  return tutees

def createdataTutee():
  tutees = readdata_tutee()
  #print(tutees)
  dict = {}
  #add all the deparments that have tutee (no duplication)
  for element in tutee_department:
    if element not in dict:
      dict[element] = list()
  
  for element in dict:
    n = 0
    for i in tutees:
      if i[4] == element:
        tutee_dict = {}
        tutee_dict["id"] = n
        tutee_dict["tnumber"] = int(i[3])
        tutee_dict["name"] = i[1]
        tutee_dict["courses"] = i[-1]
        #if preferred or blacklist is empty then insert an empty list:
        if i[5] == '':
          tutee_dict["preferred"] = list()
        else:
          tutee_dict["preferred"] = i[5].split(",")
        if i[6] == '':
          tutee_dict["blacklist"] = list()
        else:
          tutee_dict["blacklist"] = i[6].split(",")
        
        if tutee_dict not in dict[element]:
          dict[element].append(tutee_dict)
        n+=1
  return dict

def main():
  tutee = createdataTutee()
  for key in tutee:
    print(key)
    print(tutee[key])
    print()

if __name__ == "__main__":
   main()