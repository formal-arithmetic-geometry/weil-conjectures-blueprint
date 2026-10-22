+++
id = "lem-sc-morphism-from-function"
kind = "lemma"
title = "Rational functions define finite morphisms to $\\mathbf P^1$"
lean = ["AlgebraicGeometry.Scheme.isFinite_flat_of_hom_projectiveLine_of_functionField"]
order = 705
uses = ["def-sc-curves", "def-sc-function-field", "lem-sc-dim0-finite", "lem-sc-rational-function-morphism", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular", "thm-pqf-finite-iff-proper-finite-fibres"]
+++
Let $k$ be a field, $C$ an integral scheme, smooth of relative
dimension one and proper over $k$, $f\in k(C)$
([def-sc-function-field]) transcendental over $k$ (for $k$
algebraically closed: $f\in k(C)\setminus k$),
and $\pi_f:C\to\mathbf P^1_k$ the morphism of
[lem-sc-rational-function-morphism]. Then $\pi_f$ is
finite surjective and flat of degree $[k(C):k(f)]$.
