import streamlit as st

st.title("Password Strenght Checker")
st.write("Use this simple tool to check the strenght of your password and get suggession on how to make it stronger. We will give you helpful tips to create a "
"Strong Password!")
# value = st.number_input("Enter your password")


digit: int = (0-9)

character:str = "upper_case()"
character2:str = "lower_case()"



def password_generator():
   if st.text_input("Enter your password to get started!"):
    result = character == "upper_case()" and character2 == "lower_case()"
    result = "At least must 8 in the character"
   
      
    st.success(result)
    st.button("please enter you started in password!")
    st.title ("Improvement Suggestion")
    st.write(" * password should contain both upper and lower case characters")
    st.write(" * password should contain at least one special character(!@#$%&*")
    st.write("* your password is weak.please make it stronger!")


result = password_generator()

# st.button("please enter started your password")
# st.text("click here!")

# character: str = ("upper_case" , "lower_case")
# number:int = 1, 2, 3, 4, 5, 6, 7, 8
# digit: int = (0-9)

# def password_generator():
#  if st.text_input("Enter your password to get started!"):
#    result = st.title()
#    st.success(result)
   
   # else:
   #    user = input("please enter your password to get started!")
      # st.write("password should contain both upper and lower case character")

# if st.button("Click Here"):
#    resuslt = (st.button)
# else:
#    ("please enter your password to get started")
# st.title ("Improvement Suggestion")
# st.write(" * password should contain both upper and lower case characters")
# st.write(" * password should contain at least one special character(!@#$%&*)")
# st.write("* your password is weak.please make it stronger!")







      
   





  