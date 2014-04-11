mpiergal
jdoornbos

We simply implemented the ability to swap adjacent phrases.

When it finds a phrase X in the translation model, it adds it to the hypotheses on the appropriate stack. But then it finds the next phrase Y (if any) that begins with the following word. For each one it finds, it then adds Y + X (the reversed order) to the hypotheses on the appropriate stack (which would be later since it translates more of the input).

This doesn't keep track of what has already been translated (but it doesn't need to). It could be made more efficient by using more dynamic programming to avoid duplicating work.

There are three Python programs here (`-h` for usage):

 - `./decode` a simple non-reordering (monotone) phrase-based decoder
 - `./grade` computes the model score of your output

The commands are designed to work in a pipeline. For instance, this is a valid invocation:

    ./decode | ./grade


The `data/` directory contains the input set to be decoded and the models

 - `data/input` is the input text

 - `data/lm` is the ARPA-format 3-gram language model

 - `data/tm` is the phrase translation model

