#Loading required libraries

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL='https://timely-sunshine-e821b3.netlify.app/'

#Loading the web page in memory using requests library
page=requests.get(URL)

#Check the status code of the page
page.status_code

#Extracting the HTML code of the web page
htmlCode=page.text
soup=BeautifulSoup(htmlCode,"html.parser")
htmlCode
soup
content=soup.find_all('div',attrs={'class':'a'})
print(content)
content=soup.find('div',attrs={'class':'name'})
text=content.text
print(text)
content=soup.find('div',attrs={'class':'name'})
text=content.text.strip()
print(text)
content=soup.find('div',attrs={'class':'price'})
text=content.text
print(text)
content=soup.find('div',attrs={'class':'image'})
img_tag=content.find('img')
img_src=img_tag['src'] if img_tag else None
print(f"Content:{content}\nImageTag:{img_tag}\nImageSrc:{img_src}")
content=soup.find('div',attrs={'class':'price'})
text=content.text.strip()
print(text)
soup=BeautifulSoup(htmlCode,'html.parser')

#Extract all items
items=soup.find_all('div',class_='a')

print("******************items************************\n",items)

#List to store extracted data
names=[]
prices=[]
images=[]

#Loop through each item and extract details

for item in items:
    name=item.find('div',class_='name').text.strip()
    price=item.find('div',class_='price').text.strip()
    image_tag=item.find('div',class_='image').find('img')
    image_src=image_tag['src'] if image_tag else None #Extract src attribute

    #Append data to lists
    names.append(name)
    prices.append(price)
    images.append(image_src)
#Print results
print("Names:",names)
print("Prices:",prices)
print("Images:",images)

df=pd.DataFrame({'Product_Name':names,'MRP':prices,'Image_SRC':images})
df

#saving the dataframe
df.to_csv('productdetails.csv',header=True,index=False)
print("\nCSV file 'productdetails.csv' has been saved successfully.")