
import RESTFunctions as rf
grouplist=[]

serverName='testnagios'

a=rf.getContactGroupName(serverName)
b=rf.getHostGroupName(serverName)
grouplist.append(a)
grouplist.append(b)
print(grouplist)
