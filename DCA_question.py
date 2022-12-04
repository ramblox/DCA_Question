


def get_all_combinations(input1):

    list_of_combinations=[]

    for i in range(0,len(input1)):

        for j in range(0,len(input1)):

            if j>i:
                list_of_combinations.append((input1[i],input1[j]))

    return list_of_combinations


def get_dict_of_teams(list_of_combinations):
    
    n=0
    teams={}
    temp_teams={}
    for i in list_of_combinations:
            current_split=[i]
            n+=1

            for j in list_of_combinations:

                h=0

                if(len(set(i).intersection(set(j)))==0):
                    for k in current_split:
                        if(len(set(k).intersection(set(j)))==0):
                            h+=1
                    if h==len(current_split):
                        current_split.append(j)


            temp_teams[n]=current_split

    ##temp_teams have duplicates
    ##removing duplicates
    i=0
    for key,val in temp_teams.items():
        i+=1
        if i<=len(temp_teams)/2:
            teams[key]=val
    
    return temp_teams


def teams_with_same_skill(dict_of_teams):

    n=0
    final_dict_of_teams={}

    for i in dict_of_teams.values():

        current_split=i
        sum_of_skill=[]

        for team in current_split:
            sum_of_skill.append(sum(team))
        
        if(len(set(sum_of_skill))==1):
            n+=1
            final_dict_of_teams[n]=i
    
    return final_dict_of_teams


def gettotaleff(same_skill_teams):

    total_eff=0
    for i in same_skill_teams.values():

        for j in i:
             total_eff=total_eff+j[0]*j[1]
    
    return total_eff
        
            
        


if __name__=="__main__":
    
    input1=[int(i) for i in input('Enter the values').split(',')]

    list_of_combinations=get_all_combinations(input1)

    print("list of combinations are", list_of_combinations)

    dict_of_teams=get_dict_of_teams(list_of_combinations)

    print("the possible splits for teams are",dict_of_teams)

    same_skill_teams=teams_with_same_skill(dict_of_teams)

    print("The teams with same skill are", same_skill_teams)

    if (len(same_skill_teams)==0):
        print("-1")
    
    else:

        total_efficiency=gettotaleff(same_skill_teams)

        print("The total efficiency is ", total_efficiency)   