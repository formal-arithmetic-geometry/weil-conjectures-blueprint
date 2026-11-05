+++
id = "lemma-change-coefficients"
kind = "lemma"
title = "Change of coefficients"
order = 698
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToRational", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_rationalToPadicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToPadicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_derivedReduction_boundedConstructibleBaseChange"]
uses = ["definition-constructible-sheaves", "definition-pro-etale-base-change-map", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients"]
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
