+++
id = "lemma-weil-pbc-symmetric-product-p1"
kind = "lemma"
title = "Symmetric product map"
lean = ["AlgebraicGeometry.ProjectiveSpace.exists_isFinite_surjective_projectiveLinePow"]
order = 2057
uses = ["def-weil-pbc-symmetric-product-morphism", "lem-weil-pbc-symmetric-product-finite", "lem-weil-pbc-symmetric-product-surjective"]
+++
Let $S$ be a scheme and $N$ a finite nonempty set with $n+1$ elements, indexing
the homogeneous coordinates of $\mathbf P^n_S=\mathbf P(N;S)$. There is a finite
surjective $S$-morphism

$$
 \sigma_n:(\mathbf P^1_S)^n\longrightarrow\mathbf P^n_S,
$$

namely the symmetric-product morphism
$((x_1:y_1),\ldots,(x_n:y_n))\mapsto[F_0:\cdots:F_n]$ with
$\prod_{i=1}^n(x_it+y_i)=\sum_{j=0}^nF_jt^j$ of
[def-weil-pbc-symmetric-product-morphism].
