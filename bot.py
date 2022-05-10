from unicodedata import name
import discord
import random
import http.client
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

#variable that holds the path for the chrome driver. This driver file is necessary for selenium web automation tasks
path = "C:/Users/18486/Desktop/chromedriver/chromedriver.exe"


#variable that holds and retrieves the url for local roadside assistance companies.
url = 'https://www.google.com/search?q=roadside+assistance+near+me&sxsrf=ALiCzsY0I94ebpy1WaleYg3GbNOCgCR2iw%3A1651787750031&source=hp&ei=5Ud0YtHLOq_IptQPr4aE8A8&iflsig=AJiK0e8AAAAAYnRV9jnOSv1ETQsrYEcjPAWT01_w4_ca&oq=roads&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCCMQyQMQJzIFCAAQkgMyBQgAEJIDMgQIIxAnMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIOCC4QgAQQsQMQxwEQrwEyCwguEIAEEMcBEK8BOggIABCxAxCDAToFCAAQgAQ6CwguEIAEELEDENQCOgsILhCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CAguEIAEELEDOgsIABCABBCxAxCDAToOCC4QgAQQsQMQxwEQ0QM6CwguELEDEMcBEKMCOgcILhCxAxAKOgUILhCABDoQCC4QsQMQgwEQxwEQowIQCjoHCAAQgAQQCjoLCC4QsQMQxwEQrwFQAFiWF2DVH2gDcAB4AIABZ4gBuAOSAQM1LjGYAQCgAQE&sclient=gws-wiz'
driver = webdriver.Chrome(path)
driver.get(url)


#scraping and printing the name of the roadside assistance companies. Saved in a pandas dataframe

companylist = []
links = driver.find_elements_by_class_name('Z7Mseb')
for link in links:

    title = driver.find_element_by_css_selector(".dbg0pd").text
    
    print(title)

    dictionary = {
        'company name': title
    }

    companylist.append(dictionary)
df = pd.DataFrame(companylist)


# Generated token needed to create discord bot
TOKEN = 'OTY2NTQzMDMzNjQ4NjkzMjg4.YmDRWA.LXIgoIjTMjN1AMO5a6NWx3qdVj0'


#client connection to Discord API
client = discord.Client()


#Lets user know when discord bot is activated
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))
    

#Recognizes and prints the user message in the output box as well as from what channel it was sent
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return


#Simulates a loop where the bot responds according to certain circumstances. Could only be achieved in a created discord channel 'bot-test'
    if message.channel.name =='bot-test':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
#Sending 'jumpstart' or 'oil change' will retrieve youtube videos to assist with those tasks. 
            await message.channel.send('https://www.youtube.com/watch?v=iI1o2hNy2hE')
            return

        if user_message.lower() == 'oil change':
            await message.channel.send('https://www.youtube.com/watch?v=rYWcL76WMRg&t=11s')
            return

#Sending 'roadside' will retrieve local roadside assistance companies from the created pandas dataframe
        if user_message.lower() == 'jumpstart':
        if user_message.lower() == 'roadside':
            await message.channel.send(df)
            return


client.run(TOKEN)
