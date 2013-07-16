#!/usr/local/bin/python3
# Name: August Brenner
# File name: speech_analyser.py
# Date: July 15th, 2013

import os
import re
import HTML_Modules

print("Content-type: text/html\n")
HTML_Modules.HTML_START("Speech Analyser")


# quick sort to sort the words
def quick_sort(key_value_list):
    if len(key_value_list) < 2:
        return list(key_value_list)
    else:
        pivot = key_value_list[0][1]
        small = []
        medium = []
        large = []

        for pair in key_value_list:
            if pair[1] < pivot:
                small.append(pair)
            if pair[1] == pivot:
                medium.append(pair)
            if pair[1] > pivot:
                large.append(pair)

        return quick_sort(large) + medium + quick_sort(small)


# convert dictionary to a list of key value pairs
def key_value_list(dictionary):
    key_value_list = []
    for key, value in dictionary.items():
        temp_list = [key, value]
        key_value_list.append(temp_list)
    return key_value_list


def text_analyser(file):

    # local file system path
    speech_path = speeches_dir + '/' + file

    # URL of the speech with title
    URL = '<li><a href="http://server.csmcis.net/~abrenn10/cgi-bin/cis117/speeches/' + file +\
          '">' + file + '</a></li>'

    # number of characters in the file
    f = open(speech_path, 'r', encoding='utf-8')
    all_content = f.read()
    number_of_chars = len(re.sub('\s+', '', all_content))

    # number of lines in the file
    f.seek(0, 0)
    lines = f.readlines()
    f.close()
    number_of_lines = len(lines)

    # number of words in the file
    words = re.split('\W+', all_content)
    number_of_words = len(words)

    # number of sentences in the file
    sentences = re.split('\.|\?|!', all_content)
    number_of_sentences = len(sentences)

    # average number of words per sentence
    words_per_sentence = int(len(words) / len(sentences))

    # number of paragraphs in the file
    paragraphs = re.split('\n\n', all_content)
    number_of_paragraphs = len(paragraphs)

    # percentage of meaningful words
    f = open('stop_words.txt')
    stopwords = f.read()
    f.close()
    stopwords_array = re.split('\n', stopwords)
    keywords = re.sub('\.|\?|!', '', all_content)
    keywords = keywords.lower()
    keywords = re.split('\W+', keywords)
    keywords = [word for word in keywords if word not in stopwords_array]
    percent_keywords = int((len(keywords) / number_of_words) * 100)

    # word count of meaningful words
    WORD_COUNT = {
    }

    for word in keywords:
        if word in WORD_COUNT.keys():
            WORD_COUNT[word] += 1
        else:
            WORD_COUNT[word] = 1

    ordered_words = quick_sort(key_value_list(WORD_COUNT))

    values = [number_of_chars, number_of_lines, number_of_words, number_of_sentences, words_per_sentence,
              number_of_paragraphs, percent_keywords]
    titles = ['Chars', 'Lines', 'Words', 'Sentences', 'Words per Sent.', 'Paragraphs', 'Meaningful']

    output = '''
    <div>
        <h2>''' + URL + '''</h2>
        <table>
            <tr>
    '''
    for title in titles:
        output += '<th>' + title + '</th>'
    output += '''
            </tr>
            <tbody>
                <tr>
        '''
    for value in values:
        output += '<td>' + str(value) + '</td>'

    output += '''
                </tr>
            </tbody>
        </table>
        <h5>Ten Most Common Words</h5>
    '''
    for x in range(0, 10):
        output += "<span class='word" + str(x) + "'>" + ordered_words[x][0] + "</span><sub>" +\
                  str(ordered_words[x][1]) + "</sub>"
    output += '</div><hr>'

    return output

speeches_dir = os.getcwd() + "/speeches"
for file in os.listdir(speeches_dir):
    if file.endswith(".txt"):
        print(text_analyser(file))

HTML_Modules.HTML_End()