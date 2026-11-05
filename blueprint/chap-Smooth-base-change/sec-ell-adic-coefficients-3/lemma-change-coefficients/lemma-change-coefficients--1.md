+++
id = "lemma-change-coefficients--1"
kind = "lemma"
title = "Change of coefficients (1)"
name_showing = false
order = 699001
aliases = ["bp-r209-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_extendScalars", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_map_exchangeRight_derivedExtendScalars"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-inverse-image-tensor-product--1"]
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
