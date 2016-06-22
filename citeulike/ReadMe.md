Files required:

train.tsv, validation.tsv, test.tsv: user\titem\trating, original they
require all to be positive feedback (ratings or clicks). But here I
changed it, train.tsv and validation.tsv will be positive as it used to
be, but test.tsv is a mix of positive and negative samples.

test_users.tsv:id of test users, used to recommend topK items for those
users, no longer needed.

mult.dat and vocab.dat: bag of words and dictionary of for the documents.

lda-fits: xxx
