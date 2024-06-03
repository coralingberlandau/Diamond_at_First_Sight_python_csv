import csv
from enum import Enum
import pandas as pd
from helper.logic import average_carat_by_cut, average_diamond_price, average_price_by_color, highest_diamond_price, ideal_diamond_count, premium_median_carat, unique_diamond_colors

df = pd.read_csv('data.csv')

class Menu(Enum):
    HIGHEST = 1
    AVERAGE = 2
    IDEAL = 3
    COLORS = 4
    MEDIAN = 5
    AVERAGE_CARAT = 6
    AVERAGE_COLORS = 7
    EXIT = 8 

def display_menu():
    for men in Menu:
        print(f'{men.value} - {men.name}')
    return Menu(int(input("Choose what you want: ")))

if __name__ == "__main__":
    df = pd.read_csv('data.csv')
    while True:
        try:
            user_selection = display_menu()
            if user_selection == Menu.HIGHEST:highest_diamond_price(df) 
            if user_selection == Menu.AVERAGE:average_diamond_price(df)
            if user_selection == Menu.IDEAL:ideal_diamond_count(df)
            if user_selection == Menu.COLORS:unique_diamond_colors(df)
            if user_selection == Menu.MEDIAN:premium_median_carat(df)
            if user_selection == Menu.AVERAGE_CARAT:average_carat_by_cut(df)
            if user_selection == Menu.AVERAGE_COLORS:average_price_by_color(df)
            if user_selection == Menu.EXIT:exit()
        except Exception as e:
            print(f'Error: {e}')