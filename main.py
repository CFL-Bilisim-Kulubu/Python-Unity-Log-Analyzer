from distutils.log import error
import os
from urllib import response
import openai

def readfile(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except Exception as e:
        print("Error : " + str(e))
        input("waiting for input to quit program")
        exit()

def getKey():
    try:
        openai.api_key = readfile("key.txt")
        print("\n Sucsesfully connected to OpenAI API\n\n==========================\n")
    except Exception as e:
        print("Error: API key not found etc.")
        print("\nDetailed Exception :" + str(e) + "\n")
        input("waiting for input to quit program")
        exit()
    

def try_variations(x: str):

    print("\n\n==========================\n")

    variation = [f"Search Online for :\n\n{x}",
    f"Lookup Unity Forums and API Reference for : \n{x}\n1 if you find it leave the pages link",
    f"Lookup Unity Forums and API Reference for : \n{x}\n and explain it to me or leave the pages link",
    f"Lookup Unity Forums and API Reference for : \n{x}\n and explain it to me in a short sentence or leave the pages link",
    f"Lookup Unity Forums and API Reference for : \n{x}\n explain how to fix it or leave the pages link",
    f"Lookup Unity Forums and API Reference for : \n{x}\n explain why does it occurs or leave the pages link",
    f"Explain \n{x}\n to me",
    f"Explain \n{x}\n to me in a short sentence",
    f"How to deal with this problem:\n{x}",
    f"What is the problem with \n{x}",
    f"What is the reason of \n{x}",
    f"why \n{x}\nhappens? what is the reasons or possibilities?"
    ]

    for i in variation:
        print("\nSentence : " + i)
    
    for i in range(0, len(variation)):
        print(f"\nResponse{i} : " + gpt3("You are a bot that reads and analyzes log files, analyze this file\n" + variation[i]))

    myInput = input(
'''
        ====>  Press 1 to return menu
        ====>  Press anykey to quit
    '''
    )
    if myInput == "1":
        program_loop()
    else:
        exit()
        
def gpt3(x):
    try:
        
        response = openai.Completion.create(
            engine ="text-davinci-002",
            prompt = x,
            temperature = 0.5,
            max_tokens = 100,)
        return response.choices[0].text
    except Exception as e:
        return "Error  :" + x

def program_loop():
    myInput = input(
        '''
        ====>  Press 1 to read a log file to analyze
        ====>  Press anykey to quit
    ''')
    if myInput == '1':
        myInput = input("paste file name here: ")
        try_variations(readfile(myInput))

if __name__ == '__main__':
    getKey()
    program_loop()