#Aggregate Marks= Sum of marks obtained in all subjects

#Percentage marks= Aggrate marks/ Total Maximum Marks * 100

total_marks=0

for i in range(1,6):
    marks=int(input("Enter tha marks "))
    total_marks+=marks

Aggregate_marks=total_marks

Percentage_marks=Aggregate_marks/500*100

print("Aggregate_marks :-  ",Aggregate_marks)
print("Percentage_marks :-",Percentage_marks)

