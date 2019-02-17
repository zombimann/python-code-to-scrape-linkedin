
from flask import Flask
# import web driver
from selenium import webdriver
from time import sleep
from parsel import Selector
import json

app = Flask(__name__)

@app.route("/")
def home():
    link = 'https://www.linkedin.com/in/david-craven/'
    return mainOne(link)

# -*- coding: utf-8 -*-

# link = 'https://www.linkedin.com/in/david-craven/'
# function to ensure all key data fields have a value
def validate_field(field):
    # if field is present pass if field:
    if field:
        pass
    # if field is not present print text else:
    else:
        field = 'No results'
    return field


def mainOne(url):
    # specifies the path to the chromedriver.exe
    driver = webdriver.Chrome('C:/Users/fauzia zombimann/Downloads/chromedriver')
    
    # driver.get method() will navigate to a page given by the URL address
    driver.get('https://www.linkedin.com')
    
    # locate email form by_class_name
    username = driver.find_element_by_class_name('login-email')
    
    
    # send_keys() to simulate key strokes
    username.send_keys('YOUR-EMAIL')
    
    # locate password form by_class_name
    password = driver.find_element_by_class_name('login-password')
    
    # send_keys() to simulate key strokes
    password.send_keys('YOUR-PASSWORD')
    
    # locate submit button by_class_name
    #log_in_button = driver.find_element_by_class_name('login-submit')
    
    # locate submit button by_class_id
    #log_in_button = driver.find_element_by_class_id('login submit-button')
    
    # locate submit button by_xpath
    log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
    
    # .click() to mimic button click
    log_in_button.click()
    
    sleep(3)
    
    # get the profile URL 
    driver.get(url)
    
    sleep(5)
    
    # assigning the source code for the webpage to variable sel
    sel = Selector(text=driver.page_source) 
    
    #xpath to extract the first h1 text 
    name = sel.xpath('//h1/text()').extract_first()
    
    # xpath to extract the exact class containing the text
    #name1 = sel.xpath('//*[starts-with(@class, "pv-top-card-section__name")]/text()').extract_first()
    
    #Remove new line
    if name:
        name = name.strip()
    
    
    # xpath to extract the text from the class containing the job title
    job_title = sel.xpath('//*[starts-with(@class, "pv-top-card-section__headline")]/text()').extract_first()
    
    if job_title:
        job_title = job_title.strip()
    
    
    # xpath to extract the text from the class containing the company
    company = sel.xpath('//*[starts-with(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__company-name")]/text()').extract_first()
    
    if company:
        company = company.strip()
    
    
    # xpath to extract the text from the class containing the college
    college = sel.xpath('//*[starts-with(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__school-name")]/text()').extract_first()
    
    if college:
        college = college.strip()
    
    
    # xpath to extract the text from the class containing the location
    location = sel.xpath('//*[starts-with(@class, "pv-top-card-section__location")]/text()').extract_first()
    
    if location:
        location = location.strip()
    
    
    linkedin_url = driver.current_url
    
    # validating if the fields exist on the profile
    name = validate_field(name)
    job_title = validate_field(job_title)
    company = validate_field(company)
    college = validate_field(college)
    location = validate_field(location)
    linkedin_url = validate_field(linkedin_url)
    
    # printing the output to the terminal (for debugging)
    #print('\n')
    #print('Name: ' + name)
    #print('Job Title: ' + job_title)
    #print('Company: ' + company)
    #print('College: ' + college)
    #print('Location: ' + location)
    #print('URL: ' + linkedin_url)
    #print('\n')
    
    # create dictionary with the values
    thisdict = {
            'Name': name,
            'Job Title': job_title,
            'Company': company,
            'College': college,
            'Location': location,
            'URL': linkedin_url
            }
    
    # convert dictionary to json
    data_json = json.dumps(thisdict, indent=4, sort_keys=True)
    
    with open('data.json', 'w') as outfile:
        json.dump(thisdict, outfile, indent=4, sort_keys=True)
    
    # Display the json data to terminal (for debugging)
    # print(data_json)
    
    driver.quit()
    return data_json
    



if __name__ == "__main__":
    app.run(debug=True)


