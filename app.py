from flask import Flask, jsonify, request

from query import answer_query

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Q&A service!'

@app.route('/answer', methods=['POST'])
def get_answer():
    query = request.json.get('query')
    
    response = answer_query(query)
    
    return jsonify({
        "response": f"{response}"
    })
    
if __name__ == '__main__':
    app.run()
