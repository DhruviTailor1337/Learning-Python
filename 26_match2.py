msg = "sorrY"

match msg.lower():
    case "hi"|"hii"|"hello"|"hyy"|"hiee":
        print("hey there!")
    case "bye"|"see yaa"|"good bye":
        print("bye, see you soon!")
    case "thanks"|"thank you":
        print("you're welcome!")
    case "sorry"|"i am sorry":
        print("its okay!")
    case _ :
        print("i don't understand that")
