+++
id = "lem-zl-noether-normalization-dimension"
kind = "lemma"
title = "The number of Noether coordinates is the Krull dimension"
lean = ["ringKrullDim_eq_of_finite_inj_algHom_mvPolynomial"]
order = 2993
uses = ["lem-zl-noether-normalization-field", "pqf-lem-going-up", "pqf-lem-incomparability", "pqf-lem-lying-over"]
+++
Let $K$ be a field, $B\neq0$ a finitely generated commutative
$K$-algebra, and $K[T_1,\ldots,T_d]\to B$ an injective $K$-algebra
homomorphism over which $B$ is a finitely generated module (such a
map exists by [lem-zl-noether-normalization-field]). Then
$d=\dim B$, the Krull dimension of $B$; in particular
$\dim B<\infty$.

In particular, if $B$ has Krull dimension one, there is an injective
$K$-algebra homomorphism $K[T]\to B$ making $B$ a finite
$K[T]$-module. This holds in particular over finite fields $K$, and
applies to the coordinate rings of affine charts of the curves over
$\mathbf F_q$ considered in this part.
