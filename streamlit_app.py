import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My Parents New Healthy Diner')
# streamlit.text('                                 --Viki & Suki')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg 🫣')
streamlit.text(' 🥑 + 🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#DISPLAY THE TABLE ON THE PAGE
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])


# #New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")


# # import requests
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# streamlit.header("Fruityvice Fruit Advice!")
# streamlit.text(fruityvice_response.json()) 

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
