import requests
from datetime import date,timedelta


def main():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
    current_date = date.today()
    yesterday = current_date - timedelta(days=1)
    last_update = yesterday.strftime("%m-%d-%Y")
    url =  url+'/' + str(last_update) + '.csv'
    response = requests.get(url)
    
    ## We can check if data not available and do something else with it
    if response.status_code == 404 or response.status_code == 400:
       return print('No new data')
        
    ## data is inside of response.text
    print(response.text)

def saveToFile(data,filename):
    ##Write something to save the data to either json or csv
    ## Use the date as the file name so like this: 2020-03-28.csv or 2020-03-28.json 
    pass

def cleanData(data):
    ## Might want to clean the data before you save it so something here
    pass

if __name__ == "__main__":
    main()