d = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero',-1:'one',-2:'two',-3:'-three',-4:'-four',-5:'-five',-6:'-six',-7:'-seven',-8:'-eight',-9:'-nine'}
val = int(input('enter value: '))
print('{} is {}'.format(val,d.get(val) if (d.get(val) is not None) else '-ve number' if val<-9 else '+ve number'))