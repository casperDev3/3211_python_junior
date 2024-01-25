# comments

# testnameuser = "test"  # chaotic
# testNameUser = 'test'  # camel case
# TestNameUser = "test" # paskal case
# # test-name-user =  'test' # kebab case
# test_name_user = "test" # snake case

# TYPES -- Primitives

# #### string (str)
#
# txtOne = "Test Hello World!"
# txtTwo = 'test Hrllelel kfkfk'
# txtThree = """test three"""
# txtFour = '''test four'''
#
# ### numbers
# # integer (int)
# numOne = 234
# # float (float)
# numTwo = 23.4
# # complex
# numThree = 21j
#
# ### boolean
# bOne = True
# bTwo = False
#
# ### None
# vNone = None

# # OPERATION with primitives types
# print("Type function --", type(txtOne))
# print("UpperCase -- ", txtOne.upper())
# print("LowerCase -- ", txtOne.lower())
# print("Capitalize --", txtOne.capitalize())
# print("Title -- ", txtThree.title())
# print("Get Letter", txtOne[2])
#
# # number
# print("Plus = ", numTwo + numOne)
# print("Mimus = ", numTwo - numOne)
# print("Multi = ", numTwo * numOne)
# print("Dev = ", numTwo / numOne)
# print("Up = ", numTwo**2)
# print("Full = ", numTwo % 2)
# print("Inc = ", numOne + 1)
# print("Dec = ", numOne - 1)
# print("Round = ", round(numTwo / numOne, 2))

# # cond numbers
# print(numOne >= numTwo)
# print(numOne > numTwo)
# print(numOne < numTwo)
# print(numOne <= numTwo)
# print(numOne == numTwo)
# print(numOne != numTwo)

####### --- INPUT DATA --- #######
# template data John Patrick Doe
print("Doe J. P.")
firstName = input("Please enter your firstname:  ").capitalize()
fathersName = input("Please enter your fathersname:  ").capitalize()
lastName = input("Please enter your lastname:  ").capitalize()

# print(lastName + " " + firstName[0] + ". " + fathersName[0] + ".")
pib = f"{lastName} {firstName[0]}. {fathersName[0]}."
print(pib)