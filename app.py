from flask import Flask, render_template, request
import pickle as pk
import pandas as pd

app = Flask(__name__)

infile = open('model','rb')
model = pk.load(infile)
infile.close()

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def metier():
    
    L = []
    n_tokens_title = request.form["n_tokens_title"]
    L.append(n_tokens_title)
    n_tokens_content = request.form["n_tokens_content"]
    L.append(n_tokens_content)
    n_unique_tokens = request.form["n_unique_tokens"]
    L.append(n_unique_tokens)
    n_non_stop_unique_tokens = request.form["n_non_stop_unique_tokens"]
    L.append(n_non_stop_unique_tokens)
    num_hrefs = request.form["num_hrefs"]
    L.append(num_hrefs)
    num_self_hrefs = request.form["num_self_hrefs"]
    L.append(num_self_hrefs)
    num_imgs = request.form["num_imgs"]
    L.append(num_imgs)
    num_videos = request.form["num_videos"]
    L.append(num_videos)
    average_token_length = request.form["average_token_length"]
    L.append(average_token_length)

    data_channel = request.form.getlist("data_channel")
    print(data_channel)
    L.extend(data_channel)

    kw_min_min = request.form["kw_min_min"]
    L.append(kw_min_min)
    kw_max_min = request.form["kw_max_min"]
    L.append(kw_max_min)
    kw_avg_min = request.form["kw_avg_min"]
    L.append(kw_avg_min)
    kw_min_max = request.form["kw_min_max"]
    L.append(kw_min_max)
    kw_max_max = request.form["kw_max_max"]
    L.append(kw_max_max)
    kw_avg_max = request.form["kw_avg_max"]
    L.append(kw_avg_max)
    kw_min_avg = request.form["kw_min_avg"]
    L.append(kw_min_avg)
    kw_max_avg = request.form["kw_max_avg"]
    L.append(kw_max_avg)
    kw_avg_avg = request.form["kw_avg_avg"]
    L.append(kw_avg_avg)
    self_reference_min_shares = request.form["self_reference_min_shares"]
    L.append(self_reference_min_shares)
    self_reference_max_shares = request.form["self_reference_max_shares"]
    L.append(self_reference_max_shares)
    self_reference_avg_sharess = request.form["self_reference_avg_sharess"]
    L.append(self_reference_avg_sharess)

    weekday = request.form.getlist("weekday")
    L.extend(weekday)

    LDA_00 = request.form["LDA_00"]
    L.append(LDA_00)
    LDA_01 = request.form["LDA_01"]
    L.append(LDA_01)
    LDA_02 = request.form["LDA_02"]
    L.append(LDA_02)
    LDA_03 = request.form["LDA_03"]
    L.append(LDA_03)
    LDA_04 = request.form["LDA_04"]
    L.append(LDA_04)
    global_subjectivity = request.form["global_subjectivity"]
    L.append(global_subjectivity)
    global_sentiment_polarity = request.form["global_sentiment_polarity"]
    L.append(global_sentiment_polarity)
    global_rate_positive_words = request.form["global_rate_positive_words"]
    L.append(global_rate_positive_words)
    global_rate_negative_words = request.form["global_rate_negative_words"]
    L.append(global_rate_negative_words)
    rate_positive_words = request.form["rate_positive_words"]
    L.append(rate_positive_words)
    rate_negative_words = request.form["rate_negative_words"]
    L.append(rate_negative_words)
    avg_positive_polarity = request.form["avg_positive_polarity"]
    L.append(avg_positive_polarity)
    min_positive_polarity = request.form["min_positive_polarity"]
    L.append(min_positive_polarity)
    max_positive_polarity = request.form["max_positive_polarity"]
    L.append(max_positive_polarity)
    avg_negative_polarity = request.form["avg_negative_polarity"]
    L.append(avg_negative_polarity)
    min_negative_polarity = request.form["min_negative_polarity"]
    L.append(min_negative_polarity)
    max_negative_polarity = request.form["max_negative_polarity"]
    L.append(max_negative_polarity)
    title_subjectivity = request.form["title_subjectivity"]
    L.append(title_subjectivity)
    title_sentiment_polarity = request.form["title_sentiment_polarity"]
    L.append(title_sentiment_polarity)
    abs_title_subjectivity = request.form["abs_title_subjectivity"]
    L.append(abs_title_subjectivity)
    abs_title_sentiment_polarity = request.form["abs_title_sentiment_polarity"]
    L.append(abs_title_sentiment_polarity)
    print(len(L))

    liste = ['n_tokens_title', 'n_tokens_content', 'n_unique_tokens',
       'n_non_stop_unique_tokens', 'num_hrefs', 'num_self_hrefs', 'num_imgs',
       'num_videos', 'average_token_length', 'num_keywords',
       'data_channel_is_entertainment', 'data_channel_is_socmed',
       'data_channel_is_tech', 'data_channel_is_world', 'kw_min_min',
       'kw_max_min', 'kw_avg_min', 'kw_min_max', 'kw_max_max', 'kw_avg_max',
       'kw_min_avg', 'kw_max_avg', 'kw_avg_avg', 'self_reference_min_shares',
       'self_reference_max_shares', 'self_reference_avg_sharess',
       'weekday_is_monday', 'weekday_is_tuesday', 'weekday_is_wednesday',
       'weekday_is_thursday', 'weekday_is_friday', 'weekday_is_saturday',
       'weekday_is_sunday', 'is_weekend', 'LDA_00', 'LDA_01', 'LDA_02',
       'LDA_03', 'LDA_04', 'global_subjectivity', 'global_sentiment_polarity',
       'global_rate_positive_words', 'global_rate_negative_words',
       'rate_positive_words', 'rate_negative_words', 'avg_positive_polarity',
       'min_positive_polarity', 'max_positive_polarity',
       'avg_negative_polarity', 'min_negative_polarity',
       'max_negative_polarity', 'title_subjectivity',
       'title_sentiment_polarity', 'abs_title_subjectivity',
       'abs_title_sentiment_polarity']

    futur_dict = []
    for i in range(len(L)):
    	list_tmp = []
    	list_tmp.append(L[i])
    	futur_dict.append(list_tmp)
    tmp = dict(zip(liste,futur_dict))

    data = pd.DataFrame.from_dict(tmp)
    result = model.predict(data)
    if result == True:
    	return "Votre article va buzzer ! ;)"
    else: 
    	return "Votre Article va Bidder ! XD"



if __name__ == "__main__":
    app.run(debug=True)