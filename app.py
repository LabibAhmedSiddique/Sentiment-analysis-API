from flask import Flask, request, jsonify,render_template
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

def sentiment_analysis(text):
    model_name = "distilbert-base-uncased"
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)#tokanize text input to feed compitable data to model
                                                                
    sentiment_classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)#pipeline to take
                                                                                           #model and tokenizer to perform classification easily
    result = sentiment_classifier(text)
    label = result[0]['label']#strip only the label
    label_mapping = {'LABEL_0': 'negative', 'LABEL_1': 'positive', 'LABEL_2': 'neutral'}
    label = label_mapping[label]#maps labels to result and return sentiment 
    return label

app = Flask(__name__)

@app.route('/analyze', methods=['POST','GET'])
def analyze_sentiment():
    if request.method == 'POST':
        try:
            data = request.get_json()#perse incoming requst as json
            text = data['text']
            
            sentiment = sentiment_analysis(text)
            
            response = {'sentiment': sentiment}
            return jsonify(response)
        
        except KeyError:
            error = {'error': 'Invalid request payload'}
            return jsonify(error), 400 #handle bad request
        
        except Exception as e:
            error = {'error': str(e)}
            return jsonify(error), 500 #handle internal server error 
    else:
        return render_template('index.html', text='')#made an extra modifiation to the requirments and made 
                                                    #the frontend    


if __name__ == '__main__':
    app.run(debug=True)