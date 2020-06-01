# Write-a-program-that-prompts-for-a-file-name-then-opens-that-file-and-reads-through-the-file-looking for lines of the form:
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
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
