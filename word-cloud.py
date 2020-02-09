import requests
import string


html_start_text = "<!DOCTYPE html>\n"\
"<html>\n<head lang=\"en\">\n"\
"<meta charset=\"UTF-8\">\n"\
"<title>Tag Cloud Generator</title>\n"\
"</head>\n"\
"<body>\n"\
"<div style=\"text-align: center; vertical-align: middle; font-family: arial; color: white; \"background-color:black;" \
              " border:1px solid" \
              " black\">\n"

html_end_text = "</div>" \
            " </body>" \
            "</html>"

min_font_size = 20
max_font_size = 200


# Get the speech and store the main text in a variable
speech_url = requests.get("http://193.1.33.31:88/pa1/gettysburg.txt")
speech_body = speech_url.text

stopwords_url = requests.get("http://193.1.33.31:88/pa1/stopwords.txt")
stopwords_body = stopwords_url.text

# Make it into a list so that each word  is counted on its own
speech_words_list = speech_body.split()
stopwords_list = stopwords_body.split(sep=",")

# Initialise a dictionary
d = {}

# Print the words that are greater than 3 characters
for word in speech_words_list:
    if len(word) > 4:
        word = word.lower()
        word = word.strip(string.punctuation)
        print(word)
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

# Create Word Cloud
with open("cloud_tag.html", 'w') as cloud:
    cloud.write(html_start_text)
    for word in speech_words_list:
        cloud.write(f"<span style=\"font-size: {min(100 * 20, 200)}px\"> {word} </span>\n")
    cloud.write(html_end_text)
