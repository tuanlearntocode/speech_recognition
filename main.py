from processor import Processor

P = Processor()
P.text = 'Hello sir!\nWhat can I do for you? \nI\'m listening...'
while True:
    print(P.text)
    P.speaking()
    hear = P.listening()
    if hear == 'what time is it':
        P.mytime()
        P.speaking()

    elif hear == 'what is the date today':
        P.myday()
        P.speaking()

    elif 'bye' in hear:
        P.text = 'Goodbye sir!'
        P.speaking()
        break

    P.text = 'Anything else I can do for you?'
print('You\'re good to go')
