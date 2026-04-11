print("enter the mark for below subject")
math= int(input("math :"))
eng= int(input ("english :"))
ss= int(input ("socal :"))
sci= int (input ("science :"))
average= (eng + math + ss + sci) / 4
print(average)
if average >= 81 & average <= 100 :
    print("grade A")
elif  average >= 61 & average <= 80 :
    print("grade B")
elif average >= 41 & average <= 60 :
    print("grade C")
else :
    print("grade F")
       
   

