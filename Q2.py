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
                    df['YEAR'] = filename.split('_')[-1].split('.')[0]

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
    
    try:
        seasons = {
            'Summer' : ['December', 'January', 'February'],
            'Winter' : ['June', 'July', 'August'],
            'Autumn' : ['March', 'April', 'May'],
            'Spring' : ['September', 'October', 'November']
        }


        temp_text = 'Average Temperature For Each Season \n\n'

        for season, months in seasons.items():
            avg_value = round(data[months].mean().mean(), 1)
            temp_text = temp_text + f'Season: {season}, Temperature: {avg_value} (°C)\n'

        save_to_file(temp_text, './average_temp.txt')
    
    except ValueError:
        print('No Data Found')


def find_temp_range(data):
    if data.empty:
        return
    
    try:
        range_text = ''
        months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
            
        data['TEMP_RANGE'] = data[months].max(axis=1) - data[months].min(axis=1)
    
        station = data.loc[data['TEMP_RANGE'].idxmax()]
        
        range_text = range_text + f'Station with largest temperature range: \n\n'

        range_text = range_text + f"Station Name: {station['STATION_NAME']}, Temperature: {round(station['TEMP_RANGE'], 1)} (°C)"

        save_to_file(range_text, 'largest_temp_range_station.txt')

    except ValueError:
        print('No Data Found')

    except Exception as er:
        raise er

def find_warmest_and_coolest_station(data):
    if data.empty:
        return
    
    try:
        warmest_text = 'Warmest and Coolest Station \n\n'
        months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
        
        data['AVG_TEMP'] = data[months].mean(axis=1)
        
        # find the warmest and coolest station, but there can be multiple stations with the same temperature
        warmest_station = data.loc[data['AVG_TEMP'].idxmax()]
        coolest_station = data.loc[data['AVG_TEMP'].idxmin()]

        warmest_text = warmest_text + f"Warmest Station Name: {warmest_station['STATION_NAME']}, Temperature: {round(warmest_station['AVG_TEMP'], 1)} (°C)\n"
        warmest_text = warmest_text + f"Coolest Station Name: {coolest_station['STATION_NAME']}, Temperature: {round(coolest_station['AVG_TEMP'], 1)} (°C)"

        save_to_file(warmest_text, './warmest_and_coolest_station.txt')

    except ValueError:
        print('No Data Found')

    except Exception as er:
        raise er

if __name__ == '__main__':
    
    data = merge_all_data()
    
    find_temp_range(data)
    cal_average_temp(data)
    find_warmest_and_coolest_station(data)
