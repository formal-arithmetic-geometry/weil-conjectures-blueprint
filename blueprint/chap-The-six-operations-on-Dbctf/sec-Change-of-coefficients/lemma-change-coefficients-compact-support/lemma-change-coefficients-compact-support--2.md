+++
id = "lemma-change-coefficients-compact-support--2"
kind = "lemma"
title = "Change of coefficients for compactly supported direct image (2)"
name_showing = false
order = 637002
aliases = ["bp-r194-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.BoundedConstructibleCoefficientChange.squareCompatible_lowerShriekOfCompactificationIso"]
uses = ["definition-constructible-sheaves", "definition-change-of-coefficients-maps", "definition-compactification-refinement", "proposition-construction-independence-rf-shriek"]
+++
Let $\ell$ be a prime and $k$ a field of characteristic $p>0$ with
$p\ne\ell$. Let $\Lambda,\Lambda'$ be commutative condensed rings.
On the bounded constructible categories of separated schemes of finite
type over $k$, suppose that direct-image functors $Rg_*$ with adjunctions
$g^*\dashv Rg_*$ have been given for both coefficient rings.

Suppose also that functors
$T_X:\Dbc(X,\Lambda)\to\Dbc(X,\Lambda')$ are given, together with
isomorphisms commuting with pullback, extension by zero along open
immersions, and direct image along proper morphisms. Assume that the
pullback comparisons respect composition, and that the other two
comparisons correspond to the pullback comparisons under the adjunctions
$j_!\dashv j^*$ and $p^*\dashv Rp_*$, respectively, as in
Definition [definition-change-of-coefficients-maps](2),(4).
For both coefficient rings, assume that the canonical maps
$j_{1!}\to Rh_*j_!$ are isomorphisms whenever $h$ is proper,
$hj=j_1$, and the square with the identity of the open subscheme is
cartesian.

Let $c_1,c_2$ be compactifications of $f:X\to Y$, and let
$\alpha_\Lambda:Rf_!^{c_1}\xrightarrow{\sim}Rf_!^{c_2}$ and
$\alpha_{\Lambda'}$ be the isomorphisms through the chosen common
refinement of
Proposition [proposition-construction-independence-rf-shriek].
For each compactification $c$, compose the proper direct-image and
extension-by-zero comparisons to obtain
$$
\gamma_{c,K}:T_Y(Rf_!^cK)\xrightarrow{\ \sim\ }Rf_!^c(T_XK).
$$
Then these comparisons commute with the independence isomorphisms:
$$
\alpha_{\Lambda',T_XK}\circ\gamma_{c_1,K}
=\gamma_{c_2,K}\circ T_Y(\alpha_{\Lambda,K}).
$$
Thus the coefficient comparison is independent of the compactification
under these identifications.
