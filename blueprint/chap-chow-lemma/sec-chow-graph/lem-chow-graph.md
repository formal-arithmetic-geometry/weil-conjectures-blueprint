+++
id = "lem-chow-graph"
kind = "lemma"
title = "The graph of the cover"
order = 624
lean = ["AlgebraicGeometry.ChowGraph", "AlgebraicGeometry.ChowGraph.emb", "AlgebraicGeometry.ChowGraph.exists_isClosedImmersion_over", "AlgebraicGeometry.ChowGraph.proj", "AlgebraicGeometry.ChowGraph.toGraph"]
uses = ["lem-chow-affine-immersion", "lem-chow-closed-model", "lem-chow-segre", "lem-chow-tuple-immersion"]
+++
Let $S$ be noetherian, let $X\to S$ be separated of finite type and let
$X=U_1\cup\dots\cup U_m$ be a finite affine open covering such that
$U:=U_1\cap\dots\cap U_m$ is scheme-theoretically dense in $X$. Choose, by
[lem-chow-affine-immersion], immersions
$j_i\colon U_i\to\mathbf P^{n_i}_S$ and, by [lem-chow-closed-model],
closed subschemes $Z_i\subseteq\mathbf P^{n_i}_S$ with $U_i\to Z_i$ a
scheme-theoretically dense open immersion and $Z_i\to S$ proper. Let
$Z\subseteq\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S$ be the
scheme-theoretic image of

$$
j=(j_1|_U,\dots,j_m|_U)\colon U
\longrightarrow\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S .
$$

Then:

1. $Z\to\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S$ is a
closed immersion, $j$ induces an open immersion $U\to Z$ identifying $U$ with
a scheme-theoretically dense open subscheme of $Z$, and $Z\to S$ is proper;
1. for every $i$ the projection $\mathrm{pr}_i|_Z\colon Z\to\mathbf P^{n_i}_S$ factors through $Z_i$, and the induced morphism
$p_i\colon Z\to Z_i$ is proper;
1. $p_i|_U$ is the open immersion $U\to U_i\to Z_i$; in particular
$U\subseteq p_i^{-1}(U_i)$.

The formalisation takes the $m$-fold fibre product
$\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S$ to be the categorical
product in the category of $S$-schemes, so that (1) is a closed immersion into
that product rather than into a single projective space; the composition with
the Segre embedding of [lem-chow-segre], giving a closed immersion
$Z\to\mathbf P^N_S$ over $S$ as used in Step 7 of the proof of
[thm-chow-lemma], is the separate statement
`ChowGraph.exists_isClosedImmersion_over` listed above. It also
weakens the hypotheses to what the proof uses:
the members of the cover need not be affine and need not cover $X$, only $X$
needs to be a noetherian space, and $U$ need not be dense in $X$.

## Proof

Each $j_i|_U$ is an immersion, being the composition of the open immersion
$U\to U_i$ with the immersion $j_i$. Hence $j$ is an immersion by
[lem-chow-tuple-immersion], and it is quasi-compact because $U$ is
noetherian. Part (1) now follows from 01RG for the first two
assertions; for the third, $\mathbf P^{n_1}_S\times_S\dots\times_S \mathbf P^{n_m}_S\to S$ is proper, being a finite fibre product of proper
$S$-schemes, and $Z$ is a closed subscheme of it, so $Z\to S$ is proper by
01W5.

For (2), the open immersion $U\to Z$ is quasi-compact and scheme-theoretically
dominant, so $\mathrm{pr}_i|_Z\colon Z\to\mathbf P^{n_i}_S$ and its restriction
$\mathrm{pr}_i\circ j=j_i|_U$ to $U$ have the same kernel. That kernel
contains the ideal sheaf of $Z_i$, because $j_i|_U$ factors through $Z_i$ by
construction; so the universal property of the closed immersion
$Z_i\to\mathbf P^{n_i}_S$ produces the morphism $p_i\colon Z\to Z_i$ with
$p_i$ followed by $Z_i\to\mathbf P^{n_i}_S$ equal to $\mathrm{pr}_i|_Z$. (This
is 01R9 in the case in which $Z_i$ is presented as the
scheme-theoretic image of $j_i|_U$, which it is: formation of the
scheme-theoretic image commutes with restriction to the open $U_i\subseteq X$.)
It is proper: $Z\to S$ is proper by (1) and $Z_i\to S$ is separated, so $p_i$
is proper by 01W6.

Part (3) is immediate from $\mathrm{pr}_i\circ j=j_i|_U$ and the fact that
$j_i$ identifies $U_i$ with an open subscheme of $Z_i$.
