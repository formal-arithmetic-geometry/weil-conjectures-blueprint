+++
id = "sk-prop-sf-comparison"
kind = "theorem"
title = "Bounded-below cohomology comparison"
order = 728
lean = ["AlgebraicGeometry.ProEtale.comparisonUpperStar", "AlgebraicGeometry.ProEtale.full_comparisonUpperStar", "AlgebraicGeometry.ProEtale.faithful_comparisonUpperStar", "AlgebraicGeometry.ProEtale.nonempty_iso_comparisonUpperStar_comp_rightDerivedLowerStar"]
tags = ["sketch"]
+++
Let $X$ be a scheme, $\Lambda$ a ring, and $\nu_X:X_{\mathrm{proét}}\to X_{\mathrm{ét}}$
the comparison morphism. For $K\in D^+(X_{\mathrm{ét}},\Lambda)$ the unit of the
adjunction between
$\nu_X^*:D^+(X_{\mathrm{ét}},\Lambda)\to D^+(X_{\mathrm{proét}},\Lambda)$ and
$R\nu_{X,*}$ is an isomorphism

$$
K\xrightarrow{\ \sim\ }R\nu_{X,*}\nu_X^*K\quad\text{in }D^+(X_{\mathrm{ét}},\Lambda).
$$

Consequently $\nu_X^*:D^+(X_{\mathrm{ét}},\Lambda)\to D^+(X_{\mathrm{proét}},\Lambda)$ is
fully faithful, and there is a canonical isomorphism in the derived category
of $\Lambda$-modules

$$
R\Gamma(X_{\mathrm{proét}},\nu_X^*K)\simeq R\Gamma(X_{\mathrm{ét}},K).
$$

More generally, for a pro-étale affine $U=\varprojlim_iU_i$ with $U_i$
affine and étale over $X$,

$$
R\Gamma(U_{\mathrm{proét}},(\nu_X^*K)|_U)\simeq
\varinjlim_iR\Gamma((U_i)_{\mathrm{ét}},K|_{U_i}).
$$

The colimit here is a filtered derived colimit, so its cohomology is the
filtered colimit of the cohomology groups.
