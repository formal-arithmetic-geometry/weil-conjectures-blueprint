+++
id = "lem-kun-compactification-affine"
kind = "lemma"
title = "Compactification of an affine scheme"
order = 6106
lean = ["AlgebraicGeometry.exists_projective_compactification_of_affine"]
uses = ["def-kun-projective", "def-kun-dimension"]
+++
Let $X$ be an affine scheme of finite type over a field $K$. There is an
open dense immersion $X\to\bar X$ with $\bar X$ projective over $K$ (choose a
closed immersion $X\hookrightarrow\mathbf A^n_K$, take the scheme-theoretic
closure in $\mathbf P^n_K$); one has $\dim\bar X=\dim X$.

## Proof

Write $X=\Spec(B)$ with $B$ a finitely generated $K$-algebra, fix a
surjection $K[T_1,\ldots,T_n]\twoheadrightarrow B$, giving a closed immersion
$X\hookrightarrow\mathbf A^n_K$ ($\mathbf A^n_K=\Spec(K[T_1,\ldots,T_n])$);
the open immersion $\mathbf A^n_K\hookrightarrow\mathbf P^n_K$ identifies the
complement of the hyperplane at infinity. Let $\bar X$ be the
scheme-theoretic closure of $X$ in $\mathbf P^n_K$; then $\bar X$ is a closed
subscheme of $\mathbf P^n_K$, hence projective over $K$ by
[def-kun-projective], and $X=\bar X\cap\mathbf A^n_K$ is open dense in
$\bar X$. The generic points of $\bar X$ lie in the open subset $X$, so
$\dim\bar X=\dim X$ by [def-kun-dimension].

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-derived-categories
