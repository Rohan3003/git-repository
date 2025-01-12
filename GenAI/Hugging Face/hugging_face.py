import transformers
from transformers import pipeline

model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_classifier = pipeline(model=model_name)

text_input1 = "I love the weather today"
print(sentiment_classifier(text_input1))

text_input2 = "I hate my life"
print(sentiment_classifier(text_input2))

text_input3 = "I don't know what to do"
print(sentiment_classifier(text_input3))