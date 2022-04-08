message = input()
binary = ''
for x in message:
  bin = format(ord(x),'b')
  if len(bin)<7:
    bin='0'*(7-len(bin))+bin
  binary +=bin

answer=''
i=1
if binary[0] == '1':
    answer = '0 0'
else:
    answer = '00 0'
while i<len(binary):
    if binary[i]!=binary[i-1]:
        if binary[i] == '1':
            answer += ' 0 0'
        else:
            answer += ' 00 0'
    else:
        answer += '0'
    i+=1
    
print(answer)
