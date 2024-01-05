import streamlit as st
import time

from monty_hall import simiulate


st.title('Monty Hall Simulation :door: :door: :car:')
st.image('pictures/monty_hall.png')

number_game = st.number_input("Enter number of game simulate: ",
                min_value=1, max_value=10000)

col1, col2 = st.columns(2)

win_switch = 0
win_no_switch = 0

col1.subheader("percent win with switch")
col2.subheader("percent win without switch")
chart1 = col1.line_chart(x=None, y=None, width=0, height=400)
chart2 = col2.line_chart(x=None, y=None, width=0, height=400)

for i in range(number_game):
    win_with_switch, win_with_no_switch = simiulate(1)

    win_switch += win_with_switch
    win_no_switch += win_with_no_switch

    chart1.add_rows([win_switch / (i + 1)])
    chart2.add_rows([win_no_switch / (i + 1)])

    time.sleep(0.01)