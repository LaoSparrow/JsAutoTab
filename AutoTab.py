#!/bin/python

#I am not ensure if this will destroy your scripts or not because there must be some cases I didn't write into this code
#Same as last script 'Encode16', I didn't left comments on this code
#But it's different now, why I didn't left comments is because I am so lazy (

#(I am sad with my poor English)

#Author:LaoSparrow
#Date:22/12/2020


#Very IMPORTANT X3 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Before running this code, please REMOVE or RENAME the 'output.js' 




#Setting(s)
spaceInTab = 4



ret = input('Path to the file:')

f = open(ret,'r')
f.seek(0, 0)
inpf = f.read()
f.close()

outf = open('output.js','a+',encoding='UTF-8')
outf.seek(0,0)

def MakeTabs(numTabs):
    for e in range(numTabs):
        for i in range(spaceInTab):
            outf.write(' ')

jumpchar = 0
tabs = 0
for i in range(len(inpf)):
    if jumpchar > 0:
        jumpchar -= 1
        continue

    if inpf[i:i+len('}:function(){};')] == '}:function(){};':
        outf.write('\n')
        tabs -= 1
        MakeTabs(tabs)
        outf.write(inpf[i:i+len('}:function(){};')])
        outf.write('\n')
        MakeTabs(tabs)
        jumpchar = len('}:function(){};') - 1
        continue

    if inpf[i:i+5] == '})();' or inpf[i:i+5] == '}());':
        outf.write('\n')
        tabs -= 1
        MakeTabs(tabs)
        outf.write(inpf[i:i+5])
        outf.write('\n')
        MakeTabs(tabs)
        jumpchar = 4
        continue

    if inpf[i:i+4] == '}));' or inpf[i:i+4] == '}();':
        outf.write('\n')
        tabs -= 1
        MakeTabs(tabs)
        outf.write(inpf[i:i+4])
        outf.write('\n')
        MakeTabs(tabs)
        jumpchar = 3
        continue

    if inpf[i:i+3] == '});':
        outf.write('\n')
        tabs -= 1
        MakeTabs(tabs)
        outf.write(inpf[i:i+3])
        outf.write('\n')
        MakeTabs(tabs)
        jumpchar = 2
        continue

    if inpf[i:i+2] == '};':
        outf.write('\n')
        tabs -= 1
        MakeTabs(tabs)
        outf.write(inpf[i:i+2])
        outf.write('\n')
        MakeTabs(tabs)
        jumpchar = 1
        continue

    if inpf[i] == '}':
        outf.write('\n')
        tabs -= 1
        MakeTabs(tabs)
        outf.write(inpf[i])
        outf.write('\n')
        MakeTabs(tabs)
        continue

    if inpf[i] == '{':
        outf.write(inpf[i])
        outf.write('\n')
        tabs += 1
        MakeTabs(tabs)
        continue

    if inpf[i] == ';' or inpf[i] == ':':
        outf.write(inpf[i])
        outf.write('\n')
        MakeTabs(tabs)
        continue

    outf.write(inpf[i])

outf.close()