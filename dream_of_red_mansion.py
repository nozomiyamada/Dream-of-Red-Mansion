import re


# 1.1) split the text into 3 pieces
def split_text(file_name):
    """
    open the 'Dream of Red Mansion' and split
    search the word '第一回', '第四十回', ...

    split_text('dream_of_red_mansion.txt')
    >> part1.txt, part2.txt, part3.txt will be output
    """

    open_file = open(file_name, 'r')  # open file in read mode
    part1_file = open('part1.txt', 'w')  # make part1.txt in write mode
    part2_file = open('part2.txt', 'w')  # make part2.txt in write mode
    part3_file = open('part3.txt', 'w')  # make part3.txt in write mode

    text = open_file.read()  # read all text

    part1_start_index = text.find('第一回')  # search the start of 第一回
    part2_start_index = text.find('第四十一回')
    part3_start_index = text.find('第八十一回')

    part1_file.write(text[part1_start_index: part2_start_index])
    part2_file.write(text[part2_start_index: part3_start_index])
    part3_file.write(text[part3_start_index:])

    open_file.close()
    part1_file.close()
    part2_file.close()
    part3_file.close()


# 1.2) count adverbs in 3 documents
def count_adverb():
    """
    count 越发、难道、可巧、不曾、原是
    make local function 'count_from_one_file' in advance
    count them in each document by using local function 3 times and print

    count_adverb() # no argument
    >>
    part1.txt
    [('越发', 72), ('难道', 87), ('可巧', 47), ('不曾', 51), ('原是', 51)]
    part2.txt
    [('越发', 88), ('难道', 68), ('可巧', 40), ('不曾', 52), ('原是', 78)]
    part3.txt
    [('越发', 38), ('难道', 33), ('可巧', 1), ('不曾', 14), ('原是', 45)]
    """

    # local function for count adverb in one file
    def count_from_one_file(file_name):
        open_file = open(file_name, 'r')
        text = open_file.read()
        adverbs = ['越发', '难道', '可巧', '不曾', '原是']  # list of adverbs
        count_list = []  # initialize list
        for adverb in adverbs:
            number = text.count(adverb)  # count the each adverb
            count_list.append((adverb, number))  # make tuple (word, number) and append to list
        open_file.close()
        print(file_name)
        print(count_list)

    count_from_one_file('part1.txt')
    count_from_one_file('part2.txt')
    count_from_one_file('part3.txt')


# 1.3) count function words in 3 documents and calculate frequency
def count_function_word():
    """
    count 或、亦、方、即、皆、仍、故、尚、呀、吗、咧、罢、么、呢、让、向、往、就、但、 越、再、更、很、偏
    make local function 'count_from_one_file' in advance
    1. count all 汉字 but not count symbol > use variable 'count_all_letter'
    2. count ( 汉字 and function word ) > use variable 'count function word'
    count them in each document by using local function 3 times and print

    count_function_word() # no argument
    >>
    part1.txt
    频率: 2.75%
    part2.txt
    频率: 2.49%
    part3.txt
    频率: 2.66%
    """

    # local function for count function word in one file
    def count_from_one_file(file_name):
        open_file = open(file_name, 'r')
        text = open_file.read()
        words = ['或', '亦', '方', '即', '皆', '仍', '故', '尚', '呀', '吗', '咧', '罢', '么',
                 '呢', '让', '向', '往', '就', '但', '越', '再', '更', '很', '偏']
        count_all_letter = 0  # counter for all 汉字
        count_function_word = 0  # counter for functional word
        for letter in text:  # for loop each letter
            if letter.isalpha() == True:  # if and only if the letter is 汉字 (not count symbol)
                count_all_letter += 1
                if letter in words:  # if the letter is 汉字 and functional word
                    count_function_word += 1
        open_file.close()
        print(file_name)
        print('频率: {}%'.format(round(count_function_word * 100 / count_all_letter, 2)))  # calculate

    count_from_one_file('part1.txt')
    count_from_one_file('part2.txt')
    count_from_one_file('part3.txt')


# 1.4) count average paragraph and sentence length
def average_length():
    """
    count length of both paragraph and sentence and calculate average
    1. list of paragraphs: split text with '\n'
    2. list of sentences: split text with '．' '。' or '\n' (must use regular expression)
    3. count length of each element in list by using len()
        and make new list that contains only int
        e.g. ['你好', '我爱你',...] > [2, 3,...]
        at the same time, strip white space ' ' in head (or tail) of the sentence
    4. calculate average: (sum of the integers in the list) / (length of the list)

    average_length() # no argument
    >>
    part1.txt
    平均段落长度: 235.26
    平均句子长度: 26.34
    part2.txt
    平均段落长度: 343.24
    平均句子长度: 25.84
    part3.txt
    平均段落长度: 420.65
    平均句子长度: 26.57
    """

    # local function for count average length in one file
    def count_from_one_file(file_name):
        open_file = open(file_name, 'r')
        text = open_file.read()
        paragraph_list = text.splitlines()
        sentence_list = re.split('[．。\n]', text)
        paragraph_length = [len(paragraph.strip(' ')) for paragraph in paragraph_list]
        sentence_length = [len(sentence.strip(' ')) for sentence in sentence_list]
        average_paragraph = sum(paragraph_length) / len(paragraph_length)
        average_sentence = sum(sentence_length) / len(sentence_length)
        open_file.close()
        print(file_name)
        print('平均段落长度: {}'.format(round(average_paragraph, 2)))
        print('平均句子长度: {}'.format(round(average_sentence, 2)))

    count_from_one_file('part1.txt')
    count_from_one_file('part2.txt')
    count_from_one_file('part3.txt')