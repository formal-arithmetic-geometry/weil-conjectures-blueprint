+++
id = "lem-weil-pbc-finite-pushforward-open-quotient-constant"
kind = "lemma"
title = "Constructibility of finite pushforward of an open quotient constant"
uses = ["def-constructible-constructible", "def-weil-pbc-direct-image", "def-weil-pbc-extension-by-zero"]
lean = ["AlgebraicGeometry.finite_pushforward_open_constantModSheaf_constructible"]
source = "literature/blueprint/master/blueprint/sec-proper-base-change/sk-thm-p1/lemma-weil-pbc-normalization-exact-sequence.md, Proof sketch: cokernel constructibility and vanishing over the isomorphism locus; arbitrary-mono generalization justified by finite stalks"
+++
Let Λ be a commutative ring, ℓ a natural number such that R = Λ/(ℓ) is finite as a set, X a Noetherian scheme, ν:Y→X a finite morphism, and j:U→Y an open immersion. Then ν_*j_! of the constant Λ-module sheaf R on U is constructible [def-constructible-constructible], using direct image [def-weil-pbc-direct-image] and extension by zero [def-weil-pbc-extension-by-zero].
