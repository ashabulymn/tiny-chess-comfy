import json,os,sys,urllib.request
U=os.environ.get('MAKEFUN_ENV_URL') or sys.exit('no env')
def p(x,b):
 r=urllib.request.Request(U+x,data=json.dumps(b).encode(),headers={'content-type':'application/json'})
 return json.load(urllib.request.urlopen(r))
V={'p':100,'n':320,'b':330,'r':500,'q':900,'k':20000}
def bd(f):
 a={};z=f.split()[0].split('/')
 for y,row in enumerate(z):
  x=0
  for c in row:
   if c.isdigit():x+=int(c)
   else:a['abcdefgh'[x]+str(8-y)]=c;x+=1
 return a
def key(m,a):
 t=a.get(m[2:4],'');u=a.get(m[:2],'p');return -(V.get(t.lower(),0)*10+V.get(m[4].lower(),0) if t else 0),V.get(u.lower(),0),m
while 1:
 g=p('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':g=p('/move',{'game':g['game'],'move':min(g['legal_moves'],key=lambda m:key(m,bd(g['fen'])))})
print('done',file=sys.stderr)