At attempt to use MCMC to solve simple substitution ciphers
=====

A work in progress that I will probably abandon.  It sortof works sometimes.

It was an interesting idea.  I tried it out.

It's not the right way to write a cryptogram solver.

But in some failure modes it produces plausibly pronounceable non-dictionary words.

Usage example
=====


    $ python3
    Python 3.6.5 (default, Jun 17 2018, 12:13:06) 
    [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from CryptoGibbs import *
    >>> raw_text = " This is a good idea. So the “problem” is that the single sampled sentence in the cryptogram may not fall at exactly the observed probability vector from the corpus? That is, that some sentences don’t use enough ETH trigrams "
    >>> c = Cipher()
    >>> scrambled = c.scramble(raw_text)
    >>> scrambled
    ' pbmu mu j oggw mwaj ug pba lvgctan mu pbjp pba umxota ujnltaw uaxpaxda mx pba dvhlpgovjn njh xgp rjtt jp akjdpth pba gcuavyaw lvgcjcmtmph yadpgv rvgn pba dgvlqu pbjp mu pbjp ugna uaxpaxdau wgxp qua axgqob apb pvmovjnu '
    >>> solver = CryptoGibbs(scrambled)
    About to build trigram map
    About to ingest brown corpus
    built trigram map
    Initial perm prob log is 541.7961927037308
    >>> solver.jump_for(10000)
    Current guess is  this is a good idea so the problem is that the single sampled sentence in the cryptogram may not wall at exactly the obserfed probability fector wrom the corpus that is that some sentences dont use enough eth trigrams 
    Best guess was  this is a good idea so the problem is that the single sampled sentence in the cryptogram may not wall at exactly the obserfed probability fector wrom the corpus that is that some sentences dont use enough eth trigrams 
    >>> 


Failure example
====

Here we try it on a scrambled message that is too short for this technique.

Note, at the end of this sample, the log likelihood of the incorrect
solution is higher than the log likelihood of the correct solution.

    >>> raw_text = " This message is probably too short "
    >>> scrambled = c.scramble(raw_text)
    >>> scrambled
    ' pbmu nauujoa mu lvgcjcth pgg ubgvp '
    >>> solver = CryptoGibbs(scrambled)
    About to build trigram map
    About to ingest brown corpus
    built trigram map
    Initial perm prob log is 85.57526567246632
    >>> solver.jump_for(10000)
    Current guess is  anto whoorch to diserely ass onsia 
    Best guess was  anto whoorch to diserely ass onsia 
    >>> solver.jump_for(10000)
    Current guess is  anto whoorch to diserely ass onsia 
    Best guess was  anto whoorch to diserely ass onsia 
    >>> solver.best_p
    285.80768960451894
    >>> solver.get_prob_log(c)
    283.8936171749462
    >>> 

