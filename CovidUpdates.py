from plyer import notification
import requests
from bs4 import BeautifulSoup
import pandas as pd

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="covidNotiIco.ico",
        timeout=15
    )
contries,totalcases,new_cases,total_deaths,new_deaths,total_recovered=[],[],[],[],[],[]
headers=['contries','total_cases','new_cases','total_deaths','new_deaths','total_recovered']
def getData(url,notycon):
    soup=BeautifulSoup(requests.get(url).content,'html.parser')
    tablebody=soup.find('tbody')
    ttt=tablebody.find_all('tr')
    for i in ttt:
        id=i.find_all('td')
        if id[1].text.strip().replace(",",'').lower()==notycon:
            contries1=id[1].text.strip().replace(",",'')
            totalcases1=id[2].text.strip().replace(",",'')
            newcases1 = id[3].text.strip().replace(",", '')
            total_deaths1 = id[4].text.strip().replace(",", '')
            new_deaths1=id[5].text.strip().replace(",", '')
            total_recovered1 = id[6].text.strip().replace(",", '')
            return contries1, totalcases1, newcases1, total_deaths1, new_deaths1, total_recovered1

    contries1 = 'not found'
    totalcases1 = 'not found'
    newcases1 = 'not found'
    total_deaths1 = 'not found'
    new_deaths1 = 'not found'
    total_recovered1 = 'not found'
    return contries1, totalcases1, newcases1, total_deaths1, new_deaths1, total_recovered1

def downdatascsv(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    tablebody = soup.find('tbody')
    ttt = tablebody.find_all('tr')
    for i in ttt:
        id = i.find_all('td')
        totalcases.append(id[2].text.strip().replace(",",''))
        new_cases.append(id[3].text.strip().replace(",",""))
        total_deaths.append(id[4].text.strip().replace(",",""))
        new_deaths.append(id[5].text.strip().replace(",",""))
        total_recovered.append(id[6].text.strip().replace(",",""))
        contries.append(id[1].text.strip().replace(",",""))
    print("COUNTRIES:",contries)
    print("TOTAL CASES:",totalcases,"\nNEW CASES:",new_cases)
    print("NEW DEATHS:", new_deaths, "\nTOTAL DEATHS:", total_deaths)
    print("TOTAL RECOVERED:",total_recovered)
    downloaddatas=list(zip(contries,totalcases,new_cases,new_deaths,total_deaths,total_recovered))
    df=pd.DataFrame(data=downloaddatas,columns=["COUNTRIES","TOTAL CASES","NEW CASES","NEW DEATHS","TOTAL DEATHS","TOTAL RECOVERED"])
    print(df)
    df.to_csv("COVID19-UPDATES.csv")
    df.to_json("COVID19-UPDATES.json")
def downdatasjson(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    tablebody = soup.find('tbody')
    ttt = tablebody.find_all('tr')
    for i in ttt:
        id = i.find_all('td')
        totalcases.append(id[2].text.strip().replace(",",''))
        new_cases.append(id[3].text.strip().replace(",",""))
        total_deaths.append(id[4].text.strip().replace(",",""))
        new_deaths.append(id[5].text.strip().replace(",",""))
        total_recovered.append(id[6].text.strip().replace(",",""))
        contries.append(id[1].text.strip().replace(",",""))
    print("COUNTRIES:",contries)
    print("TOTAL CASES:",totalcases,"\nNEW CASES:",new_cases)
    print("NEW DEATHS:", new_deaths, "\nTOTAL DEATHS:", total_deaths)
    print("TOTAL RECOVERED:",total_recovered)
    downloaddatas=list(zip(contries,totalcases,new_cases,new_deaths,total_deaths,total_recovered))
    df=pd.DataFrame(data=downloaddatas,columns=["COUNTRIES","TOTAL CASES","NEW CASES","NEW DEATHS","TOTAL DEATHS","TOTAL RECOVERED"])
    print(df)
    df.to_json("COVID19-UPDATES.json")
if __name__=="__main__":
    contry,totalcas,newcas,total_death,new_death,total_recover=getData('https://www.worldometers.info/coronavirus/',"usa")
    notifyMe("COVID-19 GLOBAL UPDATES","IN {}\nTotal Cases : {}\nTotal Deaths : {}\nNew Cases : {}\nNew Deaths : {}\nTotal Recovered : {}".format(contry,totalcas,newcas,total_death,new_death,total_recover))
    print(contry)
    print(totalcas)
    print(newcas)
    print(total_death)
    print(new_death)
    print(total_recover)