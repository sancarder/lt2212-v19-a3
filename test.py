import os, sys
import argparse
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

# test.py -- Don't forget to put a reasonable amount code comments
# in so that we better understand what you're doing when we grade!

# add whatever additional imports you may need here.

def load_data(datafile):

    #Load the data and divide it into features and labels                                                                                                                            
    #Read the data and transform it into an numpy array                                                                                                                             
    df = pd.read_csv(datafile)

    #Fetch data from all columns but the last one (labels)                                                                                            
    features = df.iloc[:, :-1]                                                                                                                                                     
    
    #Fetch data from the last column to get class labels                                                                                                                     
    labels = df.iloc[:, -1]
    
    return features, labels


def test_model(model, features, labels):
    
    #Sets the classes_ attribute to the known labels
    setattr(model, 'classes_', labels)

    #Predict labels
    predicted_classes = model.predict(features)    
    #for i in range(len(features)):
        #print("N-gram: {}, Predicted: {}, Real: {}".format(features.values[i], predicted_classes.values[i], labels[i]))

    #Get predicted log probabilities
    predicted_logs = model.predict_log_proba(features)
    
    #Get predicted probabilities
    predicted_probas = model.predict_proba(features)

    #Calculate entropy and perplexity on the probability distribution
    crossentropy = calculate_crossentropy(predicted_probas, predicted_logs)
    perplexity = calculate_perplexity(crossentropy)
    
    #Calculate accuracy
    accuracy = model.score(features, labels)
        
    return accuracy, perplexity


def calculate_crossentropy(probs, logs):

    #Calculates the cross entropy of a probability distribution
    #The probability distribution is all probabilities for all ngrams
    #It is then divided with 1/N
        
    values = []

    #Multiply each probability measure with its log probability
    for i in range(len(probs)):
        for j in range(len(probs[i])):
            values.append(probs[i][j] * logs[i][j]) #p * l

    #Sum the calculations
    pp_sum = -sum(values)

    #Multiply the sum with 1/N
    crossentropy = (1/len(values))*pp_sum
    
    return crossentropy


def calculate_perplexity(entropy):

    #Calculate perplexity by raising the power of the entropy
    perplexity = np.power(2, entropy)
    
    return perplexity


def parse_arguments(parser):

    #Adds arguments from the command line to the parser                                                                                                                              
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
    parser.add_argument("datafile", type=str, help="The file name containing the features in the test data.")
    parser.add_argument("modelfile", type=str, help="The name of the saved model file.")

    return parser.parse_args()


if __name__ == "__main__":

    #Parses the arguments from the command line                                                                                                                                     
    args = parse_arguments(argparse.ArgumentParser(description="Test a maximum entropy model."))

    print("Loading data from file {}.".format(args.datafile))
    features, labels = load_data(args.datafile)
    
    print("Loading model from file {}.".format(args.modelfile))
    with open(args.modelfile, 'rb') as modelfile:
        model = pickle.load(modelfile)

    #print("Testing {}-gram model.".format(args.ngram))                                                                                                                         
    accuracy, perplexity = test_model(model, features, labels)

    print("Accuracy is: {}".format(accuracy))
    print("Perplexity is: {}".format(perplexity)) 
