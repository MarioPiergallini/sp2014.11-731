Mario Piergallini
Jeremy Doornbos

We first implemented IBM Model 1, and then added two things to this:
 
 - Symmetrization: We ran IBM Model 1 on both German-to-English and English-to-German and then took the intersection of the alignments generated. This leverages the information from both sides.
 - Exact matching: If a word is exactly the same in German and English, we added it to a set of exact matches if it also occurred in the same sentences 10% of the time. If the word was also long, the threshold was lowered. This captures the intuition that proper names and numerical expressions will tend to translate to themselves and that the longer an exact matching word is the more likely this is true ("die" is a bad match, "accounting" and "berlusconi" are probably good matches)

There are three Python programs here (`-h` for usage):

 - `./align` aligns words using Dice's coefficient.
 - `./check` checks for out-of-bounds alignment points.
 - `./grade` computes alignment error rate.

The commands are designed to work in a pipeline. For instance, this is a valid invocation:

    ./align -t 0.9 -n 1000 | ./check | ./grade -n 5


The `data/` directory contains a fragment of the German/English Europarl corpus.

 - `data/dev-test-train.de-en` is the German/English parallel data to be aligned. The first 150 sentences are for development; the next 150 is a blind set you will be evaluated on; and the remainder of the file is unannotated parallel data.

 - `data/dev.align` contains 150 manual alignments corresponding to the first 150 sentences of the parallel corpus. When you run `./check` these are used to compute the alignment error rate. You may use these in any way you choose. The notation `i-j` means the word at position *i* (0-indexed) in the German sentence is aligned to the word at position *j* in the English sentence; the notation `i?j` means they are "probably" aligned.
