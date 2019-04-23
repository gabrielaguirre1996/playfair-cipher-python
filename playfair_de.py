import sys
def matrix(key):
    matrix=[]
    for e in key:
        if e not in matrix:
            matrix.append(e)
    letters="abcdefghiklmnopqrstuvwxyz"
    
    for e in letters:
        if e not in matrix:
            matrix.append(e)
            
            
    matrix_box=[]
    for e in range(5):
        matrix_box.append('')
        
    matrix_box[0]=matrix[0:5]
    matrix_box[1]=matrix[5:10]
    matrix_box[2]=matrix[10:15]
    matrix_box[3]=matrix[15:20]
    matrix_box[4]=matrix[20:25]
    return matrix_box
            
def messages(message_user):
        message=[]
        for e in message_user:
            message.append(e)
            
        for unused in range(len(message)):
            if " " in message:
                message.remove(" ")
                
        i=0
        for e in range(len(message)/2):
            if message[i]==message[i+1]:
                message.insert(i+1,'x')
            i=i+2
            
        if len(message)%2==1:
            message.append("x")
            
        i=0
        new=[]
        for x in xrange(1,len(message)/2+1):
            new.append(message[i:i+2])
            i=i+2
        return new
        
def position(matrixk, letter):
    x=y=0
    for i in range(5):
        for j in range(5):
            if matrixk[i][j]==letter:
                x=i
                y=j
                
    return x,y
    
def decrypt(user_cipher):
    #print 'line 61: ' + user_cipher
    
    cipher=cipherx(user_cipher)
    matrixk=matrix(key)
    # print matrixk
    plaintext=[]
    for e in cipher:
       # print 'before Position()'
        x1,y1=position(matrixk,e[0])
        x2,y2=position(matrixk,e[1])
        # print x1,y1
        if x1==x2:
            if y1==4:
               y1=-1
            if y2==4:
                y2=-1
            plaintext.append(matrixk[x1][y1-1])
            plaintext.append(matrixk[x1][y2-1])     
        elif y1==y2:
            if x1==4:
                x1=-1;
            if x2==4:
                x2=-1;
            plaintext.append(matrixk[x1-1][y1])
            plaintext.append(matrixk[x2-1][y2])
        else:
            plaintext.append(matrixk[x1][y2])
            plaintext.append(matrixk[x2][y1])

    #for unused in range(len(plaintext)):
        #if "x" in plaintext:
            #plaintext.remove("x")
    
    output=""
    for e in plaintext:
        output+=e
    return output.lower()
    
def cipherx(cipher):
    i=0
    new=[]
    for myx in range(len(cipher)/2):
        new.append(cipher[i:i+2])
        i=i+2
    return new
    

# key=raw_input("Please input the key : ")
key=sys.argv[1].lower()

user_cipher=''
if len(sys.argv) == 2:
    user_cipher = raw_input('Please input the cipher : ')
else:
    file = open(sys.argv[2], 'r')
    user_cipher = file.read()
    file.close()

original = decrypt(user_cipher)
print original

fh = open("encrypt-me.txt","w")
fh.write( original )
fh.close()