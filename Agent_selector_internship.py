import random

def Create_agent(n):
    all_agents=[]
    for i in range(n):
        print("Input the following for Agent Number",i+1,"...")
        is_available=input("is_available(True/False):")
        while(is_available!="True" and is_available!="False"):
              print("Invalid value.please type either True or False")
              is_available=input("is_available(True/False):")

        if is_available=="True":
            available_since=int(input("available since(seconds):"))
            while(available_since<0):
                print("time cannot be negative.Try again")
                available_since=int(input("available since(seconds):"))
            
        elif is_available=="False": 
            available_since=-int(input("time needed by agent to be free(seconds)"))
            while(available_since>0):
                print("time cannot be negative.Try again")
                available_since=-int(input("time needed by agent to be free(seconds)"))
                
        roles=list(map(str,input("roles(separated by comma)=").split(",")))
        print()
        print()
        
        
        all_agents.append([is_available,available_since,roles])
    return(all_agents)

def Create_issues():
    issues=[]
    for i in range(int(input("input number of issues:"))):
        print("input the following for issue number",i+1)
        role=list(map(str,input("issue roles(separated by comma)=").split(",")))
        print("input agent selection mode")
        print("1:All available")
        print("2:least busy")
        print("3:random")
        mode=int(input("enter 1,2 or 3:"))
        while(mode!=1 and mode!=2 and mode!=3):
            print("invalid number.Try again")
            mode=int(input("enter 1,2 or 3:"))
        completion_time=int(input("time needed by agent to complete this issue(seconds)"))
        while(completion_time<0):
            print("time cannot be negative.Try again")
            completion_time=int(input("time needed by agent to complete this issue(seconds)"))
        issues.append([mode,role,completion_time])
        print()
        print()
    return(issues)

    


def Agent_selector(agents,issues):
    i=0
    while(i<len(issues)):
        j=0
        newval=[]
        maximum=0
        maxi=0
        while(j<len(agents)):
            if agents[j][0]!="False":
                flag=1
                for x in issues[i][1]:
                    #print(agents[j][2])
                    if x not in agents[j][2]:
                        flag=0
                        break
                if flag==1:
                    #print("yes issues",i+1,"is resolved by agent",j+1)
                    if maximum<agents[j][1]:
                        maximum=agents[j][1]
                        maxi=len(newval)
                    newval.append([j+1,agents[j]])
            j+=1

        if len(newval)==0:
            print("No agent meet the requirements of ISSUE NO",i+1," or is busy in solving some other issue")
            print()
        elif issues[i][0]==1:
            agent_no=[]
            if len(newval)==1:
                print("Agents that is used for ISSUE",i+1,"is:")
                print("Agent No.",newval[0][0])
                print()
                agents[newval[0][0]][0]="False"
                agents[newval[0][0]][1]=issues[i][2]+1
                print()
            else:
                print("Agents that can be used for ISSUE",i+1,"are:")
                for i in range(len(newval)):
                    print(i+1,":[Agent No.",newval[i][0],"]")
                    agent_no.append(newval[i][0])
                    
                print("Choose anyone between the above agents:(all availability mode)")
                choose=int(input())
                while(choose not in agent_no ):
                    print("Invalid agent no please choose the right one")
                    choose=int(input())
                print()
                print()
                agents[choose-1][0]="False"
                agents[choose-1][1]=issues[i][2]+1
                print()
        elif issues[i][0]==2:
            print("Agent used for ISSUE",i+1,"is:")
            print("Agent No.",newval[maxi][0])
            print()
            print()
            agents[maxi][0]="False"
            agents[maxi][1]=issues[i][2]+1
        else:
            print("Agent used for ISSUE",i+1,"is:")
            n=random.randint(0,len(newval)-1)
            print("Agent No.",newval[n][0])
            print()
            print()
            agents[newval[n][0]-1][0]="False"
            agents[newval[n][0]-1][1]=issues[i][2]+1
            
        ################################
        #changing the time
        for m in range(0,len(agents)):
            if agents[m][0]=="True":
                agents[m][1]+=1
            elif agents[m][0]=="False":
                if agents[m][1]>1:
                    agents[m][1]-=1
                else:
                    agents[m][0]="True"
                    agents[m][1]=0
            
        ###############################
        #print("All agents after issue",i,"are")
        #print(agents)
        i+=1
            
            
            
            
            
                
        
    


if __name__ == "__main__": 
    
    n=int(input("total number of agents="))
    all_agents=Create_agent(n)
    print("AGENTS CREATED...")
    print()
    for i in range(0,len(all_agents)):
        print("Agent no "+str(i+1)+"=",end="")
        print(all_agents[i])
    print()
    print()
    issues=Create_issues()
    #print(issues)
    print()
    print("ISSUES DONE")
    print()
    Agent_selector(all_agents,issues)
