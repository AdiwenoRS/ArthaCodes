from nltk.chat.util import Chat, reflections

pairs = [

    [

        r"my name is (.*)",

        ["Hello %1, How are you today ?",]

    ],

    ]

def MyChatbot_test():

    print("Hi, I am your chatbot.")

    chatbot=Chat(pairs, reflections)

    chatbot.converse()

    if __name__ == '__main__':

        MyChatbot_test()