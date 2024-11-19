import pickle
# we are using Flask micro web framework
from flask import Flask, request # request always refers to the current request object

app = Flask(__name__)

def load_model():
    # unpickle header and tree in tree..p
    infile = open("tree.p", "rb")
    header, tree = pickle.load
    infile.close()
    return header, tree

def tdidt_predict(header, tree, instance):
    info_type = tree[0]
    if info_type == "Leaf":
        return tree[1] # label
    att_index = header.index(tree[1])
    for i in range(2, len(tree)):
        value_list = tree[i]
        if value_list[1] == instance[att_index]:
            return tdidt_predict(header, value_list[2], instance)
        
# we need to add some routes
# route is function that handles request
# maybe for JSON response for a /predict API endpoint
@app.route("/")
def index():
    # return context and status code
    return "<h1>Welvome to the interview predictor app</h1>", 200

# lets add a route for the /predict endpoint
@app.route("/predict")
def predict():
    # lets parse the unseen instance values from the query string
    # they are in the request object
    level = request.args.get("level") # defaults to None if arg is omitted
    lang = request.args.get("lang")
    tweets = request.args.get("tweets")
    phd = request.args.get("phd")
    instance = [level, lang, tweets, phd]
    header, tree = load_model()
    # lets make a prediction
    pred = tdidt_predict(header, tree, instance)
    if pred is not None:
        return jsonify({"prediction": pred}), 200
    # something went wrong
    return "Error making a predictin", 400

if __name__ == "__main__":
    # header, tree = load_model()
    # print(header)
    # print(tree)
    app.run(host="0.0.0.0", port=5001, debug=False) # port may be 5000 (should run in vscode still)
    # TODO when deploy app to "production", set debug=False
    # add check host and port values