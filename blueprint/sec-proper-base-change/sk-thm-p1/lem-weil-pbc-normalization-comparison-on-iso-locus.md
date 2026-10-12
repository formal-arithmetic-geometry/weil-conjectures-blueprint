+++
id = "lem-weil-pbc-normalization-comparison-on-iso-locus"
kind = "lemma"
title = "Normalization comparison objects on the isomorphism locus"
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-extension-by-zero", "def-weil-pbc-inverse-image"]
lean = ["AlgebraicGeometry.normalization_comparison_on_iso_locus"]
source = "literature/blueprint/master/blueprint/sec-proper-base-change/sk-thm-p1/lemma-weil-pbc-normalization-exact-sequence.md, Proof sketch: cokernel constructibility and vanishing over the isomorphism locus; arbitrary-mono generalization justified by finite stalks"
+++
Let Λ be a commutative ring, ℓ any natural number, ν:X′→X a finite morphism of schemes, and V an open of X such that ν restricted over V is an isomorphism. Let j:U→X and j′:U′→X′ be open immersions with ν′:U′→U giving a Cartesian square j′ν = ν′j. Set R = Λ/(ℓ). Then V^*(j_! R_U) and V^*(ν_*j′_!R_U′) are isomorphic as Λ-module sheaves, using inverse image [def-weil-pbc-inverse-image], extension by zero [def-weil-pbc-extension-by-zero], and direct image [def-weil-pbc-direct-image]. No comparison morphism is specified.
