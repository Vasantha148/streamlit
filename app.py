import streamlit as st 
st.title("fibnacci series")
a=st.text_input(label="enter the value")
print(a)
if (a.isdigit()):
    st.success("number")
else:
    st.warning("not a number")
import streamlit as st

st.title("Nth Fibonacci Term")

a = st.text_input(label="Enter the term number (n)")

if st.button("Submit"):
    try:
        num = int(a)
        if num < 0:
            st.write("Please enter a non-negative number")
        elif num == 0:
            st.write("Fibonacci term 0 is:", 0)
        else:
            fib_a, fib_b = 0, 1
        for i in range(num):
                fib_a, fib_b = fib_b, fib_a + fib_b
        st.write("Fibonacci term", num, "is:", fib_a)
    except ValueError:
        st.write("Please enter a valid number (positive integer)")


st.title("check numbers in string")

a = st.text_input(label="Enter the input")

if st.button("enter"):
    for i in range(len(a)):
        if a[i].isdigit():
            st.write(a[i])
