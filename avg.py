fname=input('Enter the name of your file here')
fhand=open(fname)
count=0
total=0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        ipos=line.find(':')
        piece=line[ipos+2:]
        value=float(piece)
        total=total+value
        count=count+1
        avg=total/count
    else:
      continue
print('Average spam confidence:',avg)
