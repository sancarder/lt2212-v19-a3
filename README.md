# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Sandra Derbring

## Additional instructions

Document here additional command-line instructions or other details you
want us to know about running your code.

To run the code, the flags -S, -E, -N and -T are implemented as requested. It is also possible to run flags to choose tags as class labels or word/tag pairs as features, as asked for in the bonus part. The flag [-L tags] outputs the labels as tags. The flag [-F pairs] uses the word/tag pair as features instead of words (and outputs them as labels, if not the -L flag is used). 

## Reporting for Part 4

My initial hypothesis was that the larger the selected set, the higher accuracy and the lower perplexity. But while running small tests to test the code, I realized that the accuracies were very low. My hypothesis then adjusted a little bit. Since the data is relatively small and there are so many labels, the changes in set selections and ngrams won't matter as much as I initially thought. 

To test this, I did nine test runs by a systematic scheme. I ran 3 instances with 2, 3, and 4 grams respectively.
For each gram, I tried a larger selection of a little less than a 1/10 of the corpus, a medium selection of 1/15 of the corpus and a significantly smaller selection of corpus. I chose those numbers because I wanted to be able to see patterns between small and large samples, but ran into memory errors when I tried larger samples. The number of test lines are consistently about a fourth of the selected set.
For the sake of consistency, I started from line 0 each time. 

The accuracy measures were lower than I expected. But since logistic regression modeling isn't particulary suited for many classes, it is perhaps to be expected. The data, while not very large, still created a large amount of class labels out of its vocabulary. Finding a pattern and correctly predicting the right one would require much more data, and/or fewer labels to choose from. The accuracy is pretty much consistent no matter what ngram number or test size was chosen even though the numbers tend to go down a little with the smaller datasets. The perplexity, however, clearly goes down when the dataset is smaller, but the ngram size does not seem to matter. 


| Command                                                                     | Accuracy             | Perplexity        |
|-----------------------------------------------------------------------------|----------------------|-------------------|
| python gendata.py /scratch/brown_rga.txt browndata1.txt -N 2 -E 1000 -T 250 | 0.13369254083178986  | 649.0675311467971 |
| python gendata.py /scratch/brown_rga.txt browndata2.txt -N 2 -E 600 -T 150  | 0.12077434267552731  | 463.2994515088634 |                                      
| python gendata.py /scratch/brown_rga.txt browndata3.txt -N 2 -E 200  -T 50  | 0.1144               | 211.6655519438415 |
| python gendata.py /scratch/brown_rga.txt browndata4.txt -N 3 -E 1000 -T 250 | 0.131286394917946    | 660.4166947750257 |
| python gendata.py /scratch/brown_rga.txt browndata5.txt -N 3 -E 600 -T 150  | 0.1274131274131274   | 464.34168359475194|                                        
| python gendata.py /scratch/brown_rga.txt browndata6.txt -N 3 -E 200  -T 50  | 0.12172442941673711  | 218.9950553462103 |
| python gendata.py /scratch/brown_rga.txt browndata7.txt -N 4 -E 1000 -T 250 | 0.13673253352152434  | 659.3543406562037 |                                        
| python gendata.py /scratch/brown_rga.txt browndata8.txt -N 4 -E 600 -T 150  | 0.12828344532681735  | 473.56566937236374|                                        
| python gendata.py /scratch/brown_rga.txt browndata9.txt -N 4 -E 200  -T 50  | 0.11129707112970712  | 214.31796164207617|                    


## Reporting for Part Bonus 

To use POS tags as features alongside words, I used the word/tag pairs as input for the features. The n:th word of the one hot vector is the POS tag and the model then predicts a POS tag from the input data. See explanation above about how the optional flags are used for outputting tags and using word/tag pairs as labels.
Using tags as the class labels gives a significant higher accuracy since there are fewer tags than unique words and correspondingly, a much lower perplexity. Just like for the data run on tokens, the ngram size does not seem to matter much for the accuracy and neither does the test size. For perplexity, though, test size clearly matters as perplexity goes down with smaller datasets.

| Command                                                                                             | Accuracy             | Perplexity         |
|-----------------------------------------------------------------------------------------------------|----------------------|--------------------|
| python gendata.py /scratch/brown_rga.txt tagged_browndata1.txt -N 2 -E 1000 -T 250 -F pairs -L tags | 0.2672506256703611   | 189.1507040289585  |
| python gendata.py /scratch/brown_rga.txt tagged_browndata2.txt -N 2 -E 600 -T 150 -F pairs -L tags  | 0.2601880877742947   | 129.25201965810083 |                                 
| python gendata.py /scratch/brown_rga.txt tagged_browndata3.txt -N 2 -E 200  -T 50 -F pairs -L tags  | 0.26634615384615384  | 64.46660070570107  |
| python gendata.py /scratch/brown_rga.txt tagged_browndata4.txt -N 3 -E 1000 -T 250 -F pairs -L tags | 0.28247528128196386  | 195.69383853249778 |
| python gendata.py /scratch/brown_rga.txt tagged_browndata5.txt -N 3 -E 600 -T 150 -F pairs -L tags  | 0.27053701015965165  | 127.32835980023437 |                             
| python gendata.py /scratch/brown_rga.txt tagged_browndata6.txt -N 3 -E 200  -T 50 -F pairs -L tags  | 0.2451669595782074   | 70.992226710265    |
| python gendata.py /scratch/brown_rga.txt tagged_browndata7.txt -N 4 -E 1000 -T 250 -F pairs -L tags | 0.2761260459319922   | 191.26096338783495 |                                 
| python gendata.py /scratch/brown_rga.txt tagged_browndata8.txt -N 4 -E 600 -T 150 -F pairs -L tags  | 0.2622563496751329   | 130.35212444340723 |                              
| python gendata.py /scratch/brown_rga.txt tagged_browndata9.txt -N 4 -E 200  -T 50 -F pairs -L tags  | 0.24416517055655296  | 73.88359785334593  |