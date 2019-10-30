from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',#Storage adapters provide an interface that allows ChatterBot to connect to different storage technologies.
    trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('C:/Users/deepak/Desktop/chatbot/data/'):
        convData = open(r'C:/Users/deepak/Desktop/chatbot/data/' + file,encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)
        #print("Training completed")
    

setup()
