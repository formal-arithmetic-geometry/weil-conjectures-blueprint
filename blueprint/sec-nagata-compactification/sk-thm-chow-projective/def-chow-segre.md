+++
id = "def-chow-segre"
kind = "definition"
title = "Segre embedding"
order = 420
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

The morphism $s$ is defined over $\operatorname{Spec}\mathbf Z$ by these
formulas and over a general $S$ by base change along $S\to\operatorname{Spec}\mathbf Z$.
