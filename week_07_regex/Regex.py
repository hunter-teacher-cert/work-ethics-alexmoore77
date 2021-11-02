import re

def find_date(line):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    result = re.findall(pattern,line)

    pattern = r"(October|Oct|November|Nov)( \d{1,2}, \d{4})"
    result = result + re.findall(pattern,line)
    return result

def find_name(line):
    pattern = r"[^(From)][^(Last)][^(Meanwhile)][^(Beyond)][^(Orkney)][A-Z][a-z]{3,} [A-Z][a-z]{3,}"
    result = re.findall(pattern,line)

    #pattern = r"[^From][^Last][^Meanwhile][^Beyond][^Orkney]Mrs?\.? [A-Z][a-z]{3,} [A-Z][a-z]{3,}"
    #result = re.findall(pattern,line)

    
        #pattern = r"\d"
    #result = result + re.findall(pattern,line)
    return result



#commented out 11-2-21
#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)

#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)

#f = open("datefile.dat")
#for line in f.readlines():
#    print(find_date(line))
f = open("frankenstein.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)