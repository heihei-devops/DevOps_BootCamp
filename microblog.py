# from flask import Flask, request, render_template
# from config import Config
# import random
# app = Flask(__name__)
# app.config.from_object(Config)

# from app import routes

# def factors(num):
#   return [x for x in range(1, num+1) if num%x==0]

# @app.route('/')
# def index():
#     return render_template('form.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     return 'You entered: {}'.format(request.form['text'])



from app import app






# @app.route('/')
# def home():
#   n = random.randint(2, 10000)
#   return render_template(
#     # name of template
#     "index.html",
#     # now we pass in our variables into the template
#     random_num=n, 
#   )


# @app.route('/test')
# def testing():
#     return 'You made it to the main testing route!'

# @app.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello '+ name + '!'

# @app.route('/factors/<int:n>')
# def factors_display(n):
# 	return render_template(
# 		"factors.html",  # name of template
# 		number=n,  # value for `number` in template
# 		factors=factors(n) # value for `factors` in template
# 	)
	

# if __name__ == '__main__':
#   app.run(debug=True, host='0.0.0.0')