import xlparser as xlp
import RESTFunctions as rf
import re
import requests as req
import sys, json



serverName='testnagios'
hgalias='This host group has been automatically created by wizzard'
cgalias='This contact group has been automatically created by wizzard'
xlsxFile='/usr/local/nagiosxi/html/config/uploads/FILE.xlsx'
ci=0
hi=0


hostGroup,contactGroup=xlp.groups(xlsxFile)

for key in hostGroup.keys():
    hostgrouplist = rf.getHostGroupName(serverName)
    if key not in hostgrouplist:
        hi+=1
        hresult=rf.createHostGroup(key, hgalias, serverName)


for key in contactGroup.keys():
    contactgrouplist = rf.getContactGroupName(serverName)
    if key not in contactgrouplist:
        ci+=1
        cresult=rf.createContactGroup(key, cgalias, serverName)





