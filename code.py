import streamlit as st
import requests

def app():
    url = "https://icanhazdadjoke.com/"
    parameters = {
        "Accept" : "text/plain",
        "User-Agent": "VSCode",
    }

    response = requests.get(url, headers=parameters)
    return response.text

def addition(firstnum,secondnum):
    return firstnum + secondnum

def checkint(first,second):
    if type(first) == int and type(second) == int:
        return True
    
    # #first number not interger, second is integer
    # elif type(first) != int and type(second) == int:
    #     print ("first number is not integer \n")

    # #second number not interger, first is integer
    # elif type(first) == int and type(second) != int:
    #     print ("second number is not integer \n")

    else: 
        return False
    
def multiply (first,second):
    isnumber = checkint(first,second)
    if isnumber == True:
        return first * second 

    else:
        return False
    
st.title('dad joke app')
joke_button = st.button("Generate Joke", type="primary")
if joke_button: 
    st.write(app())

st.title('addition app')
number = st.number_input("Insert your first number", placeholder="Type a number", value=None, step=1, key=1)
number2 = st.number_input("Insert your second number", placeholder="Type a number", value=None, step=1, key=2)
if number and number2 :
    st.write(addition(number,number2))

st.title('multiplication app')
number3 = st.number_input("Insert your first number", placeholder="Type a number", value=None, step=1, key=3)
number4 = st.number_input("Insert your second number", placeholder="Type a number", value=None, step=1, key=4)
if number3 and number4 :
    st.write(multiply(number3,number4))
