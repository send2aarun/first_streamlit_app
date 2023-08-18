import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_chice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_chice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return fruityvice_normalized

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information. ")
    
  else:
    back_from_function = get_fruityvice_data (fruit_choice)
    streamlit.dataframe(back_from_function)
    
# streamlit.stop()



# Next fewl line till streamlit.dataframe(fruityvice_normalize are replaced with try excpt
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# # streamlit.header("Fruityvice Fruit Advice!")
# # streamlit.text(fruityvice_response.json()) 

# # take the json version of the response and normalize it
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # output it the screen as a table
# streamlit.dataframe(fruityvice_normalized)


# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# # my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# # my_data_row = my_cur.fetchone()
# my_data_rows = my_cur.fetchall()
# # streamlit.text("Hello from Snowflake:")
# # streamlit.text("The fruit load list contains:")
# streamlit.header("The fruit load list contains:")
# # streamlit.text(my_data_row)
# streamlit.dataframe(my_data_rows)

# fruit_choice2 = streamlit.text_input('What fruit would you like to add?','Kiwi')
# # streamlit.write('The user entered ', fruit_choice2)
# streamlit.write('Thanks for adding ', fruit_choice2)
# my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")

