from app import app

if __name__ == '__main__':
   #socketio.run(app =app,host='127.0.0.1',port=5500, debug=True)
   app.run(host='0.0.0.0',port=3000,debug = True)
