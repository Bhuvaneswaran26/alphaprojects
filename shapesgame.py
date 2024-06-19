import random
def question():
    print("Hello "+ name+" find my name--selectchoice by a b c d")
def correct():
    print("It,s correct",name)
def wrong():
    print("so sad wrong ",name)
    
def pyramid(score):
    for i in range(1,a+1):
        spaces="  "*(a-i)
        stars="* "*(2*i-1)
        print(spaces+stars)
    question()
    print("a.Inverted pyramid")
    print("b.Rightangled traingle")
    print("c.Pyramid")
    print("d.Hollow pyramid")
    ans=input()
    if ans=='c':
        score+=1
        
        
        correct()
        return score  
       
    else:
        wrong()
      
def invertedpyramid(score):
    for i in range(1,a+1):
        spaces="  "*i
        stars="* "*((2*a)-(2*i-1))
        print(spaces+stars)
    question()
    print("a.Inverted pyramid")
    print("b.Rightangled traingle")
    print("c.Pyramid")
    print("d.Hollow pyramid")
    ans=input()
    if ans=='a':
       
        
        correct()
        score+=1
        return score  
    else:
        wrong()
    return score
def hollowpyramid(score):
    for i in range(1,a+1):
        space1=" "*(a-i)
        star="* "
        middlespace=" "*((2*i)-4)
        if i==1 or i==a:
            print(space1+(star)*i)
        else:
            print(space1+star+middlespace+star)
    question()
    print("a.Inverted pyramid")
    print("b.Rightangled traingle")
    print("c.Inverted hollowPyramid")
    print("d.Hollow pyramid")
    ans=input()
    if ans=='d':
        correct()
        score+=1
        return score  
    else:
        wrong()
    
def invertedhollowpyramid(score):
    
    for i in range(1,a+1):
        space=" "*i
        star="* "
        middlespace=" "*(2*a-(2*i+2))
        if i==1 or i==a:
            print(space+star*(a-i+1))
        else:
            print(space+star+middlespace+star)
        question()
        print("a.Inverted pyramid")
        print("b.pyramid")
        print("c.InvertedhollowPyramid")
        print("d.Hollow pyramid")
        ans=input()
        if ans=='c':
            correct()
            score+=1
            return score   
        else:
            wrong()
def leftsided_lowerbase_rightangled_traingle(score):
    for i in range(1,a+1):
        print("* "*i)
    question()
    print("a.Leftsided_lowerbase_rightangled_traingle")
    print('b.Rightsided_lowerbase_rightangled_traingle')
    print('c.Traingle')
    print("d.square")
    ans=input()
    if ans=='a':
        correct()
        score+=1
    else:
        wrong()
    return score
def rightsided_lowerbase_rightangled_traingle(score):
    for i in range(1,a+1):
        space="  "*(a-i)
        star="* "*i
        print(space+star)
    question()
    print("a.Leftsided_lowerbased_rightangled_traingle")
    print('b.Rightsided_lowerbased_rightangled_traingle')
    print('c.Traingle')
    print("d.square")
    ans=input()
    if ans=='b':
        correct()
        score+=1 
    else:
        wrong()
    return score
def rightsided_upperbase_rightangled_traingle(score):
    for i in range(1,a+1):
      spaces="  "*(i-1)
      stars="* "*(a-i-1)
      print(spaces+stars)
    question()
    print("a.Leftsided_lowerbased_rightangled_traingle")
    print('b.Rightsided_lowerbased_rightangled_traingle')
    print("c.Leftsided_upperbased_rightangled_traingle")
    print('d.Rightsided_upperbased_rightangled_traingle')
    ans=input()
    if ans=='d':
        correct()
        score+=1 
    else:
        wrong()
    return score
def leftsided_upperbase_rightangled_traingle(score):
    for i in range(1,a+1):
      print((a-i-1)*"* ")
    question()
    print("a.Leftsided_lowerbased_rightangled_traingle")
    print('b.Rightsided_lowerbased_rightangled_traingle')
    print("c.Leftsided_upperbased_rightangled_traingle")
    print('d.Rightsided_upperbased_rightangled_traingle')
    ans=input()
    if ans=='c':
        correct()
        score+=1 
    else:
        wrong()
    return score

def leftsided_lowerbase_hollowrightangled_traingle(score):
    for i in range(1,a+1):
      middle_spaces="  "*(i-2)
      star="* "
   
      if i==1 or i==a:
            print(star*i)
      else:
            print(star+middle_spaces+star)
    question()
    print("a.Leftsided_lowerbased_hollow_rightangled_traingle")
    print('b.Rightsided_lowerbased_hollow_rightangled_traingle')
    print("c.Leftsided_upperbased_hollow_rightangled_traingle")
    print('d.Rightsided_upperbased_hollow_rightangled_traingle')
    ans=input()
    if ans=='a':
        correct()
        score+=1 
    else:
        wrong()
    return score
def leftsided_upperbase_hollowrightangled_traingle(score):
    for i in range(1,a+1):
        spaces="  "*(a-i-1)
        star="* "
        if i==1 or i==a:
            print(star*(a-i+1))
        else:
            print(star+spaces+star)
    question()
    print("a.Leftsided_lowerbased_hollow_rightangled_traingle")
    print('b.Rightsided_lowerbased_hollow_rightangled_traingle')
    print("c.Leftsided_upperbased_hollow_rightangled_traingle")
    print('d.Rightsided_upperbased_hollow_rightangled_traingle')
    ans=input()
    if ans=='c':
        correct() 
        score+=1
    else:
        wrong()
    return score
def rightsided_lowerbase_hollowrightangled_traingle(score):
    for i in range(1,a+1):
        spaces="  "*(a-i)
        middle_spaces=" "*(2*i-4)
        star="* "
        if i==1 or i==a:
            print(spaces+star*(i))
        else:
            print(spaces+star+middle_spaces+star)  
    question()
    print("a.Leftsided_lowerbased_hollow_rightangled_traingle")
    print('b.Rightsided_lowerbased_hollow_rightangled_traingle')
    print("c.Leftsided_upperbased_hollow_rightangled_traingle")
    print('d.circle')
    ans=input()
    if ans=='b':
        correct()
        score+=1 
    else:
        wrong()
    return score
def rightsided_upperbase_hollowrightangled_traingle(score):
    for i in range(1,a+1):
        spaces="  "*(i-1)
        middle_spaces="  "*(a-i-1)
        star="* "
        if i==1 or i==a:
            print(spaces+star*(a-i+1))
        else:
            print(spaces+star+middle_spaces+star)
    question()
    print("a.Rectangle")
    print('b.Rightsided_upperbased_hollow_rightangled_traingle')
    print("c.Leftsided_upperbased_hollow_rightangled_traingle")
    print('d.pentagon')
    ans=input()
    if ans=='b':
        correct()
        score+=1 
    else:
        wrong()
    return score
def square(score):
    for i in range(1,a+1):
        print("*  "*a)
         
    question()
    print("a.Rectangle")
    print('b.Rightsided_upperbased_hollow_rightangled_traingle')
    print("c.Square")
    print('d.pentagon')
    ans=input()
    if ans=='c':
        correct()
        score+=1 
    else:
        wrong()
    return score    
def hollowsquare(score):
    for i in range(1,a+1):
        star="*  "
        space="   "*(a-2)
        if i==1 or i==a:
            print(star*a)
        else:
            print(star+space+star)
    question()
    print("a.Rectangle")
    print('b.Hollow_square')
    print("c.Square")
    print('d.pentagon')
    ans=input()
    if ans=='b':
        correct()
        score+=1 
    else:
        wrong()
    return score  
def hollowrectangle(score):
    for i in range(1,a+1):
        space="    "*(a-2)
        star="*   "
        if i==1 or i==a:
            print(star*a)
        else:
            print(star+space+star)
    question()
    print("a.Rectangle")
    print('b.Hollow_square')
    print("c.Square")
    print('d.Hollow_rectangle')
    ans=input()
    if ans=='d':
        correct()
        score+=1 
    else:
        wrong()
    return score  
def rectangle(score):
    for i in range(1,a+1):
        print("*   "*a)
    question()
    print("a.Rectangle")
    print('b.Hollow_square')
    print("c.Square")
    print('d.Hollow_rectangle')
    ans=input()
    if ans=='a':
        correct()
        score+=1 
    else:
        wrong()
    return score  
def rhombus(score):
    for i in range(1,a+1):
        spaces="  "*(a-i)
        stars="* "*(2*i-1)
        print(spaces+stars)
    for i in range(1,a+1):
        spaces="  "*i
        stars="* "*((2*a)-(2*i-1))
        print(spaces+stars)
    question()
    print("a.Rectangle")
    print('b.Hollow_square')
    print("c.Hollow_rhombus")
    print('d.Rhombus')
    ans=input()
    if ans=='d':
        correct() 
        score+=1
    else:
        wrong()
    return score  
def hollowrhombus(score):
    for i in range(1,a+1):
        space1=" "*(a-i)
        star="* "
        middlespace=" "*((2*i)-4)
        if i==1:
            print(space1+(star)*i)
        else:
            print(space1+star+middlespace+star)
    for i in range(1,a+1):
        space=" "*i
        star="* "
        middlespace=" "*(2*a-(2*i+2))
        if i==a:
            print(space+star*(a-i+1))
        else:
            print(space+star+middlespace+star)
    question()
    print("a.Rectangle")
    print('b.Hollow_square')
    print("c.Hollow_rhombus")
    print('d.Rhombus')
    ans=input()
    if ans=='c':
        correct()
        score+=1 
    else:
        wrong()
    return score  
#program execution 
print("Enter your name buddy")
name=input()   
score=0
a=8
for i in range(10):
    lis=['pyramid','invertedpyramid','hollowpyramid','invertedhollowpyramid',
         'leftsided_lowerbase_rightangled_traingle','rightsided_lowerbase_rightangled_traingle',
         'leftsided_upperbase_rightangled_traingle','rightsided_upperbase_rightangled_traingle',
         'leftsided_lowerbase_hollowrightangled_traingle','leftsided_upperbase_hollowrightangled_traingle',
         'rightsided_lowerbase_hollowrightangled_traingle','rightsided_upperbase_hollowrightangled_traingle',
         'square','hollowsquare','rectangle','hollowrectangle','rhombus','hollowrhombus']
    c=random.choice(lis)
    if c=='pyramid':
        score=pyramid(score)
    elif c=='invertedpyramid':
       score= invertedpyramid(score)
    elif c=='hollowpyramid':
        score=hollowpyramid(score)
    elif c=='invertedhallowpyramid':
       score= invertedhollowpyramid(score)
    elif c=='leftsided_lowerbase_rightangled_traingle':
        score=leftsided_lowerbase_rightangled_traingle(score)
    elif c=='rightsided_lowerbase_rightangled_traingle':
        score=rightsided_lowerbase_rightangled_traingle(score)
    elif c=='rightsided_upperbase_rightangled_traingle':
        score=rightsided_upperbase_rightangled_traingle(score)
    elif c=='leftsided_upperbase_rightangled_traingle':
        score=leftsided_upperbase_rightangled_traingle(score)
    elif c=='leftsided_lowerbase_hollowrightangled_traingle':
        score=leftsided_lowerbase_hollowrightangled_traingle(score)
    elif c=='leftsided_upperbase_hollowrightangled_traingle':
       score= leftsided_upperbase_hollowrightangled_traingle(score)
    elif c=='rightsided_lowerbase_hollowrightangled_traingle':
        score=rightsided_lowerbase_hollowrightangled_traingle(score)
    elif c=='rightsided_upperbase_hollowrightangled_traingle':
        score=rightsided_upperbase_hollowrightangled_traingle(score)
    elif c=='square':
        score=square(score)
    elif c=='hollowsquare':
        score=hollowsquare(score)
    elif c=='rectangle':
       score= rectangle(score)
    elif c=='hollowrectangle':
        score=hollowrectangle(score)

    elif c=='rhombus':
        score=rhombus(score)
    elif c=='hollowrhombus':
        score=hollowrhombus(score)
print(name,"you have scored--",score)

        
