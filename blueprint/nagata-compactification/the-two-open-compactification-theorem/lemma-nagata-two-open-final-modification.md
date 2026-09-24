+++
id = "lemma-nagata-two-open-final-modification"
kind = "lemma"
title = "Structural properties of the final common modification"
order = 560
uses = ["def-nagata-two-open-final-modification", "lemma-nagata-common-modification", "lemma-nagata-intermediate-separated"]
+++
Each $W'_i\to W_i$ is $U$-admissible; the maps $W'_i\hookrightarrow W$
are open immersions covering $W$; their copies of $U$ agree; and $W\to S$
is separated and of finite type. In particular the induced map
$j_W\colon U\to W$ is an open immersion.

## Proof

The schemes $W_i$ are separated and of finite type by
[lemma-nagata-intermediate-separated]. Thus all hypotheses of the
common-modification property apply, and
[lemma-nagata-common-modification] gives every stated assertion.
The map $j_W$ is the composite of $U\hookrightarrow W'_i$ with either open
immersion $W'_i\hookrightarrow W$; the two composites coincide by the
gluing construction.
