for i in range(1,3):
    print("select the choice \npress 1 to encode the message")
    print("press 2 to decode the message ")
    choice=int(input())
    if choice==1:
            
        print("Enter your message-")
        message=input()
        emessage=""
        
        for i in message:
            emessage+=str(ord(i))+" "
        print(emessage)
        print("Copy and send the encoded message in whatsapp")
    
    elif choice==2:
        decodedmessage=""
        print("paste the encoded message")
        dmessage=input().split(" ")
        for i in dmessage:
                decodedmessage+=chr(int(i))
        print(decodedmessage)
            
            
        
