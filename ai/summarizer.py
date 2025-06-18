from transformers import pipeline
import textwrap

# Load the summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_length=1024):
    # break long text into smaller chunks to fit model input
    return textwrap.wrap(text, max_length)

def summarize_text(text):
    chunks = chunk_text(text, max_length=1024)
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=200, min_length=50, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    return ' '.join(summaries)
