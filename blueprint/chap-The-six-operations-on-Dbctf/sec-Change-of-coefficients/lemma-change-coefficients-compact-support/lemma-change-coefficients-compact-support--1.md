+++
id = "lemma-change-coefficients-compact-support--1"
kind = "lemma"
title = "Change of coefficients for compactly supported direct image (1)"
name_showing = false
order = 637001
aliases = ["bp-r194-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekExtendScalarsIso", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekToPadicAlgClIso", "AlgebraicGeometry.ProEtale.CondensedRing.etaleReductionLowerShriekIsoOfCompactification"]
uses = ["definition-constructible-sheaves", "definition-sp-scalar-extension", "lemma-extension-scalars-preserves-dctf", "definition-change-of-coefficients-maps", "definition-compactification-refinement", "proposition-construction-independence-rf-shriek", "proposition-comparison-etale-derived-category"]
+++
Let $\ell$ be a prime, let $k$ be a field of characteristic $p>0$ with
$p\ne\ell$, and let $E\subset\overline{\mathbf Q}_\ell$ be a finite
extension of $\mathbf Q_\ell$. Let $f:X\to Y$ be a morphism of separated
schemes of finite type over $k$, and define $Rf_!$ using the chosen
compactification as in
Proposition [proposition-construction-independence-rf-shriek].
For each of the coefficient maps
$$
\mathcal O_E\longrightarrow E,\qquad
E\longrightarrow\overline{\mathbf Q}_\ell,
$$
there is a natural isomorphism, for $K\in\Dbc(X,\Lambda)$,
$$
(Rf_!K)_{\Lambda'}\xrightarrow{\ \sim\ }Rf_!(K_{\Lambda'}).
$$
It is the composite of the proper direct-image comparison and the
extension-by-zero comparison, as in
Definition [definition-change-of-coefficients-maps](5). Here $\Dbc$
denotes complexes with bounded constructible cohomology; no separate
finite Tor-dimension hypothesis is imposed.

For $n\geq 0$, put $A_n=\mathcal O_E/\ell^n\mathcal O_E$ and let
$$
\operatorname{red}_{X,n}:\Dbc(X,\mathcal O_E)\longrightarrow
D(X_{\acute{e}t},A_n),\qquad
K\longmapsto R\nu_{X,*}(K\otimes^{\mathbf L}_{\mathcal O_E}A_n)
$$
be derived reduction followed by passage to the small étale site.
Every specified compactification $c$ of $f$ gives a natural isomorphism
$$
\operatorname{red}_{Y,n}(Rf_!K)\xrightarrow{\ \sim\ }
Rf_{\acute{e}t,!}(\operatorname{red}_{X,n}K),
\qquad K\in\Dbc(X,\mathcal O_E),
$$
formed from the comparisons for its open and proper parts.
