+++
id = "lem-sc-rigidity"
kind = "lemma"
title = "The rigidity lemma"
lean = ["AlgebraicGeometry.exists_eq_snd_comp"]
order = 455
+++
Let $k$ be a field and $X,Y,Z$ schemes over $k$ with $X$ proper,
geometrically connected and geometrically reduced over $k$, $Y$
connected, and $Z$ separated over $k$.
Let $f:X\times_kY\to Z$ be a morphism of $k$-schemes such that, for
some point $y_0\in Y$, the image under $f$ of the fibre
$\operatorname{pr}_2^{-1}(y_0)=X\times_k\Spec\kappa(y_0)$ is a single
point. Then $f$ factors through the projection
$X\times_kY\to Y$: there is a morphism $g:Y\to Z$ with
$f=g\circ\operatorname{pr}_2$.
