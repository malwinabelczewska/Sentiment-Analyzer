from textblob import TextBlob
import gradio as gr

# Keeps the last 10 visitor inputs
history = []

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "😊 Positive"
        color = "#d4edda"
    elif polarity < 0:
        sentiment = "☹️ Negative"
        color = "#f8d7da"
    else:
        sentiment = "😐 Neutral"
        color = "#fff3cd"

    score_str = f"{polarity:.2f}"
    result_html = f"""
        <div style="padding: 1em; background-color: {color}; border-radius: 10px;">
            <h2>{sentiment}</h2>
            <p><strong>Polarity score:</strong> {score_str}</p>
        </div>
    """

    # Add to history (max 10 items)
    history.append((text, sentiment, score_str))
    if len(history) > 10:
        history.pop(0)

    # Build HTML for history
    history_html = "<ul>"
    for word, sentiment, score in reversed(history):
        history_html += f"<li>{word} → {sentiment} (score: {score})</li>"
    history_html += "</ul>"

    return result_html, history_html

# Gradio interface
interface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(label="Enter a word or sentence"),
    outputs=[
        gr.HTML(label="Sentiment Analysis"),
        gr.HTML(label="Previous Inputs")
    ],
    title="ML-Based Sentiment Analyzer",
    description="Now powered by a real model! Type any word or sentence to get the sentiment."
)

interface.launch()
