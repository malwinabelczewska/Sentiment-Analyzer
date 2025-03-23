from textblob import TextBlob
import gradio as gr

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity=blob.sentiment.polarity

    if polarity >0:
        return "😊 Positive"
    elif polarity <0:
        return "☹️ Negative"
    else:
        return "😐 Neutral"

interface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(label="Enter a word or sentence"),
    outputs=gr.Textbox(label="Sentiment"),
    title="ML-Based Sentiment Analyzer",
    description="Now powered by a real model! Type any word or sentence to get the sentiment."
)

interface.launch()