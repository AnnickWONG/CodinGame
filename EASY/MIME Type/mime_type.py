# For each of the Q filenames, display on a line the corresponding MIME type. 
# If there is no corresponding type, then display UNKNOWN.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

TBL = dict() # Dictionary to store the association table.

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    TBL[ext.lower()] = mt
    
for i in range(q):
    fname = input()  # One file name per line.
    if '.' in fname:
        type = fname.split('.')[-1].lower()
        print(TBL[type] if type in TBL.keys() else "UNKNOWN")
    else:
        print("UNKNOWN")
  
