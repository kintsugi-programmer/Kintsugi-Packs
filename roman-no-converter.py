"""
Sunday, July 26, 2020
Roman no converter 1-999

"""

def roman(_3digit_number_like_000_789_888_etc_):
       '''THIS IS THE PROGRAM TO CONVERT 1-999 NOS TO ROMAN NOS
       made by--SIDDHANT BALI'''
       p=''
       q=''
       r=''
       list1=[[1,'I'],[2,'II'],[3,'III'],[4,'IV'],[5,'V'],[6,'VI'],[7,'VII'],[8,'VII'],[9,'IX']]
       list2=[[1,'X'],[2,'XX'],[3,'XXX'],[4,'XL'],[5,'L'],[6,'LX'],[7,'LXX'],[8,'LXXX'],[9,'XC']]
       list3=[[1,'C'],[2,'CC'],[3,'CCC'],[4,'CD'],[5,'D'],[6,'DC'],[7,'DCC'],[8,'DCCC'],[9,'CM']]
       a=str(_3digit_number_like_000_789_888_etc_)
       unit=int(a[-1])
       tenth=int(a[-2])
       hundred=int(a[-3])
       b=0
       c=0
       d=0
       for j in range(9):
              if unit==int(list1[j][0]):
                     b=list1[j][1]

       for k in range(9):
              if tenth==int(list2[k][0]):
                     c=list2[k][1]

       for l in range(9):
              if hundred==int(list3[l][0]):
                     d=list3[l][1]

       if d!=0:
            p=d
       if c!=0:
            q=c
       if b!=0:
            r=b
     
       return (p+q+r)