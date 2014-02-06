#Created by SVRobots
#January 14 2014 Version

import itertools
import sys
import time
import hashlib
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value
import ctypes
from time import sleep

mlength=6
length=0
chars="abcdefghijklmnopqrstuvwxyz"
i=0
p=8

def scan(chars,length,lindex,uindex,h,term):
  sets=itertools.product(chars, repeat=length)
  index=0
  pas="a"
  for b in sets:
    index=index+1
    if index >= lindex:
      if index < uindex and term.value==0:
        pas=""
        for a in b:
          pas=pas+a
        m = hashlib.md5()
        m.update(pas)
        if h == m.hexdigest():
          print "Password:",pas
          term.value=1
      else:
        break

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "hash and or max length missing"
    print "[MD5_HASH] [MAX_LENGTH] <process_limit> <character_set>"
  mlength=int(sys.argv[2])
  h = sys.argv[1]
  if len(sys.argv) >= 4:
    p=int(sys.argv[3])
    if p < 1:
      p=1
    if p > 8:
      p=8
  if len(sys.argv) == 5:
    chars=sys.argv[4]
  st=time.time()
  lock = Lock()
  term=Value('i',0,lock=False)
  while length<mlength and term.value==0:
    length=length+1
    llength=0
    rlength=0
    slength=pow(len(chars),length)+1
    sub=int((pow(len(chars),length)/p)+10)
    while slength > 0:
      if slength <= sub:
        llength=rlength
        rlength=llength+slength
        i=i+slength
        slength=0
      else:
        llength=rlength
        rlength=llength+sub
        slength=slength-sub
        i=i+sub
      thread1 = Process(target = scan, args=(chars,length,llength,rlength,h,term))
      thread1.start()
      
      if p > 1:
        if slength <= sub:
          llength=rlength
          rlength=llength+slength
          i=i+slength
          slength=0
        else:
          llength=rlength
          rlength=llength+sub
          slength=slength-sub
          i=i+sub
        thread2 = Process(target = scan, args=(chars,length,llength,rlength,h,term))
        thread2.start()
      if p > 2:
        if slength <= sub:
          llength=rlength
          rlength=llength+slength
          i=i+slength
          slength=0
        else:
          llength=rlength
          rlength=llength+sub
          slength=slength-sub
          i=i+sub
        thread3 = Process(target = scan, args=(chars,length,llength,rlength,h,term))
        thread3.start()
      
      if p > 3:
        if slength <= sub:
          llength=rlength
          rlength=llength+slength
          i=i+slength
          slength=0
        else:
          llength=rlength
          rlength=llength+sub
          slength=slength-sub
          i=i+sub
        thread4 = Process(target = scan, args=(chars,length,llength,rlength,h,term))
        thread4.start()
      
      if p > 4:
        if slength <= sub:
          llength=rlength
          rlength=llength+slength
          i=i+slength
          slength=0
        else:
          llength=rlength
          rlength=llength+sub
          slength=slength-sub
          i=i+sub
        thread5 = Process(target = scan, args=(chars,length,llength,rlength,h,term))
        thread5.start()
      
      if p > 5:
        if slength <= sub:
          llength=rlength
          rlength=llength+slength
          i=i+slength
          slength=0
        else:
          llength=rlength
          rlength=llength+sub
          slength=slength-sub
          i=i+sub
        thread6 = Process(target = scan, args=(chars,length,llength,rlength,h,term))
        thread6.start()
      
      if p > 6:
        if slength <= sub:
          llength=rlength
          rlength=llength+slength
          i=i+slength
          slength=0
        else:
          llength=rlength
          rlength=llength+sub
          slength=slength-sub
          i=i+sub
        thread7 = Process(target = scan, args=(chars,length,llength,rlength,h,term))
        thread7.start()
      
      if p > 7:
        if slength <= sub:
          llength=rlength
          rlength=llength+slength
          i=i+slength
          slength=0
        else:
          llength=rlength
          rlength=llength+sub
          slength=slength-sub
          i=i+sub
        thread8 = Process(target = scan, args=(chars,length,llength,rlength,h,term))
        thread8.start()
      sleep(1)
      
      done=p
      if p==1:
        while thread1.exitcode==None:
          sleep(1)
      if p==2:
        while thread1.exitcode==None or thread2.exitcode==None:
          sleep(1)
      if p==3:
        while thread1.exitcode==None or thread2.exitcode==None or thread3.exitcode==None:
          sleep(1)
      if p==4:
        while thread1.exitcode==None or thread2.exitcode==None or thread3.exitcode==None or thread4.exitcode==None:
          sleep(1)
      if p==5:
        while thread1.exitcode==None or thread2.exitcode==None or thread3.exitcode==None or thread4.exitcode==None or thread5.exitcode==None:
          sleep(1)
      if p==6:
        while thread1.exitcode==None or thread2.exitcode==None or thread3.exitcode==None or thread4.exitcode==None or thread5.exitcode==None or thread6.exitcode==None:
          sleep(1)
      if p==7:
        while thread1.exitcode==None or thread2.exitcode==None or thread3.exitcode==None or thread4.exitcode==None or thread5.exitcode==None or thread6.exitcode==None or thread7.exitcode==None:
          sleep(1)
      if p==8:
        while thread1.exitcode==None or thread2.exitcode==None or thread3.exitcode==None or thread4.exitcode==None or thread5.exitcode==None or thread6.exitcode==None or thread7.exitcode==None or thread8.exitcode==None:
          sleep(1)
  
  print "Elapsed Time:",(time.time()-st)
