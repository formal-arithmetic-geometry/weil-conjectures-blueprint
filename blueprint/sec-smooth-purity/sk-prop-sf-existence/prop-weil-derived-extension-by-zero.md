+++
id = "prop-weil-derived-extension-by-zero"
kind = "theorem"
title = "The derived extension-by-zero functor"
order = 1837
tags = ["latex:proposition"]
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-extension-by-zero"]
+++
The exact functor $j_!$ of
[def-weil-extension-by-zero] induces, by degreewise application,
an exact triangulated functor

$$
j_!:D(U_{\mathrm{proet}},A)
\longrightarrow D(\overline X_{\mathrm{proet}},A),
$$

and this is the derived functor of
def:weil-derived-pullback-tensor-hom-type operations.

## Proof

The functor $j_!$ of [def-weil-extension-by-zero] is exact, so its
degreewise extension to complexes carries quasi-isomorphisms to
quasi-isomorphisms and preserves the translation and the distinguished
triangles of the homotopy categories: an exact functor of abelian
categories preserves short exact sequences, hence cones and distinguished
triangles. Therefore $j_!$ induces an exact triangulated functor

$$
j_!:D(U_{\mathrm{proet}},A)\longrightarrow
D(\overline X_{\mathrm{proet}},A),
$$

and exactness makes this the derived functor of $j_!$: its
degreewise application is canonical and agrees with the derived functor
computed on any adapted resolution. This is the extension-by-zero
operation of def:weil-derived-pullback-tensor-hom-type for the
open immersion $j$, with the ambient derived categories of
[def-weil-extension-by-zero].
