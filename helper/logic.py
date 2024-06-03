def highest_diamond_price(df):
    highest_price = df['price'].max()
    print(f'Highest diamond price: {highest_price}')

def average_diamond_price(df):
    average_price = df['price'].mean()
    print(f'Average diamond price: {average_price}')

def ideal_diamond_count(df):
    ideal_count = df[df['cut'] == 'Ideal'].shape[0]
    print(f'Ideal diamond count: {ideal_count}')

def unique_diamond_colors(df):
    unique_colors = df['color'].unique()
    color_count = len(unique_colors)
    print(f'Number of unique diamond colors: {color_count}')
    print(f'Unique diamond colors: {unique_colors}')

def premium_median_carat(df):
    median_carat = df[df['cut'] == 'Premium']['carat'].median()
    print(f'Median carat for Premium diamonds: {median_carat}')

def average_carat_by_cut(df):
    average_carat = df.groupby('cut')['carat'].mean().to_string()
    print(f'Average carat by cut:\n{average_carat}')

def average_price_by_color(df):
    average_price = df.groupby('color')['price'].mean().to_string()
    print (f'Average price by color:\n{average_price}')