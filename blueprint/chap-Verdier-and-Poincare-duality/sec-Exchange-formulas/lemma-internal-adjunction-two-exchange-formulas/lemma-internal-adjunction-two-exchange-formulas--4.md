+++
id = "lemma-internal-adjunction-two-exchange-formulas--4"
kind = "lemma"
title = "Biduality under proper direct image"
name_showing = false
order = 829004
aliases = ["bp-r248-4"]
lean = ["AlgebraicGeometry.Etale.isIso_rightDerivedLowerStar_map_verdierDualDoubleDual_app_iff_of_finite"]
uses = ["definition-compactification-refinement", "definition-verdier-dual-evaluation"]
+++
The comparison through the particular maps $e_K$ in (10.3) is bypassed
by the Lean route; the proper step uses the following isomorphism
criterion.

Let $\Lambda$ be a finite commutative ring, let $f:X\to Y$ be proper,
and let $a_Y:Y\to S$. Put $a_X=a_Y\circ f$ and suppose that $f$,
$a_Y$ and $a_X$ each admit a compactification. Assume that the monoidal
structure on $f^*$ is compatible with the Koszul braidings. For every
$K\in D(X_{\acute{e}t},\Lambda)$,

$$
Rf_*\delta_K\text{ is an isomorphism}
\quad\Longleftrightarrow\quad
\delta_{Rf_*K}\text{ is an isomorphism}.
$$

Here the dualizing complexes are $a_X^!\Lambda_S$ and $a_Y^!\Lambda_S$.
The braiding compatibility is the hypothesis
`AlgebraicGeometry.Etale.LeftDerivedUpperStarBraided`; the mainline
application supplies it using
`AlgebraicGeometry.Etale.leftDerivedUpperStarBraided`.
