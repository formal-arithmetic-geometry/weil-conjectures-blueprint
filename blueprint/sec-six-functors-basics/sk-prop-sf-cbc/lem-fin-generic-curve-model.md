+++
id = "lem-fin-generic-curve-model"
kind = "lemma"
title = "A generic curve model with finite comparison boundary"
lean = ["AlgebraicGeometry.exists_isFinite_sigmaDesc_genericCurveModel"]
order = 2723
uses = ["def-pc-projective-morphism", "def-sbc-smooth-morphisms", "def-weil-pbc-scheme-conventions", "lem-fin-finite-over-projective", "lem-fin-normalization-extension-finite", "lem-fin-projective-generically-finite", "lem-fin-spread-finite-algebra", "lem-sc-normalized-curve-smooth", "lem-weil-pbc-proper-closed-image"]
+++
Let $f:X\to S$ be
projective, with $S$ integral
of finite type over a field, and with geometric fibres of dimension
at most one. After restricting $S$ to a nonempty open, there is a
finite surjection $p:S'\to S$ with $S'$ integral, and a finite
surjection

$$
\nu:Y\longrightarrow T=(X\times_S S')_{\mathrm{red}},
$$

where $Y$ is a finite disjoint union of
smooth projective families of
pure relative dimension one and finite etale families.
Moreover $\nu$ is an isomorphism outside a closed
$D\subset T$ finite over $S'$.
