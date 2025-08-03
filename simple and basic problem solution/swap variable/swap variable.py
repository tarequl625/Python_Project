#type - 1
fisrtVariable = 10
secondVariable = 20
temporaryVariable = secondVariable
secondVariable = fisrtVariable
fisrtVariable = temporaryVariable
print("first variable is ",fisrtVariable)
print("second variable is ",secondVariable)

#type - 2
fisrtVariable = int(input("Enter first value : "))
secondVariable = int(input("Enter second value : "))
temporaryVariable = secondVariable
secondVariable = fisrtVariable
fisrtVariable = temporaryVariable
print("first variable is ",fisrtVariable)
print("second variable is ",secondVariable)

#type - 3
fisrtVariable = int(input("Enter first value : "))
secondVariable = int(input("Enter second value : "))
secondVariable,fisrtVariable = fisrtVariable,secondVariable
print("first variable is ", fisrtVariable)
print("second variable is ", secondVariable)

#type - 3
fisrtVariable,secondVariable,*other = input("Enter first and second value give a space : ").split()
secondVariable,fisrtVariable = fisrtVariable,secondVariable
print("first variable is ", fisrtVariable)
print("second variable is ", secondVariable)