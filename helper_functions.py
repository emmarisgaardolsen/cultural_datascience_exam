import re
from nltk.tokenize import word_tokenize
import nltk
from wordcloud import WordCloud
nltk.download('punkt')
import seaborn as sns

#stop_words = stopwords.words('english')


def opentxtfile(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        transcripts= ''.join(lines)

    return transcripts


# function for cleaning text including removing punctuations
def func_cleaning_transcripts(speech):
    transcripts = re.sub(r'\W', ' ', speech) # non word characters
    transcripts = re.sub(r'\*', '', transcripts) #  remove astrisk
    transcripts = transcripts.lower() # lower case
    transcripts = re.sub(r'\s+', ' ', transcripts) # remove repeated spaces
    transcripts = transcripts.replace('\n', ' ') # remove line breaks
    
    return transcripts


def remove_stopwords(transcripts):
    with open("stopord.txt", 'r') as f_object:
        stop_words = f_object.read().split()
    tokenized_transcripts=word_tokenize(transcripts)
    transcripts_wo_stopwords= [w for w in tokenized_transcripts if not w in stop_words] 
    transcripts_wo_stopwords=' '.join(transcripts_wo_stopwords)    
    return transcripts_wo_stopwords


def plot_word_counts(df, n):
    import matplotlib.pyplot as plt
    # Get the top n most frequent words
    top_n = df['transcripts'].str.split(expand=True).stack().value_counts().sort_values(ascending=False).head(n)
    # Plot a bar chart of the top n most frequent words
    sns.barplot(x=top_n.values, y=top_n.index)
    plt.title("Most Frequent Words")
    plt.xlabel("Number of Occurrences")
    plt.ylabel("Word")
    plt.show()

    # Print the top n most frequent words
    print(top_n)


import matplotlib.pyplot as plt

def double_plot_word_counts(df1, df2, n):
    # Create a figure with two subplots
    plt.figure(figsize=(10, 6))

    # Plot the first DataFrame in the first subplot
    plt.subplot(1, 2, 1)
    top_n1 = df1['transcripts'].str.split(expand=True).stack().value_counts().sort_values(ascending=False).head(n)
    sns.barplot(x=top_n1.values, y=top_n1.index)
    plt.title("Most Frequent Words - " + df1.name)
    plt.xlabel("Number of Occurrences")
    plt.ylabel("Word")

    # Plot the second DataFrame in the second subplot
    plt.subplot(1, 2, 2)
    top_n2 = df2['transcripts'].str.split(expand=True).stack().value_counts().sort_values(ascending=False).head(n)
    sns.barplot(x=top_n2.values, y=top_n2.index)
    plt.title("Most Frequent Words - " + df2.name)
    plt.xlabel("Number of Occurrences")
    plt.ylabel("Word")

    # Show the figure
    plt.show()


def word_cloud(name,transcript,color_map,x):
    import matplotlib.pyplot as plt
    with open("stopord.txt", 'r') as f_object:
        stop_words = f_object.read().split()
    wc = WordCloud(stopwords=stop_words, width = 300, height = 250,background_color="white", colormap=color_map,max_font_size=75, random_state=60)
    plt.rcParams['figure.figsize'] = [x,x]
    wc.generate(transcript)
    plt.subplot(3,4,3)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(name)
    plt.show()

def lix_score(text):
  # Split the text into a list of words
  words = text.split()
  
  # Count the number of words in the text
  num_words = len(words)
  
  # Count the number of long words in the text
  num_long_words = 0
  for word in words:
    if len(word) > 6:
      num_long_words += 1
  
  # Count the number of sentences in the text
  num_sentences = text.count('.')
  
  # Calculate the Lix score
  lix = (num_words / num_sentences) + (num_long_words * 100) / num_words
  
  # Return the Lix score
  return lix