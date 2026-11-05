+++
id = "lemma-punctured-surface-punctured-curve--1"
kind = "lemma"
title = "Restriction to the punctured trait at a transverse corner"
name_showing = false
order = 970001
aliases = ["bp-r295-1"]
lean = ["AlgebraicGeometry.Scheme.TransverseCorner.bijective_cohomologyMap_puncturedTraitι"]
uses = []
+++
Let $Z$ be a regular locally noetherian scheme over an algebraically
closed field $k$, and suppose that $Z$ is an étale limit, with affine
transition maps, of smooth surfaces over $k$. Let $D_1,D_2\subset Z$ be
regular divisors meeting transversely at exactly one point $z$; thus their
scheme-theoretic intersection is regular of codimension two in $Z$.
Choose a geometric point $\bar z:\operatorname{Spec}\Omega\to Z$ over $z$
with $\Omega$ algebraically closed. Write $S=Z_{(\bar z)}$, let $z_S$ be
its closed point, and put $D_{i,S}=D_i\times_Z S$.

Let $\ell$ be a prime invertible in $k$. For every $q\geq0$, the
restriction map

$$
H^q(S-D_{2,S},\mathbf F_\ell)\longrightarrow
H^q(D_{1,S}-z_S,\mathbf F_\ell)
$$

is bijective. Here the coefficients on the target are identified with
the pullback of the constant sheaf on the source.
