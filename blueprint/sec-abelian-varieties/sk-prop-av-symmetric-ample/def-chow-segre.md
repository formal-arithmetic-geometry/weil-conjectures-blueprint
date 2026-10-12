+++
id = "def-chow-segre"
kind = "definition"
title = "Segre embedding"
order = 482
lean = ["AlgebraicGeometry.ProjectiveSpace.segre"]
uses = ["def-nagata-affine-proj", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-projective-space-base-change", "def-weil-pbc-scheme-conventions", "prop-nagata-proj-standard-open"]
+++
Let $S$ be a scheme and let $n$ and $m$ be index sets for the homogeneous
coordinates of $\mathbf P^{n}_S$ and $\mathbf P^{m}_S$. The *Segre
embedding* is the morphism of $S$-schemes

$$
s\colon\mathbf P^{n}_S\times_S\mathbf P^{m}_S
\longrightarrow\mathbf P^{n\times m}_S,
\qquad
\bigl((x_k)_{k\in n},(y_l)_{l\in m}\bigr)
\longmapsto
\bigl[x_k\,y_l\bigr]_{(k,l)\in n\times m} .
$$

Iterating it, for finitely many index sets $n_1,\dots,n_m$ one obtains the
morphism of $S$-schemes

$$
 s:\prod_{i=1}^m\mathbf P^{n_i}_S\longrightarrow
 \mathbf P^{n_1\times\dots\times n_m}_S,
 \qquad
 x\longmapsto\bigl[\prod_{i=1}^m x_{i,e_i}\bigr]_{e},
$$

where $x=\bigl((x_{i,k})_{k\in n_i}\bigr)_{i=1}^m$ and the target coordinates
$X_e$ are indexed by the tuples $e=(e_1,\dots,e_m)\in n_1\times\dots\times
n_m$. In the classical indexing $n_i=\{0,\dots,n_i\}$ the target is
$\mathbf P^{N}_S$ with $N=\prod_{i=1}^m(n_i+1)-1$.
