+++
id = "thm-cbc-finite-torsion"
kind = "theorem"
title = "Compact-support base change at finite coefficients"
order = 6611
lean = ["AlgebraicGeometry.Etale.compactSupportExchange_isIso"]
uses = ["def-compact-support-direct-image", "prop-compactification-coherence", "thm-nagata-compactification", "def-cbc-exchange-map", "def-cbc-compact-support-square", "cor-cbc-derived-extension-zero-base-change"]
+++
Let $\square$ be a compact-support base-change square
([def-cbc-compact-support-square]) with $f:X\to Y$ separated of finite type,
let $\Lambda$ be a finite commutative ring and let $g:Y'\to Y$ be arbitrary.
For every
$$
 K\in D^+(X_{\Et},\Lambda)
$$
the exchange map ([def-cbc-exchange-map])
$$
 \Ex_!(K):g^{-1}Rf_!K\xrightarrow{\ \sim\ }
 Rf'_!g'^{-1}K
$$
is an isomorphism in $D^+(Y'_{\Et},\Lambda)$; it is natural in $K$, is the
identity for identity base changes, and satisfies horizontal and vertical
pasting after inserting the canonical associativity isomorphisms. It is
independent of the chosen compactification.

## Proof

Fix a compactification $c=(j,p)$ of $f$ with base change $c'=(j',p')$ as
in [def-cbc-compact-support-square]. The map $\Ex_!(K)$ of
[def-cbc-exchange-map] is the composite
$$
 \begin{aligned}
 g^{-1}Rf_!K&=g^{-1}Rp_*j_!K
 &&\text{(definitions)}\\
 &\xrightarrow{\ \sim\ }Rp'_*g^{-1}j_!K
 &&\text{(proper base change applied to the proper }p)\\
 &\xrightarrow{\ \sim\ }Rp'_*j'_!g'^{-1}K
 &&\text{([cor-cbc-derived-extension-zero-base-change])}\\
 &=Rf'_!g'^{-1}K &&\text{(definitions).}
 \end{aligned}
$$
The first arrow is an isomorphism by the bounded-below proper base change of
the proper-base-change chapter ($p$ is proper, $g$ arbitrary,
$j_!K\in D^+(X_{\Et},\Lambda)$ because $j_!$ is exact), the second by the
extension-by-zero base change of
[cor-cbc-derived-extension-zero-base-change] applied to the open-immersion
square with $g_U=g'$ (the square of [def-cbc-compact-support-square] is
cartesian, so $X'=U\times_{\overline X}\overline X'$ and the identification
$j'_!g'^{-1}K$ is the one of [def-cbc-exchange-map]). Hence $\Ex_!(K)$ is an
isomorphism for the chosen compactification.

For another compactification $c_1$ with a refinement to $c_2$, the comparison
isomorphisms of the compact-support direct image commute with the two
displayed factors by the coherence of compactifications (the comparison of
$Rf_!$ is $Ru_*j_{1!}\xrightarrow{\sim}j_{2!}$ composed with the composition
isomorphism of proper direct images, and both factors of $\Ex_!$ are
compatible with the refinement maps, as the refined data are cartesian over
the same base change and the maps are mates of compatible data); hence
$\Ex_!(K)$ is independent of the compactification. Naturality in $K$, the
identity for identity base changes, and the pasting laws follow from the
corresponding properties of the two factors (the proper exchange and the
extension-by-zero comparison of
[cor-cbc-derived-extension-zero-base-change]), which is the statement of
[def-cbc-exchange-map].

Unresolved dependencies: def:weil-pbc-derived-categories, def:weil-pbc-etale-sheaves, def:weil-compactifications-refinements, thm:weil-pbc-bounded-below
