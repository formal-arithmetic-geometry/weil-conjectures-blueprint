+++
id = "lemma-change-coefficients--1"
kind = "lemma"
title = "Change of coefficients (1)"
name_showing = false
order = 699001
aliases = ["bp-r209-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_extendScalars", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToPadicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToRational", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_rationalToPadicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_derivedReduction_boundedConstructibleBaseChange"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "proposition-pro-etale-site-separably-closed--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-descent-finite-coefficient-field--3", "lemma-integral-models--3", "definition-pro-etale-base-change-map--1", "proposition-six-operations-dctf--3", "proposition-six-operations-dctf--4", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--16", "definition-change-of-coefficients-maps--1", "definition-change-of-coefficients-maps--4"]
+++
Suppose that the schemes in (8.1) are of finite type over
$k$. Let $\Lambda\to\Lambda'$ be a coefficient map of
Proposition [proposition-six-operations-change-coefficients] and let
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$. Then the square

$$
\begin{CD}
(g^*Rf_*K)_{\Lambda'} @>>> (Rf'_*g'^*K)_{\Lambda'}\\
@VVV @VVV\\
g^*Rf_*(K_{\Lambda'}) @>>> Rf'_*g'^*(K_{\Lambda'})
\end{CD}
$$

commutes. Here the upper arrow is the extension of scalars of the base change
map (4.5) for $K$, the lower arrow is the base change map
for $K_{\Lambda'}$, and the vertical arrows are the composites of the
change-of-coefficients isomorphisms of
Proposition [proposition-six-operations-change-coefficients] for $g^*$ and
$Rf_*$, respectively for $Rf'_*$ and $g'^*$.
