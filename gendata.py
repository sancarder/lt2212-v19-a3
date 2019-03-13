import os, sys
import glob
import argparse
import numpy as np
import pandas as pd

# gendata.py -- Don't forget to put a reasonable amount code comments
# in so that we better understand what you're doing when we grade!

# add whatever additional imports you may need here. You may not use the
# scikit-learn OneHotEncoder, or any related automatic one-hot encoders.
import random
import nltk
from nltk import ngrams


def load(inputfile):

    # Loads the file and returns the lines
    with open(inputfile, 'r') as myFile:
        lines = myFile.readlines()

    return lines


def prepare_data(lines, startline, endline, testnumber):

    corpus_lines = []

    print("This file has {} lines.".format(len(lines)))
    
    print("Starting from line {}.".format(startline))
    if endline:
        print("Ending at line {}.".format(endline))
    else:
        print("Ending at last line of file.")    


    #Fetch all lines between the given start and end lines
    for line in lines[startline:endline]:
        corpus_lines.append(line)
    
    #Shuffles the list of lines and split them
    #into training and test sets
    random.shuffle(corpus_lines)
    test_lines = corpus_lines[:testnumber]
    training_lines = corpus_lines[testnumber:]
            
    return corpus_lines, training_lines, test_lines       


def lines_to_tokens(lines):

    words = []
    tags = []
    pairs = []

    #Using NLTK to tokenize the sentence and strip the tags
    for line in lines:
        for pair in line.split():
            word, tag = nltk.tag.str2tuple(pair)
            words.append(word)
            tags.append(tag)
            pairs.append(pair)
                
    return words, tags, pairs


def create_vocabulary(words):

    vocabulary = {}
    count = 1

    #Adding start item at index 0 in vocabulary
    vocabulary['<start>'] = 0

    #Adding words in set from index 1
    for word in words:
        if word not in vocabulary:
            vocabulary[word] = count
            count+=1

    return vocabulary
 

def one_hot_transform(vocabulary):

    onehots = {}
    
    for word in vocabulary:
        #Creates an array of zeros in the lenght of V
        onehot = np.zeros((len(vocabulary),), dtype='int')

        #Assign 1 on the index where the word belongs
        windex = vocabulary[word]
        onehot[windex] = 1        

        onehots[word] = onehot

    return onehots


def produce_features(ngrams, onehots, tag_ngrams, labeltype):

    vectors = []

    for i in range (len(ngrams)):

        gram = ngrams[i]
        tag_gram = tag_ngrams[i]
        
        #Get label as word or tag
        if labeltype == 'tags':
            label = tag_gram[-1]
        else:
            label = gram[-1]
        
        #Get one hot vectors for all word but the last
        ohv_list = []
        for g in gram[:-1]:
            ohv_list.append(onehots[g])
                
        ohv_array = np.concatenate(ohv_list)

        #Append label at the end of the array
        features = np.append(ohv_array, label)

        vectors.append(features)

    #Add all features in one stack
    all_arrays = np.stack(vectors)
    
    return all_arrays


def print_feature_table(outputfile, arrays, ngrams, datatype):
    
    #Name file after type of data (train or test)
    filename = outputfile.split('.')[0]
    outputfile = filename+'.'+datatype

    #Makes a panda dataframe                                                                                                                                                    
    pdframe = pd.DataFrame(arrays)
    
    #Prints to file                                                                                                                                                           
    with open(outputfile, 'w') as out:
        pdframe.to_csv(out, encoding="utf-8", columns=None)
    

def parse_arguments(parser):

    """Parses the arguments from the command line.                                                                                                                                  
    Args:                                                                                                                                                                           
    parser:   An ArgumentParser object.                                                                                                                                           
    Returns:                                                                                                                                                                        
        A Namespace object built from the parsed attributes.                                                                                                                        
    """ 
 
    #Adds arguments from the command line to the parser
    parser.add_argument("inputfile", type=str, help="The file name containing the text data.")
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
    parser.add_argument("-S", "--start", metavar="S", dest="startline", type=int, default=0, help="What line of the input data file to start from. Default is 0, the first line.")
    parser.add_argument("-E", "--end", metavar="E", dest="endline", type=int, default=None, help="What line of the input data file to end on. Default is None, the last line.")
    parser.add_argument("outputfile", type=str, help="The name of the output file for the feature table.")
    parser.add_argument("-T", "--lines", metavar="T", dest="testlines", type=int, default=None, help="The number of lines assigned to test data (default None).")
    parser.add_argument("-L", "--label", metavar="L", dest="label", type=str, default="words", help="The type of label to classify (words or tags) (default words).")
    parser.add_argument("-F", "--features", metavar="F", dest="features", type=str, default="words", help="The type of features to model on (words or pairs) (default words).")

    return parser.parse_args()


if __name__ == "__main__":

    ngram_cond = True
    startline_cond = True
    endline_cond = True
    testline_cond = True
    
    #Parses the arguments from the command line                                                                                                                                     
    args = parse_arguments(argparse.ArgumentParser(description="Convert text to features."))

    #Read the file into lines
    print("Loading data from file {}.".format(args.inputfile))
    lines = load(args.inputfile)

    #Checking conditions
    if args.ngram < 2:
        ngram_cond = False
        print("The ngram needs to be at least 2. Try again. ")
        
    if args.startline > len(lines):
        startline_cond = False
        print("The files have too few lines or your starting point occurs later than your end point. Try again.")

    if args.endline:
        if args.endline > len(lines) or args.startline > args.endline:
            endline_cond = False
            print("The files have too few lines to end at this line. Try again.")

    if args.testlines and args.endline:
        if args.testlines > (args.endline-args.startline):
            testline_cond = False
            print("Your test set can't be larger than the total set")

        
    #If all conditions hold, run the rest of the script
    if ngram_cond and startline_cond and endline_cond and testline_cond:

        #Splitting data into sets
        corpus_lines, training_lines, test_lines = prepare_data(lines, args.startline, args.endline, args.testlines)

        #Tokenize each set
        corpus_tokens, corpus_tags, corpus_pairs = lines_to_tokens(corpus_lines)
        training_tokens, training_tags, training_pairs = lines_to_tokens(training_lines)
        test_tokens, test_tags, test_pairs = lines_to_tokens(test_lines)

        #Creating ngrams for training and test sets with a start symbol on the far right
        training_token_ngrams = list(ngrams(training_tokens, args.ngram, pad_left=True, left_pad_symbol='<start>'))
        training_tag_ngrams = list(ngrams(training_tags, args.ngram, pad_left=True, left_pad_symbol='<start>'))
        training_pair_ngrams = list(ngrams(training_pairs, args.ngram, pad_left=True, left_pad_symbol='<start>'))
        test_token_ngrams = list(ngrams(test_tokens, args.ngram, pad_left=True, left_pad_symbol='<start>'))
        test_tag_ngrams = list(ngrams(test_tags, args.ngram, pad_left=True, left_pad_symbol='<start>'))
        test_pair_ngrams = list(ngrams(test_pairs, args.ngram, pad_left=True, left_pad_symbol='<start>'))

        #Create vocabulary and one hot vectors for the corpus
        if args.features == 'pairs':
            vocab_data = corpus_pairs
            training_ngrams = training_pair_ngrams
            test_ngrams = test_pair_ngrams

        else:
            vocab_data = corpus_tokens
            training_ngrams = training_token_ngrams
            test_ngrams = test_token_ngrams            

            
        vocabulary = create_vocabulary(vocab_data)
        onehots = one_hot_transform(vocabulary)

        #Produce features for sets
        print("Constructing {}-gram model for training data with {} tokens".format(args.ngram, len(training_tokens)))
        training_data = produce_features(training_ngrams, onehots, training_tag_ngrams, args.label)
        
        print("Constructing {}-gram model for test data with {} tokens".format(args.ngram, len(test_tokens)))
        test_data = produce_features(test_ngrams, onehots, test_tag_ngrams, args.label)

        #Write sets to file
        print("Writing table to training file")
        print_feature_table(args.outputfile, training_data, training_ngrams, "train")

        print("Writing table to test file")
        print_feature_table(args.outputfile, test_data, test_ngrams,  "test")


        # THERE ARE SOME CORNER CASES YOU HAVE TO DEAL WITH GIVEN THE INPUT
        # PARAMETERS BY ANALYZING THE POSSIBLE ERROR CONDITIONS.
