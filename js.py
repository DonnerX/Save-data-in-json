import json
import re

def search(txt,r1,r2):
    p_s=re.search(r1,txt).start()
    p_e=re.search(r2,txt).end()
    txt2=txt[p_s:p_e]
    return [txt2,p_s,p_e]

with open('Test_Fixed_Event_CATL_OK_new.a2l','r') as f:
    txt=f.read()
    f.close()


#--------------GET A2ML and HEAD---------------------#
print 'getting A2ML and HEAD...'
try:  
    p_e=re.search(r'.*/begin A2ML',txt).start()
    head=txt[0:p_e]
    txt=txt[p_e:]
    m=search(txt,r'.*/begin A2ML',r'.*/end A2ML\n')
    a2ml=m[0]
    txt=txt[:m[1]]+txt[m[2]:]
    data={'HEAD':head}
    data['A2ML']=a2ml
except:
    print "A2ML do not exist"
#---------------GET MOD_PAR-----------------------------#
print 'getting MOD_PAR...'
try:
    m=search(txt,r'    /begin MOD_PAR ',r'    /end MOD_PAR\n')
    mod_par=m[0]
    txt=txt[:m[1]]+txt[m[2]:]
    data['MOD_PAR']=mod_par
except:
    print "MOD_PAR do not exist"
#-----------------GET MOD_COMMON-----------------------#
print 'getting MOD_COMMON...'
try:
    m=search(txt,r'    /begin MOD_COMMON ""',r'    /end MOD_COMMON\n')
    mod_common=m[0]
    txt=txt[:m[1]]+txt[m[2]:]
    data['MOD_COMMON']=mod_common
except:
    print "MOD_common do not exist"
#------------------get IF_DATA XCP----------------------#
print 'getting IF_DATA XCP...'
try:
    m=re.search(r'.*(/)begin IF_DATA .*[CX]CP',txt)
    p_s=m.start(0)
    numplace=m.start(1)-p_s
    m=re.search(r'\s{%d}/end IF_DATA\n'%numplace,txt)
    p_e=m.end()
    data['XCP']=txt[p_s:p_e]
    txt=txt[:p_s]+txt[p_e:]
except:
    print "XCP do not exist"

#------------get IF_DATA CNP_CREATE_INI------------#
print 'getting CNP_CREATE_INI...'
try:
    m=re.search(r'.*(/)begin IF_DATA CNP_CREATE_INI',txt)
    p_s=m.start(0)
    numplace=m.start(1)-p_s
    m=re.search(r'\s{%d}/end IF_DATA\n'%numplace,txt)
    p_e=m.end()
    data['CNP']=txt[p_s:p_e]
    txt=txt[:p_s]+txt[p_e:]
except:
    print 'CNP do not exist'

#--------------------clear the enter--------------------#
m=re.match('\n*',txt)
rest=txt[m.end():]
#-------------------get measurements-----------------#
print 'getting measurements...'
meas={}
for m in re.finditer('.*/begin MEASUREMENT\s([\s\S]*?)\n[\s|\S]*?/end MEASUREMENT\n',rest):
    meas['%s'%m.group(1)]=m.group()
    rep=m.group()
    rep=re.sub('\[','\\[',rep)
    rep=re.sub('\]','\\]',rep)
    rep=re.sub('\(','\\(',rep)
    rep=re.sub('\)','\\)',rep)
    rep=re.sub('\+','\\+',rep)
    rep=re.sub('\-','\\-',rep)
    rep=re.sub('\*','\\*',rep)
    rep=re.sub('\?','\\?',rep)
    rep=re.sub('\^','\\^',rep)
    rep=re.sub('\$','\\$',rep)
    rep=re.sub('\{','\\{',rep)
    rep=re.sub('\}','\\}',rep)
    rep=re.sub('\|','\\|',rep)
    link = re.compile('%s'%rep)
    rest=re.sub(link,'',rest)
data['MEASUREMENT']=meas
#-------------------get characteristics-----------------#
print 'getting characteristics...'
char={}
for m in re.finditer('.*/begin CHARACTERISTIC\s([\s\S]*?)\n[\s|\S]*?/end CHARACTERISTIC\n',rest):
    char['%s'%m.group(1)]=m.group()
    rep=m.group()
    rep=re.sub('\[','\\[',rep)
    rep=re.sub('\]','\\]',rep)
    rep=re.sub('\(','\\(',rep)
    rep=re.sub('\)','\\)',rep)
    rep=re.sub('\+','\\+',rep)
    rep=re.sub('\-','\\-',rep)
    rep=re.sub('\*','\\*',rep)
    rep=re.sub('\?','\\?',rep)
    rep=re.sub('\^','\\^',rep)
    rep=re.sub('\$','\\$',rep)
    rep=re.sub('\{','\\{',rep)
    rep=re.sub('\}','\\}',rep)
    rep=re.sub('\|','\\|',rep)
    link = re.compile('%s'%rep)
    rest=re.sub(link,'',rest)
data['CHARACTERISTIC']=char
#--------------------get COMPU_METHOD--------------------#
print 'getting COMPU_METHOD...'
CM={}
for m in re.finditer('.*/begin COMPU_METHOD\s([\s\S]*?)\n[\s|\S]*?/end COMPU_METHOD\n',rest):
    CM['%s'%m.group(1)]=m.group()
    rep=m.group()
    rep=re.sub('\[','\\[',rep)
    rep=re.sub('\]','\\]',rep)
    rep=re.sub('\(','\\(',rep)
    rep=re.sub('\)','\\)',rep)
    rep=re.sub('\+','\\+',rep)
    rep=re.sub('\-','\\-',rep)
    rep=re.sub('\*','\\*',rep)
    rep=re.sub('\?','\\?',rep)
    rep=re.sub('\^','\\^',rep)
    rep=re.sub('\$','\\$',rep)
    rep=re.sub('\{','\\{',rep)
    rep=re.sub('\}','\\}',rep)
    rep=re.sub('\|','\\|',rep)
    link = re.compile('%s'%rep)
    rest=re.sub(link,'',rest)
data['COMPU_METHOD']=CM
#--------------------get COMPU_VTAB---------------------#
print 'getting COMPU_VTAB...'
CV={}
for m in re.finditer('.*/begin COMPU_VTAB\s([\s\S]*?)\n[\s|\S]*?/end COMPU_VTAB\n',rest):
    CV['%s'%m.group(1)]=m.group()
    rep=m.group()
    rep=re.sub('\[','\\[',rep)
    rep=re.sub('\]','\\]',rep)
    rep=re.sub('\(','\\(',rep)
    rep=re.sub('\)','\\)',rep)
    rep=re.sub('\+','\\+',rep)
    rep=re.sub('\-','\\-',rep)
    rep=re.sub('\*','\\*',rep)
    rep=re.sub('\?','\\?',rep)
    rep=re.sub('\^','\\^',rep)
    rep=re.sub('\$','\\$',rep)
    rep=re.sub('\{','\\{',rep)
    rep=re.sub('\}','\\}',rep)
    rep=re.sub('\|','\\|',rep)
    link = re.compile('%s'%rep)
    rest=re.sub(link,'',rest)
data['COMPU_VTAB']=CV
#--------------------get COMPU_VTAB_RANGE----------------#
print 'getting COMPU_VTAB_RANGE...'
CVR={}
s=[]
e=[]
for m in re.finditer('.*/begin COMPU_VTAB_RANGE\s([\s\S]*?)\n[\s|\S]*?/end COMPU_VTAB_RANGE\n',rest):
    CVR['%s'%m.group(1)]=m.group()
    s.append(m.start())
    e.append(m.end())
s.sort()
e.sort()
s.reverse()
e.reverse()
for i in range(len(s)):
    rest=rest[:s[i]]+rest[e[i]:]
data['COMPU_VTAB_RANGE']=CVR
#--------------------get RECORD_LAYOUT------------------#
print 'getting RECORD_LAYOUT...'
RL={}
for m in re.finditer('.*/begin RECORD_LAYOUT\s([\s\S]*?)\n[\s|\S]*?/end RECORD_LAYOUT\n',rest):
    RL['%s'%m.group(1)]=m.group()
    rep=m.group()
    rep=re.sub('\[','\\[',rep)
    rep=re.sub('\]','\\]',rep)
    rep=re.sub('\(','\\(',rep)
    rep=re.sub('\)','\\)',rep)
    rep=re.sub('\+','\\+',rep)
    rep=re.sub('\-','\\-',rep)
    rep=re.sub('\*','\\*',rep)
    rep=re.sub('\?','\\?',rep)
    rep=re.sub('\^','\\^',rep)
    rep=re.sub('\$','\\$',rep)
    link = re.compile('%s'%rep)
    rest=re.sub(link,'',rest)
data['RECORD_LAYOUT']=RL
#--------------------get GROUP------------------#
print 'getting GROUP...'
GP={}
for m in re.finditer('.*/begin GROUP\s([\s\S]*?)\n[\s|\S]*?/end GROUP\n',rest):
    GP['%s'%m.group(1)]=m.group()
    rep=m.group()
    rep=re.sub('\[','\\[',rep)
    rep=re.sub('\]','\\]',rep)
    rep=re.sub('\(','\\(',rep)
    rep=re.sub('\)','\\)',rep)
    rep=re.sub('\+','\\+',rep)
    rep=re.sub('\-','\\-',rep)
    rep=re.sub('\*','\\*',rep)
    rep=re.sub('\?','\\?',rep)
    rep=re.sub('\^','\\^',rep)
    rep=re.sub('\$','\\$',rep)
    link = re.compile('%s'%rep)
    rest=re.sub(link,'',rest)
data['GROUP']=GP
#--------------------clear the enter--------------------#
rest=re.sub('\n\n+','\n\n',rest)
#--------------------get rest-------------------------#
data['REST']=rest
#-------------------save as JSON-----------------------#
#json_str=json.dumps(data)

with open('a2l.json','w') as f:
    json.dump(data,f)
    f.close()
'''
with open('a2l.json','r') as f:
    data=json.load(f)
    f.close()


TEST=data['REST']
with open ('TEST.txt','w') as f:
    f.write(TEST)
    f.close()
'''
