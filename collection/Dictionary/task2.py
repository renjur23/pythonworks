student_data={
    "hari":[45,40,32],
    "eldho":[35,40,32],
    "gopi":[46,40,33],
    "libin":[47,30,32],
}



user_input=int(input("Enter the index -->"))

avg={k:sum(v)/len(v) for k,v in student_data.items()}

# for i,element in enumerate(student_data):
    
#     if i+1==user_input:
        
#         total_mark=student_data.get(element)
        
#         avg=sum(total_mark)/len(total_mark)
        
        
print(f"the average markis {avg}")