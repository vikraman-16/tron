def encrypt(text ,rails):
    fence=[[' 'for _ in range (len(text))] for _ in range(rails)]
    rail=0
    direction =1

    for char in text:
        fence[rail][0]=char
        rail+=direction
        if rail ==0 or rail ==rails-1:
            direction *= -1
    encrypt_text=''.join(char for row in fence for char in row if char!= ' ')
    return encrypt_text

def decrypt(text,rails):
    fence=[[' 'for _ in range (len(text))] for _ in range(rails)]
    rail=0
    direction=1 

    for i in range(len(text)):
        fence[rail][i]='*'
        rail+=direction

        if rail==0 or rail == rails -1:
            direction *=-1
    index=0
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j]=='*' and index <len(text):
                fence [i][j]= text[index]
                index += 1

    rail=0
    direction=1
    decrypt_text=''

    for i in range(len(text)):
        decrypt_text += fence[rail][i]
        rail+= direction

        if rail ==0 or rail ==rails -1:
            direction *= -1

    return decrypt_text

message= "HELLOWORLD"
rails = 3 
encrypt_text=encrypt(message,rails)
decrypt_text=decrypt(encrypt_text,rails)

print(message)
print(encrypt_text)
print(decrypt_text)
