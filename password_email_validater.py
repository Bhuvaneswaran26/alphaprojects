#email and password verifier
def password_checker(password):
    lowercheck=True
    uppercheck=True
    digitcheck=True
    specialcheck=True
    for i in password:
        c=ord(i)
        if i.isdigit():
            digitcheck=False
        elif i==i.upper():
            uppercheck=False
        elif i==i.lower():
            lowercheck=False
        elif not((c>64 and c<91) or (c>96 and c<123) or (c>46 and c<58)):
            specialcheck=False
            
    if lowercheck:
        print("Lowercase character is missing")
    if uppercheck:
        print("Uppercase character is missing")
    if digitcheck:
        print("Number is missing") 
    if specialcheck:
        print("specialcharacter is missing")
    if not(lowercheck and uppercheck and digitcheck and specialcheck):
        print("your password "+password+" is valid")
    else:
        print("Invalid Password")
def email_checker(gmail):
    status=True
    if gmail.endswith("@gmail.com") and (not(gmail.startswith("."))) and not(gmail[0].isdigit()) and not(".." in gmail):
       for i in gmail:
           c=ord(i)
           if i=="." or i=="@":
               if i=="@":
                    break
           else:
               if not((c>64 and c<91) or (c>96 and c<123) or (c>46 and c<58)):
                    status=False
    else:
        status=False
    if status:
        print("your Gamil is valid")
    else:
        print("Your Gmail is Invalid")

                    

        

    
print("Enter the password")
a=input()
password_checker(a)
print("Enter your Email")
a=input()
email_checker(a)
