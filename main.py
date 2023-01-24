from flask import Flask,render_template,request as r,redirect
import pymysql as py

app = Flask('__name__')

@app.route('/')
def index():
    try:
        db = py.connect(host='localhost',user='root',password='Arunk2481@',database='IPL_History')
        cur=db.cursor()  
        query='select * from history'  
        cur.execute(query)
        data=cur.fetchall()
        return render_template('dashboard.html',d=data)
    
    except Exception as e:
        print('Error:',e)
    

@app.route('/create')
def create():
    return render_template('form.html')



#insert
@app.route('/store',methods=['POST'])
def store():
    t_n = r.form['tmn']
    cp = r.form['cpt']
    y = r.form['yr']
    h_r= r.form['hrg']
    st=r.form['sts']
    try:
        db=py.connect(host='localhost',user='root',password='Arunk2481@',database='IPL_History')
        cur=db.cursor()
        query="insert into history(Team_Name,Captain,Year,Highest_Run_Getter,Status)values('{}','{}',{},'{}','{}')".format(t_n,cp,y,h_r,st)
        cur.execute(query)
        db.commit()
        return redirect('/')
    except Exception as e:
        print('Error:',e)
    


# Delete 
@app.route('/delete/<rid>')
def delete(rid):
    try:
        db = py.connect(host='localhost',user='root',password='Arunk2481@',database='IPL_History')
        cur=db.cursor()
        query="delete from history where id='{}'".format(rid) # single record
        #query = "update task SET is_deleted='Y' where id='{}'".format(rid)
        cur.execute(query)
        db.commit()
        return redirect('/')
    except Exception as e:
        print('Error:',e)

# Edit
@app.route('/edit/<rid>')
def edit(rid):
    try:
        db = py.connect(host='localhost',user='root',password='Arunk2481@',database='IPL_History')
        cur=db.cursor()
        query="select * from history where id={}".format(rid) # single record
        cur.execute(query)
        data=cur.fetchall()
        return render_template('editform.html',data=data)
    except Exception as e:
        print('Error:',e)

# Update
@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    t_n = r.form['tmn']
    cp = r.form['cpt']
    y = r.form['yr']
    h_r =r.form['hrg']
    st = r.form['sts']
    try:
        db=py.connect(host='localhost',user='root',password='Arunk2481@',database='IPL_History')
        cu=db.cursor()
        query="update history SET Team_Name='{}',Captain='{}',Year='{}',Highest_Run_Getter='{}',Status='{}' WHERE id={}".format(t_n,cp,y,h_r,st,rid)
        cu.execute(query)
        db.commit()
        return redirect('/')
        
    except Exception as e:
        print("Error:",e)
        
        


# run server
app.run(debug=True)  # app==> object and run()==>method of Flask class.


















