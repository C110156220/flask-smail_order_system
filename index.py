from flask import Flask , render_template  ,request , redirect , url_for
import func 
loadtimes = 0
app = Flask('__name__')
# https://predictivehacks.com/?all-tips=how-to-add-action-buttons-in-flask

@app.route('/index' , methods=['GET','POST'])
def startpage():
    global loadtimes
    data = []
    data.append(func.select('fdlist')) 
    if loadtimes == 0 :
        loadtimes+=1
        print(loadtimes)
        return render_template('index.html' , data = data  )
    else:
        print('else')
        if request.method == 'POST':


            if request.form.get('type') == 'meat':
                print('switch meat list')
                print(request.form.getlist('fdqty'))
                return what_type('meat')
            elif request.form.get('type') == 'veg':
                print('switch veg list')
                return what_type('veg')
            elif request.form.get('type') == 'other':
                print('switch other list')
                return what_type('other')
            elif request.form.get('type') == 'drink':
                print('switch drink list')
                return what_type('drink')


            if request.form.get('submit') == 'check':
                print('submit')
                order = request.form.get('car_res','nothing')
                print("--------------------\n%s\n-------------------------"%order)
                order = order.replace(' ','')
                
                return redirect(url_for('submit',order=order))
            else:
                return render_template('index.html' , data = data )

        elif request.method == 'GET':
            print('get')
            return render_template('index.html' , data = data )
        else:
            return render_template('index.html')

def what_type(type):
    data = []
    data.append(func.select('fdlist',type))
    return render_template('index.html',data = data)
    
    
@app.route('/submit/<order>' , methods=['POST','GET'])
def submit(order):
    if request.method == 'GET':
        return render_template('check.html',order=order)
    elif request.method == 'POST':
        if request.form.get('submit') == 'send':
            order = order.replace('=',':') ; order = order.replace(' ','')
            if func.insert('fdorder',order) == 1 :
                return 'success'
            else:
                return 'failed'
        elif request.form.get('submit') == 'back':
            return redirect(url_for('startpage'))
    else :
        return None
    
@app.route('/boss', methods=['GET','POST'])
def boss():
    if request.method == 'GET':
        return render_template('boss.html',data=None)
    else:
        if request.form.get('func') == 'search':
            data = func.select('fdorder','con')
            return render_template('boss.html',func = 'search',data=data)
        elif request.form.get('func') == 'con':
            data = func.select('fdlist','con')
            return render_template('boss.html',func = 'con',data=data)
        else:
            if request.form.get('done') != None:
                if func.delete('cus',int(request.form.get('done'))) == 1 :
                    data = func.select('fdorder','con')
                    return render_template('boss.html',func = 'search',data=data)

            elif request.form.get('chge') != None:
                data = func.select('fdlist','con',int(request.form.get('chge'))) 
                return  render_template('boss.html',func = 'chge',data=data)

            elif request.form.get('dele') != None:
                print(request.form.get('dele'))
                if func.delete('boss',int(request.form.get('dele'))) == 1 :
                    data = func.select('fdlist','con')
                    return render_template('boss.html',func = 'con',data=data)
           
            elif request.form.get('chgeit') != None:
                data = request.form.getlist('chgedata')
                if(func.update(data))==1:
                    data = func.select('fdlist','con')  
                    return render_template('boss.html',func = 'con',data=data)
                
            else:
                return('error')




if __name__ == '__main__':
    app.debug = True 
    app.run()
