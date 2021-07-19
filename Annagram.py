---Approach 1 ---
string1="REPLYL"
string2="RELPYM"
new_dictionary={}
for i in range(len(string1)):
    string=string1[i]
    count=string1.count(string)
    # new_dictionary.add(string,count)
    new_dictionary[string]=count
    print(string,count)
new_dict={}
for i in range(len(string2)):
    string=string2[i]
    count=string2.count(string)
    count1=new_dictionary.get(string)
    print(string,count,count1)
    if(count==count1):
        print("ÿes")
    else:
        print("NO")
    
    
print(new_dictionary)


---Approach 2-----
# if len(string1)==len(string2):
#     string1=sorted(string1)
#     string2=sorted(string2)
#     if string1==string2:
#         print("Anagram")
#     else:
#         print("Not")    
