+++
id = "lemma-uniform-bounds-pro-etale-affines"
kind = "lemma"
title = "Uniform bounds"
order = 162
lean = ["AlgebraicGeometry.ProEtale.hasClassicalUniformBounds", "AlgebraicGeometry.ProEtale.relativeCohomologicalDimension_lt_top_of_finiteType"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-cohomological-dimension"]
+++
Let $X$ and $Y$ be of finite type over $k$, let $A$ be a finite
commutative $\ell$-primary ring, let $g:X\to Y$ be of finite type, and
put $d=\dim(X)+\href{@definition-cohomological-dimension}{\operatorname{cd}_\ell(k)}$. There is an integer $c$,
depending only on $X$, such that for every [classical](@definition-classical-pro-etale-sheaves) sheaf $F$ of
$A$-modules on [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site), every [pro-étale affine](@definition-ind-etale-pro-etale-weakly) $U$ over $X$ and
every [pro-étale affine](@definition-ind-etale-pro-etale-weakly) $V$ over $Y$,

$$
H^q(U,F)=0\ \text{ for }q>d,
\qquad
H^q(X\times_YV,F)=0\ \text{ for }q>c.
$$

Moreover $\href{@definition-cohomological-dimension}{\operatorname{cd}_\ell(g)}<\infty$.
