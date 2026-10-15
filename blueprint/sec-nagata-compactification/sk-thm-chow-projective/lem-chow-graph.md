+++
id = "lem-chow-graph"
kind = "lemma"
title = "The graph of the cover"
order = 1089
lean = ["AlgebraicGeometry.ChowGraph", "AlgebraicGeometry.ChowGraph.emb", "AlgebraicGeometry.ChowGraph.exists_isClosedImmersion_over", "AlgebraicGeometry.ChowGraph.proj", "AlgebraicGeometry.ChowGraph.toGraph"]
uses = ["def-chow-segre", "def-nagata-affine-proj", "def-nagata-projective-space-base-change", "def-weil-pbc-scheme-conventions", "lem-chow-affine-immersion", "lem-chow-closed-model", "lem-chow-scheme-theoretic-closure", "lem-chow-tuple-immersion", "lem-weil-pbc-closed-immersion-products", "lemma-nagata-dense-affine-cover-exists"]
+++
Let $f\colon X\to S$ be a morphism of schemes, let $U_1,\dots,U_m$ be finitely
many open subschemes of $X$ and put $U:=U_1\cap\dots\cap U_m$. For each $i$ let
$Z_i$ be a proper closed model of $U_i\to S$ as in [lem-chow-closed-model]: a
closed immersion $Z_i\to\mathbf P^{n_i}_S$ ($n_i$ a finite set) and a
scheme-theoretically dense open immersion $U_i\to Z_i$ compatible with the
maps to $S$. Let $Z\subseteq\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S$
(the product in the category of $S$-schemes) be the scheme-theoretic image of

$$
j=(j_1,\dots,j_m)\colon U
\longrightarrow\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S ,
$$

where $j_i$ is the composite $U\subseteq U_i\to Z_i\to\mathbf P^{n_i}_S$. Then:

1. $Z\to\mathbf P^{n_1}_S\times_S\dots\times_S\mathbf P^{n_m}_S$ is a
closed immersion and $Z\to S$ is proper; moreover there are a finite set $N$
and a closed immersion $Z\to\mathbf P^N_S$ of $S$-schemes.

If moreover the underlying space of $X$ is noetherian:

2. $j$ induces a scheme-theoretically dominant morphism $U\to Z$, which (if
$m\geq1$) is an open immersion identifying $U$ with a scheme-theoretically
dense open subscheme of $Z$;
3. for every $i$ the projection $\mathrm{pr}_i|_Z\colon Z\to\mathbf P^{n_i}_S$
factors through $Z_i$, and the induced morphism $p_i\colon Z\to Z_i$ is proper;
4. $p_i|_U$ is the open immersion $U\to U_i\to Z_i$; in particular (if
$m\geq1$) $U\subseteq p_i^{-1}(U_i)$.
