import streamlit as st

st.title('Alien = :blue[Friend]:alien:')
st.subheader('Have fun exploring the galaxy!', divider='blue')

number = st.number_input("How many aliens would you want to befriend?")
st.write("YAY! You now have ", number, " alien friends!")

st.divider()

st.image('https://images.prismic.io/star-trek-untold/YjRkMDRmYTUtZDdkZS00ZGM0LWE3YWEtNTgyODhkMzUzMWNk_essay_rr_what-is-a-galaxy.jpg?auto=compress%2Cformat&rect=0%2C0%2C2000%2C1080&h=1080&width=3840')

st.subheader('current conditions')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "-450 °F", "7.77 °F")
col2.metric("Wind", "1,000,000 mph", "-9%")
col3.metric("Humidity", "0%", "0%")

st.write(':milky_way:')
