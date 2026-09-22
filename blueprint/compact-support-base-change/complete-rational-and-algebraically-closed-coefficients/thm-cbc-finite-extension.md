+++
id = "thm-cbc-finite-extension"
kind = "theorem"
title = "Compact-support base change over a finite extension"
order = 6626
lean = ["AlgebraicGeometry.Proetale.compactSupportExchange_isIso_finiteExtension"]
uses = ["prop-finite-compact-support-constructibility", "def-cbc-compact-support-square", "thm-cbc-complete-proetale"]
+++
For every finite $E/\Ql$, every compact-support base-change square
([def-cbc-compact-support-square]) with $f$ separated of finite type and $g$
arbitrary, and every $K\in\Dbc(X,E)$ (in the sense of the rational category),
whose reductions satisfy the constructibility and amplitude conditions of the
finite-coefficient compact-support constructibility statement,
$$
 Lg^*Rf_!K\xrightarrow{\ \sim\ }Rf'_!Lg'^*K
 \quad\text{in }\Dbc(Y',E).
$$
This is independent of the integral lattice and natural and coherent for
identities and pasted squares.

## Proof

Choose an integral lattice for $K$. The isomorphism of
[thm-cbc-complete-proetale] is an isomorphism of $\mathcal O_E$-linear
functors on the integral constructible categories, so by the rational
transport proposition it remains an isomorphism after rationalization; the
constructible landing is the finite-level condition of the statement.
Independence and coherence are inherited from the integral level.

Unresolved dependencies: def:weil-pbc-rational-category, prop:weil-pbc-rational-transport
