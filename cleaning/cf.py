import pandas as pd
import re
import emoji


seed_emotions = {'#thankful','#feelinggood','#blessed','#happy','#estatic','#goodmood','#yay',
            '#worstfear','#fear','#frightened','#horror','#dismay','#anxious','#afraid', 
            '#depressed','#foreveralone','#heartbroken','#leftout','#disappointed',
            '#angry','#mad','#pissed','#furious','#hate','#angrytweet' }

stop_words = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once','don', 'via', 've', 
              'during', 'out', 'very', 'having','like', 'with', 'they', 'own', 'an', 'be', 'some',
              'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 
              'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 
              'until', 'below', 'are', 'we',  'got', 'get', 'going','these', 'your', 'his', 'through', 
              'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 
              'even','know','their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 
              'no', 'when', 'at', 'any', 'before', 'them', 'time','day','see','people','time','today',
              'never','make','time','life','last','way','think','good','same', 'and', 'been', 'have', 
              'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 
              'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 
              'too', 'only', 'myself', 'which', 'would','still', 'one', 'new','those', 'i', 'after', 'few', 
              'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 
              'further', 'm','ll','o','re','ve', 'was', 'here', 'than'}
    
    

def extract_emojis(s):   
    return [c for c in s if c in emoji.UNICODE_EMOJI]


def remove_specific_links(text):
    return ' '.join(word for word in text.split() if 
                    (
                       word[0]!='@'
                       and word not in seed_emotions 
#                        and word not in stop_words
#                        and len(word) > 2
                       and not word.isdigit()
                       and not word.startswith('pic.twitter.')
                    )).lower()


def remove_pic_urls(text):
    return ' '.join(word for word in text.split() if word[0]!='#')

def remove_urls(text):
    
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split())
  


def remove_punctuation(text):
    text = text.translate(str.maketrans('','','(){}<>.,?:!)'))
    
    return text

def tokenize_sentence(text):
    tokText = word_tokenize(text.lower()) 
    
    return tokText

def remove_stopwords(tokText):
    

    
    return list(set(tokText) - stop_words)


def  add_emojis(x):    
    
    a =' '.join([re.sub('[^a-zA-Z0-9 \n\.]', '', str( x.encode("UTF-8")))  for x in  x['emoji']])
    
    return x['tweet'] + a

def  remove_hashtags(x):    
    text = x.tweet.lower()
    
    for hashtag in ast.literal_eval(x.hashtags):
        
        text = text.replace(hashtag.lower(),'')
        
    return text

    


def clean_tweet(text):
    
    text = remove_specific_links(text)

    text = remove_urls(text)
    
    text =  remove_punctuation(text)

    text = tokenize_sentence(text)

    text = remove_stopwords(text)

    return text


contraction_dict = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not", "didn't": "did not",  "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not", "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",  "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would", "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would", "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is", "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as", "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would", "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",  "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have","you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have"}

def _get_contractions(contraction_dict):
    contraction_re = re.compile('(%s)' % '|'.join(contraction_dict.keys()))
    return contraction_dict, contraction_re
contractions, contractions_re = _get_contractions(contraction_dict)

def replace_contractions(text):
    def replace(match):
        return contractions[match.group(0)]
    return contractions_re.sub(replace, text)
