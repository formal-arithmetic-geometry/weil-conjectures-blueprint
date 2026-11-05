+++
id = "lemma-integral-models--3"
kind = "lemma"
title = "Integral inverse image"
order = 294004
aliases = ["bp-r087-3"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_leftDerivedUpperStar_obj_of_scheme"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves"]
+++
For a commutative condensed ring $\Lambda$, write
$D^b_{\mathrm{fp}}(X,\Lambda)$ for the bounded complexes of
$\Lambda_X$-module objects whose cohomology sheaves admit a finite
constructible stratification on which they are pro-étale locally finitely
presented. The entries of these finite presentations are sections of the
coefficient sheaf.

For every morphism of schemes $f:X\to Y$,
$$
Lf^*:D^b_{\mathrm{fp}}(Y,\Lambda)\longrightarrow
D^b_{\mathrm{fp}}(X,\Lambda).
$$
For the integral coefficients of the lemma, on Noetherian schemes this
category agrees with $\Dbc$ of [definition-constructible-sheaves], so this
gives the asserted preservation of $\Dbc(-,\mathcal O_E)$.
