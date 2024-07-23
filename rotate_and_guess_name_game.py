import random
print("--Welcome--")
print("Rotate and find my classmate name ")
print("Note1:you will have 7 names you have to score more than 5 to win the Game")
name_list=["vikade","unar","eshgan","hrames","eshdi","thampuru","hiab","shithhar",
           "yuda","ajibal","ankapri","ythrim","ishathr","uvanbh","shahar","mulunarashi",
           "anaanj","vanibha","smiyatha","ayasreej","udharsuns","ayaj","hyaadit","aaln",
           "anshob","atsaiven","ruma","karumashan","shithar","kilako","thickkar","uryajayas",
           "vasulusrini","yaram","lajasia","gavibar","anaarch","hittic","hnuvis","dulkarten"]
answer_list=[4,2,3,1,3,4,2,5,1,3,4,5,4,4,3,4,3,4,5,7,8,2,3,1,2,5,1,3,4,4,5,4,6,2,4,4,3,5,3,4,6]

score=0
print("Note: By rotating the string you can find my classmate name")
for i in range(7):
    name=random.choice(name_list)
    name_index=name_list.index(name)
    print("---"+name+"--- find me")
    print("Enter the number of rotation ")
    
    rotation=int(input())
    rotated_string_name=name[rotation:]+name[:rotation]
    
    if answer_list[name_index]==rotation:
        score+=1
        
        print("It,s correct the name our classmate is {}".format(rotated_string_name))

    else:
        print("It's wrong Buddy")
if score>=5:
    print("You have won the game you have scored: ",score)
else:
    print("You Lost the game you scored only:",score)

    
        
    

    
    