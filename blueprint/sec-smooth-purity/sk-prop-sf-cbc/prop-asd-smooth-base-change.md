+++
id = "prop-asd-smooth-base-change"
kind = "theorem"
title = "Arbitrary base change for smooth ambient duality"
order = 1577
tags = ["latex:proposition"]
uses = ["cor-amb-affine-space-adjunction", "def-sbc-smooth-morphisms", "def-weil-derived-pullback-tensor-hom", "def-weil-pbc-derived-categories", "lem-amb-cartier-kummer-map", "lem-amb-etale-adjoint-locality", "lem-amb-proper-coproducts-projection", "thm-amb-etale-exceptional-adjoint", "thm-amb-p1-adjunction", "thm-amb-p1-decomposition", "thm-asd-smooth-tensor"]
+++
Let $f:X\to S$ be as in
[thm-asd-smooth-tensor], and let $g:S'\to S$
be any morphism of Noetherian schemes. Denote its base
change by $f':X'\to S'$, with $g':X'\to X$.
The canonical morphism

$$
g'^*f^\times K\longrightarrow f'^\times g^*K
$$

is an isomorphism for every complex $K$. At $K=A$
it identifies $g'^*\omega_f$ with $\omega_{f'}$,
and it respects the tensor isomorphism of
[thm-asd-smooth-tensor].
