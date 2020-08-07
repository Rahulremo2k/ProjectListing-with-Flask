from cs50 import SQL
from flask import Flask,render_template,request,redirect


app=Flask(__name__)

db=SQL("sqlite:///data.db")

@app.route("/")
def index():
    t = db.execute("SELECT * FROM Project")
    return render_template("index.html",t=t,n=len(t))
    
    
@app.route('/add/',methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        name = request.form.get("name")
        des= request.form.get("des")
        url = request.form.get("url")
        db.execute("INSERT INTO Project (name,des,url) VALUES(:name,:des,:url)",name=name,des=des,url=url)
        return redirect("/")
        
        
@app.route('/delete/<name>/<des>',methods=["GET","POST"])
def delete(name,des):
    db.execute("DELETE FROM Project WHERE name=? AND des=?",name,des)
    return redirect("/")
    
    
@app.route('/delall')
def delall():
    db.execute("DELETE FROM Project")
    return redirect("/")
    
@app.route('/edit/<name>/<des>/<path:url>',methods=["GET","POST"])
def edit(name,des,url):
    if request.method == "GET":
        return render_template("edit.html",name=name,des=des,url=url)
    else:
        uname = request.form.get("name")
        udes = request.form.get("des")
        uurl = request.form.get("url")
        db.execute("update Project set name=? , des=? , url=? WHERE name=? AND des=?",uname,udes,uurl,name,des)
        return redirect("/")