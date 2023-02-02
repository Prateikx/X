from flask import Flask,render_template,request
import pymysql
from flask_bootstrap import Bootstrap
connection=pymysql.connect(host="localhost",user="root",password="admin",db="Bignalytics") 



app=Flask(__name__)
b=Bootstrap=Bootstrap(app)
# @app.route('/',method=['GET'])
# def index():
#     return "welcome"

@app.route('/')  # we declarre route to ease for end user
def home():
    
    return "WELCCOME TO FLASK"
@app.route("/form")
def form():
    print(request.args)
    sql="insert into flask values(%s ,%s)"
    connection.cursor().execute(sql,(request.args.get('lname'),request.args.get('fname')))
    connection.commit()
    person={"lname":request.args.get("lname"),"fname":request.args.get("fname")}
    print(person)
    return render_template('index.html')

@app.route("/sendui") 
def sendui():
    sql="select * from flask " #sendui
    with connection.cursor() as cursor:
        cursor.execute(sql)
                                                   
    data=cursor.fetchall()
    print(data)
    
    
    return render_template('sendui.html',customer_orders=data)


if __name__ =='__main__':
    
   
    app.run(debug=True)
    