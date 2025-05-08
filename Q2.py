import os
import pandas as pd

def save_to_file(data, file_name):
    with open(file_name, 'w+') as file:
        file.write(data)

def merge_all_data():

    file_directory = './temperature_data'
    all_data = []
    df = pd.DataFrame()

    try:
        for filename in os.listdir(file_directory):
            if filename.endswith('.csv'):
                file_path = os.path.join(file_directory, filename)
                try:
                    df = pd.read_csv(file_path)
                    df['Year'] = filename.split('_')[-1].split('.')[0]
                    # print(df)

                    all_data.append(df)
                
                except Exception as er:
                    raise er
            
        if all_data:
            df = pd.concat(all_data, ignore_index=True)
        else:
            print('No Data Found')

    except FileNotFoundError:
        print('Directory \'temperature_data\' not found')
        exit(1)
    
    finally:
        return df
    
def cal_average_temp(data):

    if data.empty:
        return
    
    # print(data)
    
    try:
        # if data:
            # print(data)
        seasons = {
            'Summer' : ['December', 'January', 'February'],
            'Winter' : ['June', 'July', 'August'],
            'Autumn' : ['March', 'April', 'May'],
            'Spring' : ['September', 'October', 'November']
        }

        # print(df)

        temp_text = 'Average Temperature For Each Season \n\n'
        # temp_text = temp_text + f'Season'

        for season, months in seasons.items():
            # print(df[months].mean())
            # print(season,round(df[months].mean().mean(),2))
            avg_value = round(data[months].mean().mean(), 1)
            temp_text = temp_text + f'Season: {season}, Temperature: {avg_value} (°C)\n'

        save_to_file(temp_text, 'average_temp.txt')
    
    except ValueError:
        print('No Data Found')


data = merge_all_data()

# cal_average_temp(data)

def find_temp_range(data):
    if data.empty:
        return
    
    try:
        print(data)
        print(data['STATION_NAME'])

    
    except Exception as er:
        raise er

find_temp_range(data)

