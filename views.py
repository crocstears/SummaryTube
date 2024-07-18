from django.http import HttpResponse
from django.shortcuts import render
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
# from transformers import pipeline
import os
import string
import re
from youtube_transcript_api import YouTubeTranscriptApi
import heapq
import bs4 as bs
import urllib.request
import re
import nltk
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def get_transcript(youtube_link):
    video_id = get_video_id(youtube_link)
    if video_id:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([t['text'] for t in transcript_list])
        
        # Remove punctuation
        transcript = transcript.translate(str.maketrans('', '', string.punctuation))
        
        # Remove extra spaces
        transcript = re.sub(r'\s+', ' ', transcript)
        
        # Define words to filter out
        filter_words = ['example', 'remove', 'words']
        
        # Remove filter words
        transcript = ' '.join([word for word in transcript.split() if word.lower() not in filter_words])
        
        return transcript.strip()  # Strip leading/trailing spaces
    
    return ""

os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
# summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def get_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    video_id = parse_qs(parsed_url.query).get('v')
    if video_id:
        return video_id[0]
    return None


def generate_summary(transcript):
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', transcript)
    article_text = re.sub(r'\s+', ' ', article_text)
    
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    
    return formatted_article_text

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    transcript=get_transcript(djtext)
    # print(transcript)
    summary=generate_summary(transcript)
    print(summary)
    par={'analyzed_text':summary}
    return render(request,'analyze.html',par)