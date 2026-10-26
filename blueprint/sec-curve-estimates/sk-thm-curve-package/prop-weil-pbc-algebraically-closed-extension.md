+++
id = "prop-weil-pbc-algebraically-closed-extension"
kind = "theorem"
title = "Algebraically closed extension for proper curves"
lean = ["AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_isAlgClosed"]
order = 1312
uses = ["def-weil-pbc-eight-curve-assertions", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-curve-constructible-reduction", "lem-weil-pbc-curve-dense-open-localization", "lem-weil-pbc-zero-dimensional-field-extension", "lemma-weil-pbc-curve-filtered-cohomology", "lemma-weil-pbc-curve-locally-constant-reduction", "lemma-weil-pbc-eight-curve-devissage", "lemma-weil-pbc-finite-l-group-filtration", "lemma-weil-pbc-finite-pushforward-extension-zero", "lemma-weil-pbc-normalization-exact-sequence", "thm-sc-main"]
tags = ["latex:proposition"]
+++
Let $k\subset k'$ be algebraically closed, let $C$ be proper of dimension at
most one over $k$, and let $F$ be a torsion etale sheaf. Then

$$
 H^q(C,F)\xrightarrow{\sim}H^q(C_{k'},F|_{C_{k'}})
 \qquad(q\geq0).
$$
