+++
id = "lem-weil-pbc-local-dimension-zero-henselian"
kind = "lemma"
title = "Local rings of dimension zero are henselian"
uses = ["def-weil-pbc-henselian-terminology"]
lean = ["isHenselianLocalRing_of_ringKrullDim_eq_zero"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 06RS (lemma-local-dimension-zero-henselian, line 42571); its proof uses Lemma Tag 04GG (lemma-characterize-henselian) (10)=>(1), Lemma 05DR (lemma-finite-finite-fibres), Lemma 00GT (lemma-integral-no-inclusion), Lemma 00E0 (lemma-Zariski-topology), Lemma 00JA (lemma-product-local). The strictly henselian variant (residue field separably closed) is lem-weil-pbc-dimension-zero-local-strictly-henselian, whose proof contains this argument."
+++
Let $(R,\mathfrak m)$ be a local ring of Krull dimension $0$, i.e. a local ring whose only prime ideal is $\mathfrak m$ (for example an Artinian local ring). Then $R$ is henselian in the sense of [def-weil-pbc-henselian-terminology]: for every finite $R$-algebra $B$ (a ring map $R\to B$ making $B$ a finitely generated $R$-module), every idempotent of $B/\mathfrak mB$ lifts uniquely to an idempotent of $B$.
