from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://dbuser:dbpass@cluster0.jrbed.mongodb.net/?retryWrites=true&w=majority")
db = cluster["shop"]
users = db["users"]
orders = db["orders"]

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")[-10:]
    res = MessagingResponse()
    user = users.find_one({"number": number})
    if bool(user) == False:
        msg = res.message(
            " माझ्याबद्दल माहिती: हाय मी टिटू आहे मी रुजुलने बनवलेला बॉट आहे तुमच्या आवडत्या राजकारणी अजित अनंतराव पवार"
            " यांच्याबद्दल जाणून घेण्यासाठी ज्यांना (दादा) असेही म्हणतात.\n\n दाबा \n\n 1 अजित दादांबद्दल जाणून घेण्यासाठी \n 2 त्यांच्या ताज्या बातम्या "
            "जाणून घेण्यासाठी \n 3 त्यांच्या भविष्यातील योजना जाणून घेण्यासाठी \n 4 त्यांच्याशी संपर्क साधण्यासाठी \n 5 त्यांचे नवीनतम भाषण जाणून घेण्यासाठीत्यांचे नवीनतम भाषण जाणून घेण्यासाठी")
        msg.media("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0k3Ewoc9ZmhsMVbXU-3NLBmmxeDievuNBJg&usqp=CAU")
        users.insert_one({"number": number, "status": "main", "messages": []})
    elif user["status"] == "main":
        try:
            option = int(text)
        except:
            msg = res.message(
                "माझ्याबद्दल माहिती: हाय मी टिटू आहे मी रुजुलने बनवलेला बॉट आहे तुमच्या आवडत्या राजकारणी अजित अनंतराव पवार"
                " यांच्याबद्दल जाणून घेण्यासाठी ज्यांना (दादा) असेही म्हणतात.\n\n दाबा \n\n 1 अजित दादांबद्दल जाणून घेण्यासाठी \n2 त्यांच्या ताज्या बातम्या "
                "जाणून घेण्यासाठी \n 3 त्यांच्या भविष्यातील योजना जाणून घेण्यासाठी  \n 4 त्यांच्याशी संपर्क साधण्यासाठी \n 5 त्यांचे नवीनतम भाषण जाणून घेण्यासाठी")
            msg.media("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0k3Ewoc9ZmhsMVbXU-3NLBmmxeDievuNBJg&usqp=CAU")
            return str(res)
        if option == 1:
            msg = res.message("https://ajitpawar.org/en/biography/")
            msg.media("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZOARtwN8NlPNaXAeLUFU76-9swdz6AbfDbA&usqp=CAU")
        elif option == 2:
            msg1 = res.message("https://ajitpawar.org/en/latest-news/")
            msg1.media("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZOARtwN8NlPNaXAeLUFU76-9swdz6AbfDbA&usqp=CAU")
        elif option == 3:
            msg3 = res.message("https://www.livemint.com/news/maharashtra-to-set-up-hostel-for-students-of-all-communities-in-mumbai-ajit-pawar-11650800790961.html")
            msg3.media("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZOARtwN8NlPNaXAeLUFU76-9swdz6AbfDbA&usqp=CAU")
        elif option == 4:
            msg4 = res.message("https://ajitpawar.org/connect-with-us-mr/")
            msg4.media("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZOARtwN8NlPNaXAeLUFU76-9swdz6AbfDbA&usqp=CAU")
        elif option == 5:
            msg2 = res.message("https://ajitpawar.org/latest-speeches-mr/")
            msg2.media("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZOARtwN8NlPNaXAeLUFU76-9swdz6AbfDbA&usqp=CAU")
        else:
            users.update_one({"number": number}, {"$set": {"status": "main"}})
            res.message("तुम्ही खालीलपैकी एक पर्याय निवडू शकता: \n\n दाबा \n\n  1 अजित दादांबद्दल जाणून घेण्यासाठी \n 2 त्यांच्या ताज्या बातम्या जाणून"
                        "घेण्यासाठी \n 3 त्यांच्या भविष्यातील योजना जाणून घेण्यासाठी \n 4 त्यांच्याशी संपर्क साधण्यासाठी \n 5 त्यांचे नवीनतम भाषण जाणून घेण्यासाठीत्यांचे नवीनतम भाषण जाणून घेण्यासाठी")
        return str(res)


if __name__ == "__main__":
    app.run()
