# Matrix PDF Bot
a matrix bot for grabbing pdfs files from matrix rooms and spaces, 
this functionality could be expanded to work with matrix based 
applications such as populous in order to download and use the pdf for
other purposes

## Setup
    
    1. clone this code from git hub
    2. install requirements
    3. create a matrix account for your bot 
       https://app.element.io/?pk_vid=1653610330189fc0#/register
       and put the username and password in the configuration.yaml
       under the matrix connector here:

    mxid: "@rick_deck2049:matrix.org"
    password: "replicant2049"

    4. pick a room for your matrix bot to go in put the bot
       in and paste the room code in the configuation.yaml file
       under the matrix connector here:

    rooms:
      main: {#my-room:matrix.org}

    5. run the bot using 'opsdroid start' in the terminal

##Use

to grab a pdf from a room you'll need the internal room id. you can find this in settings > advanced > internal room id
once you got this code, just paste it in chat in the room that the bot is in and it will 
grab the pdf and respond with a download link

