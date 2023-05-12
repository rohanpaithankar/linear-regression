from flask import Flask
from flask_restful import Api, Resource 
import numpy as np 
import pickle  
from model.simple_linear_regr import SimpleLinearRegression
from model.simple_linear_regr_utils import generate_data

app = Flask(__name__)
api = Api(app)
data = []

class predict_batch(Resource):
	def get(self,lst):
		try:
			lst_num = lst.strip('][').split(',')
			lst_int = [eval(i) for i in lst_num]
			lst_int = np.array(lst_int).reshape(len(lst_num),1)
			lst_int = lst_int.tolist()
			lr = pickle.load(open('model/lr_model.pkl','rb'))
			prediction = lr.predict(lst_int)
			prediction = prediction.tolist()
			temp = {'Predictions': prediction}
			data.append(temp)
			return temp
		except Exception as e:
			return str(e)# "Invalid input. Pass a float argument like this - URL/stream/[1.0,0.5,0.6,..]"

class predict_stream(Resource):
	def get(self,stream_input):
		try:
			input_int = [eval(stream_input)]
			lr = pickle.load(open('model/lr_model.pkl','rb'))
			prediction = lr.predict(input_int)
			prediction = prediction.tolist()
			temp = {'Prediction': prediction}
			data.append(temp)
			return temp
		except Exception as e:
			return str(e)#"Invalid input. Pass a float argument like this - URL/stream/0.5"

#api.add_resource(predict_stream, '/')
api.add_resource(predict_batch, '/batch/<lst>')
api.add_resource(predict_stream, '/stream/<stream_input>')

if __name__ == '__main__':
    X_train, y_train, X_test, y_test = generate_data()
    model = SimpleLinearRegression()
    model.fit(X_train,y_train)
    predicted = model.predict(X_test)
    pickle.dump(model, open('model/lr_model.pkl','wb'))
    print("Random Forest Model Saved")
    app.run(debug=True)