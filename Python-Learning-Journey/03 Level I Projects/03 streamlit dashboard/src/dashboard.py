import streamlit as st
from pass_generator import RandomPasswordGenerator, PinCode, MemorablePassword
from nltk.corpus import words

st.image('https://img.freepik.com/premium-vector/security-password-minimal-vector-line-icon-3d-button-isolated-black-background-premium-vectorxaxa_570929-1761.jpg', width=550)
st.title(":closed_lock_with_key: Password generatare :closed_lock_with_key:")

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
   type_ = st.radio("Select your type of the password", ["Random Password", "Pincode Password", "Memorable Password"])

#  type_ = st.radio("Select your type of the password", ["Random Password", "Pincode Password", "Memorable Password"])

if type_ == "Pincode Password":
    num_ = st.slider('number of chars', 8, 32)

    generator = PinCode(num_)

elif type_ == "Random Password":
    num_ = st.slider("number of chars: ",min_value=5, max_value=50)
    have_num = st.toggle("Include Number")
    have_sym = st.toggle("Include Symbol")

    generator = RandomPasswordGenerator(number=num_, include_number=have_num, include_symbol=have_sym)

elif type_ == "Memorable Password":
    num_ = st.slider("Number of Char",1 , 10)
    devider_ = st.text_input("Your Devider: ", value="_")
    have_upper_ = st.toggle("Include Upper Case")

    generator = MemorablePassword(number=num_, devider=devider_, have_upper=have_upper_)

password = generator.generate()
st.write(f"Your password: ``` {password} ```")