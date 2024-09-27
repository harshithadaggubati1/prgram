emp={'eno':[1,2,3],'ename':['A','B','C'],'esal':[10000,22000,30000]}
print("\n The Employee dataset is:")
print(emp)
print("------------------------------------")
print("\n The Employee Name are:",emp['ename'])
print("------------------------------------")
print("\n The Employee salaries are:")
print("------------------------------------")
for i in emp['esal']:
    print(i)