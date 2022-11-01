import pandas as pd
import gensim
import numpy as np
import tqdm
import gzip

# モデルの読み込み
model_name = 'model.gz'
# model = gensim.models.KeyedVectors.load_word2vec_format(model_name, binary=False)
model = gensim.models.KeyedVectors.load_word2vec_format(model_name,binary=False)

def sorayomi(atmo,input_length,a): #明るさ,長さ,単語
    def analyze(df):
        df = df.sort_values(by='length', ascending=False)    
    
        if input_length == 'ながめ':
            df = df.head(int(len(df)//3))

        if input_length == 'ふつう':
            df = df[(int(len(df)//3)):(int(len(df)//3*2))]

        if input_length == 'みじかめ':
            df = df.tail(int(len(df)//3))
        point_score= []

        for w,t,l in tqdm.tqdm(zip(df['words'], df['title'], df['length']),total=len(df),leave=False):
            point = 0
            words = str(w).split(',')
            count = 0

            for b in words:
                try:
                    c = model.similarity(a, b)
                    c = round(c,3)
                    point += c
                    count += 1
                    if a in b:
                        point += 15
                    
                except KeyError:
                    pass

            point = point/count

            if a in t:
                point += 15

            point_score.append(point)

        df['point'] = point_score

        df = df.sort_values(by='point', ascending=False)
        df = df.head(10)

        return(df)

    if 0 <= atmo <= 10:
        usecols = ['title','author','length','words']
        df = pd.read_csv('./static/dataframe/df_10.csv', usecols=usecols)
        df = analyze(df)
        author = df.iloc[0]['author']
        title = df.iloc[0]['title']
        other = df[1:]

    elif 10 < atmo <= 20:
        usecols = ['title','author','length','words']
        df = pd.read_csv('./static/dataframe/df_20.csv', usecols=usecols)
        df = analyze(df)
        author = df.iloc[0]['author']
        title = df.iloc[0]['title']
        other = df[1:]

    # ややあかるめ
    elif 20 < atmo <= 30:
        usecols = ['title','author','length','words']
        df = pd.read_csv('./static/dataframe/df_30.csv', usecols=usecols)
        df = analyze(df)
        author = df.iloc[0]['author']
        title = df.iloc[0]['title']
        other = df[1:]

    elif 30 < atmo <= 40:
        usecols = ['title','author','length','words']
        df = pd.read_csv('./static/dataframe/df_40.csv', usecols=usecols)
        df = analyze(df)
        author = df.iloc[0]['author']
        title = df.iloc[0]['title']
        other = df[1:]


    elif 40 < atmo <= 50:
        usecols = ['title','author','length','words']
        df = pd.read_csv('./static/dataframe/df_50.csv', usecols=usecols)
        df = analyze(df)
        author = df.iloc[0]['author']
        title = df.iloc[0]['title']
        other = df[1:]


    elif 50 < atmo <= 60:
        usecols = ['title','author','length','words']
        df = pd.read_csv('./static/dataframe/df_60.csv', usecols=usecols)
        df = analyze(df)
        author = df.iloc[0]['author']
        title = df.iloc[0]['title']
        other = df[1:]

    
    elif 60 < atmo <= 70:
        usecols = ['title','author','length','words']
        df = pd.read_csv('./static/dataframe/df_70.csv', usecols=usecols)
        df = analyze(df)
        author = df.iloc[0]['author']
        title = df.iloc[0]['title']
        other = df[1:]

    elif 70 < atmo <= 80:
        usecols = ['title','author','length','words']
        df = pd.read_csv('./static/dataframe/df_80.csv', usecols=usecols)
        df = analyze(df)
        author = df.iloc[0]['author']
        title = df.iloc[0]['title']
        other = df[1:]

    elif 80 < atmo <= 90:
        usecols = ['title','author','length','words']
        df = pd.read_csv('./static/dataframe/df_90.csv', usecols=usecols)
        df = analyze(df)
        author = df.iloc[0]['author']
        title = df.iloc[0]['title']
        other = df[1:]


    elif 90 < atmo <= 100:
        usecols = ['title','author','length','words']
        df = pd.read_csv('./static/dataframe/df_90.csv', usecols=usecols)
        df = analyze(df)
        author = df.iloc[0]['author']
        title = df.iloc[0]['title']
        other = df[1:]

    return(author,title,other)

