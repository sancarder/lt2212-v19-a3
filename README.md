# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Sandra Derbring

## Additional instructions

Document here additional command-line instructions or other details you
want us to know about running your code.

## Reporting for Part 4

My initial hypothesis was that the larger the selected set, the higher accuracy and the lower perplexity. But while running small tests to test the code, I realized that the accuracies were very low. My hypothesis then adjusted a little bit. Since the data is relatively small and there are so many labels, the changes in set selections and ngrams won't matter as much as I initially thought. 

To test this, I did nine test runs by a systematic scheme. I ran 3 instances with 2, 3, and 4 grams respectively.
For each gram, I tried a large selection of about 1/4 of the corpus, a medium selection of 1/10 of the corpus and a significantly smaller selection of corpus. I chose those numbers because I wanted to be able to see patterns between small and large samples. The number of test lines are consistently about a fourth of the selected set.
For the sake of consistency, I started from line 0 each time. 

The accuracy measures were lower than I expected. But since logistic regression modeling isn't particulary suited for many classes, it is perhaps to be expected. The data, while not very large, still created a large amount of class labels out of its vocabulary. Finding a pattern and correctly predicting the right one would require much more data, and/or fewer labels to choose from. 


| Command                                                                     | Output of test.py |
|-----------------------------------------------------------------------------|-------------------|
| python gendata.py /scratch/brown_rga.txt browndata1.txt -N 2 -E 2500 -T 600 | Accuracy:         |
| python gendata.py /scratch/brown_rga.txt browndata2.txt -N 2 -E 1000 -T 250 | Accuracy:         |
| python gendata.py /scratch/brown_rga.txt browndata3.txt -N 2 -E 250  -T 50  | Accuracy:         |
| python gendata.py /scratch/brown_rga.txt browndata4.txt -N 3 -E 2500 -T 600 | Accuracy:         |
| python gendata.py /scratch/brown_rga.txt browndata5.txt -N 3 -E 1000 -T 250 | Accuracy:         |
| python gendata.py /scratch/brown_rga.txt browndata6.txt -N 3 -E 250  -T 50  | Accuracy:         |
| python gendata.py /scratch/brown_rga.txt browndata7.txt -N 4 -E 2500 -T 600 | Accuracy:         |
| python gendata.py /scratch/brown_rga.txt browndata8.txt -N 4 -E 1000 -T 250 | Accuracy:         |
| python gendata.py /scratch/brown_rga.txt browndata9.txt -N 4 -E 250  -T 50  | Accuracy:         |


## Reporting for Part Bonus 

(Delete if you aren't doing the bonus.)
