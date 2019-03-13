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
For each gram, I tried a large selection of a little less than a 1/4 of the corpus, a medium selection of 1/10 of the corpus and a significantly smaller selection of corpus. I chose those numbers because I wanted to be able to see patterns between small and large samples. The number of test lines are consistently about a fourth of the selected set.
For the sake of consistency, I started from line 0 each time. 

The accuracy measures were lower than I expected. But since logistic regression modeling isn't particulary suited for many classes, it is perhaps to be expected. The data, while not very large, still created a large amount of class labels out of its vocabulary. Finding a pattern and correctly predicting the right one would require much more data, and/or fewer labels to choose from. 


| Command                                                                     | Accuracy             | Perplexity        |
|-----------------------------------------------------------------------------|----------------------|-------------------|
| python gendata.py /scratch/brown_rga.txt browndata1.txt -N 2 -E 2000 -T 500 |                                         
| python gendata.py /scratch/brown_rga.txt browndata2.txt -N 2 -E 1000 -T 250 | 
| python gendata.py /scratch/brown_rga.txt browndata3.txt -N 2 -E 200  -T 50  | 0.1144               | 211.6655519438415
| python gendata.py /scratch/brown_rga.txt browndata4.txt -N 3 -E 2000 -T 500 |                                         
| python gendata.py /scratch/brown_rga.txt browndata5.txt -N 3 -E 1000 -T 250 |
| python gendata.py /scratch/brown_rga.txt browndata6.txt -N 3 -E 250  -T 50  | 0.12172442941673711  | 218.9950553462103 |
| python gendata.py /scratch/brown_rga.txt browndata7.txt -N 4 -E 2000 -T 500 |                                         
| python gendata.py /scratch/brown_rga.txt browndata8.txt -N 4 -E 1000 -T 250 |                                         
| python gendata.py /scratch/brown_rga.txt browndata9.txt -N 4 -E 250  -T 50  | 0.11129707112970712  | 214.31796164207617                    


## Reporting for Part Bonus 

See explanation above about how the optional flags are used for outputting tags and using word/tag pairs as labels.
Using tags as the class labels gives a significant higher accuracy since there are fewer tags than unique words.


| Command                                                                             | Accuracy             | Perplexity        |
|------------------------------------------------------------------------------------------------------------|-------------------|
| python gendata.py /scratch/brown_rga.txt 1.txt -N 2 -E 2000 -T 500 -F pairs -L tags |                                         
| python gendata.py /scratch/brown_rga.txt 2.txt -N 2 -E 1000 -T 250 -F pairs -L tags |
| python gendata.py /scratch/brown_rga.txt 3.txt -N 2 -E 200  -T 50 -F pairs -L tags  | 0.26634615384615384  | 64.46660070570107 |    
| python gendata.py /scratch/brown_rga.txt 4.txt -N 3 -E 2000 -T 500 -F pairs -L tags |                                         
| python gendata.py /scratch/brown_rga.txt 5.txt -N 3 -E 1000 -T 250 -F pairs -L tags |    
| python gendata.py /scratch/brown_rga.txt 6.txt -N 3 -E 250  -T 50 -F pairs -L tags  | 0.2451669595782074   | 70.992226710265   |
| python gendata.py /scratch/brown_rga.txt 7.txt -N 4 -E 2000 -T 500 -F pairs -L tags |                                         
| python gendata.py /scratch/brown_rga.txt 8.txt -N 4 -E 1000 -T 250 -F pairs -L tags |                                         
| python gendata.py /scratch/brown_rga.txt 9.txt -N 4 -E 250  -T 50 -F pairs -L tags  | 0.24416517055655296  | 73.88359785334593 |
