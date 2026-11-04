+++
id = "lemma-uniform-bounds-pro-etale-affines"
kind = "lemma"
title = "Uniform bounds"
order = 162
lean = ["AlgebraicGeometry.ProEtale.hasClassicalUniformBounds", "AlgebraicGeometry.ProEtale.relativeCohomologicalDimension_lt_top_of_finiteType"]
+++
Let $X$ and $Y$ be of finite type over $k$, let $A$ be a finite
commutative $\ell$-primary ring, let $g:X\to Y$ be of finite type, and
put $d=\dim(X)+\operatorname{cd}_\ell(k)$. There is an integer $c$,
depending only on $X$, such that for every classical sheaf $F$ of
$A$-modules on $X_{\mathrm{pro}\acute{e}t}$, every pro-étale affine $U$ over $X$ and
every pro-étale affine $V$ over $Y$,

$$
H^q(U,F)=0\ \text{ for }q>d,
\qquad
H^q(X\times_YV,F)=0\ \text{ for }q>c.
$$

Moreover $\operatorname{cd}_\ell(g)<\infty$.
