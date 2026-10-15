+++
id = "lem-weil-pbc-local-dimension-zero-henselian"
kind = "lemma"
title = "Local rings of dimension zero are henselian"
uses = ["def-weil-pbc-henselian-terminology"]
lean = ["isHenselianLocalRing_of_ringKrullDim_eq_zero"]
+++
Let $(R,\mathfrak m)$ be a local ring of Krull dimension $0$, i.e. a local ring whose only prime ideal is $\mathfrak m$ (for example an Artinian local ring). Then $R$ is henselian in the sense of [def-weil-pbc-henselian-terminology]: for every finite $R$-algebra $B$ (a ring map $R\to B$ making $B$ a finitely generated $R$-module), every idempotent of $B/\mathfrak mB$ lifts uniquely to an idempotent of $B$.
