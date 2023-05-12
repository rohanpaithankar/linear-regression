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
	def get(self,batch_input):
		try:
			batch_lst = batch_input.strip('][').split(',')
			lst = [eval(i) for i in batch_lst]
			lst = np.array(lst).reshape(len(lst),1)
			lst = lst.tolist()
			lr = pickle.load(open('model/lr_model.pkl','rb'))
			prediction = lr.predict(lst)
			prediction = prediction.tolist()
			result = {'Predictions': prediction}
			data.append(result)
			return result
		except Exception as e:
			return "Invalid input. Pass an argument like this - URL/stream/[1.0,0.5,0.6,..]"

class predict_stream(Resource):
	def get(self,stream_input):
		try:
			stream = [eval(stream_input)]
			lr = pickle.load(open('model/lr_model.pkl','rb'))
			prediction = lr.predict(stream)
			prediction = prediction.tolist()
			result = {'Prediction': prediction}
			data.append(result)
			return result
		except Exception as e:
			return "Invalid input. Pass an argument like this - URL/stream/0.5"

#api.add_resource(predict_stream, '/')
api.add_resource(predict_batch, '/batch/<batch_input>')
api.add_resource(predict_stream, '/stream/<stream_input>')

if __name__ == '__main__':
    X_train, y_train, X_test, y_test = generate_data()
    model = SimpleLinearRegression()
    model.fit(X_train,y_train)
    predicted = model.predict(X_test)
    pickle.dump(model, open('model/lr_model.pkl','wb'))
    print("Random Forest Model Saved")
    app.run(debug=True)
