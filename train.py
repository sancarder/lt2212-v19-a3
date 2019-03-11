import os, sys
import argparse
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

# train.py -- Don't forget to put a reasonable amount code comments
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

    
def train_model(vectors, labels):

    #Makes an instance of the model
    logregModel = LogisticRegression(solver="lbfgs", multi_class='multinomial')
    
    #Trains the model on the data
    logregModel.fit(vectors, labels)

    return logregModel
    
def parse_arguments(parser):

    #Adds arguments from the command line to the parser  

    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
    parser.add_argument("datafile", type=str, help="The file name containing the features.")
    parser.add_argument("modelfile", type=str, help="The name of the file to which you write the trained model.")

    return parser.parse_args()


if __name__ == "__main__":

    #Parses the arguments from the command line                                                                                                                                     
    args = parse_arguments(argparse.ArgumentParser(description="Train a maximum entropy model."))    
    
    print("Loading data from file {}.".format(args.datafile))
    vectors, labels = load_data(args.datafile)

    print("Training {}-gram model.".format(args.ngram))
    logreg = train_model(vectors, labels)
    
    print("Writing table to {}.".format(args.modelfile)) 
    with open(args.modelfile, 'wb') as mf:
        model = pickle.dump(logreg, mf)
    




    
    # YOU WILL HAVE TO FIGURE OUT SOME WAY TO INTERPRET THE FEATURES YOU CREATED.
    # IT COULD INCLUDE CREATING AN EXTRA COMMAND-LINE ARGUMENT OR CLEVER COLUMN
    # NAMES OR OTHER TRICKS. UP TO YOU.

