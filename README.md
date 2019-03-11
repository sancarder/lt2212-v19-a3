# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Sandra Derbring

## Additional instructions

Document here additional command-line instructions or other details you
want us to know about running your code.

## Reporting for Part 4

My hypothesis was that the larger the selected set, the higher accuracy and the lower perplexity.

To test this, I did nine test runs by a systematic scheme. I ran 3 instances with 2, 3, and 4 grams respectively.
For each gram, I tried a fourth of the corpus, half of the corpus and the whole corpus.
The number of test lines are consistently a fourth of the selected set.
For the sake of consistency, I started from line 0 each time. 

The accuracy measures were lower than I expected. But since logistic regression modeling isn't particulary suited for many classes, it is perhaps to be expected. The data, while not very large, still created a large amount of class labels out of its vocabulary. Finding a pattern and correctly predicting the right one would require much more data, and/or fewer labels to choose from. 


| Command                                                               | Output of test.py      |
|-----------------------------------------------------------------------|------------------------|
| python gendata.py /scratch/brown_rga.txt browndata1.txt -N 2 -E 2500 -T 600  | Accuracy:              |
| python gendata.py /scratch/brown_rga.txt browndata2.txt -N 2 -E 5000 -T 1200 | Accuracy:              |
| python gendata.py /scratch/brown_rga.txt browndata3.txt -N 2 -T 2400         | Accuracy:              |
| python gendata.py /scratch/brown_rga.txt browndata4.txt -N 3 -E 2500 -T 600  | Accuracy:              |
| python gendata.py /scratch/brown_rga.txt browndata5.txt -N 3 -E 5000 -T 1200 | Accuracy:              |
| python gendata.py /scratch/brown_rga.txt browndata6.txt -N 3 -T 2400         | Accuracy:              |
| python gendata.py /scratch/brown_rga.txt browndata7.txt -N 4 -E 2500 -T 600  | Accuracy:              |
| python gendata.py /scratch/brown_rga.txt browndata8.txt -N 4 -E 5000 -T 1200 | Accuracy:              |
| python gendata.py /scratch/brown_rga.txt browndata9.txt -N 4 -T 2400         | Accuracy:              |


## Reporting for Part Bonus 

(Delete if you aren't doing the bonus.)
