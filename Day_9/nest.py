names = {"Sara" : "Swiss", "Deani": "Paris"}
travel_log = {"France" : ["Pairs","Lille", "Dijon"], 
              "Miami" : ["Pairs", "Dijon"]
              }

for key in travel_log:
    for i in (travel_log[key]):
        if i == "Lille":
            print(i)

nestedd_list = ["A", "B", ["C", "D"]]
print(nestedd_list[2][1])
# print *D

travel_log_1 = {
      "France" : {"visited ": 8, 
                "total_visit": ["paris","lyon", "rome"]
},

       "Germany" : {"visited ": 10, 
                "total_visits": ["Berlin","lyon", "Sttutgart"]}}

print(travel_log_1["Germany"]["total_visits"][2])