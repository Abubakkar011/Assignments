#Importing the necessary libraries
import sqlite3
import database
import requests
from bs4 import BeautifulSoup

#Establishing connection with Database
def connection(db_name):
  con = sqlite3.connect(db_name)
  con.execute("Drop Table If Exists webPage")
  con.execute(
    "Create Table If Not Exists webPage(Name text,price text,description text,review text)"
  )
  con.close()

#Function to insert data in mysql database
def insert(db_name,values):
  con = sqlite3.connect(db_name)
  con.execute(
    "Insert into webPage(Name,price,description,review) Values(?,?,?,?)",
    (values[0], values[1], values[2], values[3]))
  con.commit()
  con.close()

#Function to print the inserted database in mysql database
def printer(db_name):
  con = sqlite3.connect(db_name)
  cur = con.cursor()
  cur.execute("Select * from webPage")
  data = cur.fetchall()
  for i in data:
    print(i)
  con.close()

#Code for scraping the website "WebScraper"
def webScraping():
  pages=int(input("Enter the total page's details you want (page should be <=4):"))
  page=1
  if pages>4:
    print("As you have crossed the max_limit of pages, we are now considering the total pages as 4")
    pages=4
  if pages<1:
    print("Enter the valid input!!")
  db_name=input("Enter the database name that you want to store:")
  
  while page<=pages and pages>=1:
    url = "https://www.webscraper.io/test-sites/e-commerce/static/computers/tablets?page="+str(page)
    req = requests.get(url)
    content = req.content
    soup = BeautifulSoup(content, "html.parser")
    cards = soup.find_all("div", {"class": "col-sm-4 col-lg-4 col-md-4"})
  
    web_list = []
    database.connection(db_name)
    for individual in cards:
      title = individual.find_all("h4")[-1]
      description = individual.find("p", {"class": "description"})
      price = individual.find("h4")
      reviews = individual.find_all("div", {"class": "ratings"})
      for review in reviews:
        rev = review.find("p", {"class": "pull-right"})
      web_list = [title.text, price.text, description.text, rev.text]
      database.insert(db_name,tuple(web_list))
  
    database.printer(db_name)
    page+=1

#Calling the function webScraping, where our main code is
webScraping()                                                                                                           
