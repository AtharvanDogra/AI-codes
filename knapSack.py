#from collections import defaultdict

dict = {1:[1,500],2:[3,900],3:[5,700],4:[7,800]}      #[weight,profit]
capacity_bag=5
stored = 0
stored_dict= {}

sorted_dict = {k:v for k,v in sorted(dict.items(),key=lambda pw_Ratio: pw_Ratio[1][1]/pw_Ratio[1][0],reverse=True)}

print(sorted_dict)

i=1         #first key is 1, which is the product to steal [from sorted dict]

weight=0    #name for indices
profit=1    # " " " "
while stored < capacity_bag:
    if stored + sorted_dict[i][weight] < capacity_bag :
        stored = stored + sorted_dict[i][weight]
        stored_dict[i] = sorted_dict[i]
        i = i+1
        print(stored)
    
    else:
        ratio = (capacity_bag-stored)/sorted_dict[i][weight]
        stored_dict[i]=[ratio,ratio*sorted_dict[i][profit]]
        stored = stored + ratio*sorted_dict[i][weight]
        print(stored)
print(stored_dict)

