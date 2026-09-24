+++
id = "chap-proper-base-change"
kind = "section"
title = "Proper Base Change"
order = 632
uses = ["def-nagata-projective-space-base-change", "def-sp-composite-acyclicity", "def-sp-convergence", "def-sp-etale-dictionary", "def-sp-exact-couple", "def-sp-truncation-couple", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-complete", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-completed-pullback-detailed", "def-weil-pbc-constructible-complexes", "def-weil-pbc-constructible-direct-image-finiteness", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-direct-image", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-finite-stage-pair-category", "def-weil-pbc-finite-torsors", "def-weil-pbc-geometric-stalks", "def-weil-pbc-henselian-terminology", "def-weil-pbc-injective-acyclicity", "def-weil-pbc-inverse-image", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-proetale-operations", "def-weil-pbc-projection-formula-map", "def-weil-pbc-property-detailed", "def-weil-pbc-qbar-category", "def-weil-pbc-scheme-conventions", "def-weil-pbc-site-comparison-morphism", "def-weil-pbc-strict-henselization-limit-detailed", "def-weil-pbc-underived-exchange-detailed", "lem-sp-couple-morphism", "lem-sp-finite-filtration-induction", "lem-sp-shift-identification", "lem-weil-pbc-closed-immersion-products", "lem-weil-pbc-closed-immersion-proper", "lem-weil-pbc-cohomology-filtered-colimit", "lem-weil-pbc-comparison-pullback", "lem-weil-pbc-completed-pullback-reduction", "lem-weil-pbc-direct-image-filtered-colimit", "lem-weil-pbc-etale-degree-zero", "lem-weil-pbc-etale-finite-data-descent", "lem-weil-pbc-etale-section-continuity", "lem-weil-pbc-exchange-identity-pasting", "lem-weil-pbc-finite-reduction-reconstruction", "lem-weil-pbc-five-lemma-transfer", "lem-weil-pbc-flat-lfp-open", "lem-weil-pbc-geometric-stalk-conservative", "lem-weil-pbc-levelwise-isomorphism-cones", "lem-weil-pbc-noetherian-finite-components", "lem-weil-pbc-prime-factor-devissage", "lem-weil-pbc-proper-closed-image", "lem-weil-pbc-proper-composition", "lem-weil-pbc-proper-immersion-closed", "lem-weil-pbc-proper-to-separated", "lem-weil-pbc-pullback-preserves-bounded-constructible", "lem-weil-pbc-qcqs-higher-direct-image", "lem-weil-pbc-reconstruction-uniform-tower", "lem-weil-pbc-surjective-nonempty-fibres", "lem-weil-pbc-torsion-filtered-union", "lem-weil-pbc-underived-proper-exchange", "lemma-nagata-projective-space-base-change-proper", "prop-weil-pbc-comparison-direct-image", "prop-weil-pbc-descent-functors", "prop-weil-pbc-direct-image-limits", "prop-weil-pbc-geometric-stalks-exact", "prop-weil-pbc-perfect-projection-formula", "prop-weil-pbc-property-iff-acyclicity", "prop-weil-pbc-rational-transport", "prop-weil-pbc-restriction-direct-image", "prop-weil-pbc-strict-henselization-stalk-formula-detailed", "thm-galois-lc-etale", "thm-sp-grothendieck", "thm-sp-grothendieck-base-change", "thm-sp-half-plane-convergence", "thm-sp-truncation-e2", "thm-weil-pbc-etale-cohomology-continuity", "thm-weil-pbc-site-comparison", "thm-weil-pbc-stein-inputs", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Proper base change: for a proper finitely presented $f$ and a Cartesian
square, the exchange map $Lg^*Rf_*K\to Rf'_*Lg'^*K$ is an isomorphism, first
for finite torsion coefficients on the etale site and then for the adic and
$\Qlb$ coefficients of the Weil proof. The chapter is the S0--S12 proof,
in two parts, preceded by its one geometric input from outside the etale
theory.

**[chap-chow-lemma]**: a proper $S$-scheme is dominated by a projective one
[cor-chow-lemma-proper]. Only S3, the reduction to the projective line, cites
it; it depends on nothing in this chapter, only on the projective-space
results of [nagata-compactification], so it stands first.

**[pbc-finite-torsion-etale]** (S0--S7), from chapter 5 of
`weil_conjectures_detailed.tex`:

- S0 [s0.-comparison-data-and-injective-acyclicity], with the
[derived-exchange-comparison-chain] that makes the exchange map well defined
and reduces the base-change property to injective acyclicity
- S1 [s1.-finite-morphisms]
- S2 [s2.-composition-and-proper-surjective-cancellation]
- S3 [s3.-reduction-to-the-projective-line]
- S4 [s4.-the-projective-line-over-a-strictly-henselian-local-base]
- S5 [s5.-the-projective-line-over-an-arbitrary-base]
- S6 [s6.-finite-torsion-proper-base-change]
- S7 [s7.-bounded-below-finite-torsion-complexes]

**[pbc-proetale-and-adic]** (S8--S12), the base-change half of chapter 6:

- S8 [s8.-etale-to-pro-etale-finite-level-transport] --- the comparison of
sites identifies the two exchange maps, so the etale theorem becomes the
pro-etale one
- S9 [s9.-derived-completion-and-inverse-limits]
- S10 [s10.-complete-pro-etale-proper-base-change] --- assembling the finite
levels into the completed comparison
- S11 [s11.-proper-base-change-over-a-finite-extension]
- S12 [s12.-qbar-proper-base-change]

Inside each step, the objects directly under the step are its statements;
the subsections under it are the detailed argument that realizes them. Where
the two state the same thing the titles agree, as with
[prop-weil-pbc-finite-morphism] and [prop-weil-pbc-finite-morphisms], or
[prop-weil-proet-finite-proper-base-change] and [thm-weil-pbc-finite-torsion].

The construction half of chapter 6 --- the comparison of sites, the
constructible finiteness, the rational and $\Qlb$ categories, the recollement
--- is in [conventions-coefficient-categories-and-basic-operations] of
[foundations], because it builds the categories rather than transporting base
change through them. The split is one-way: this chapter cites that one, never
the reverse.

The detailed chapter proves the projective line (S4, S5) before the
reduction to it is used; the reduction (S3) is stated as an implication, so
no step cites a later one. One label of the detailed source remains
unresolved, `thm:sc-main` in the curve part. The other,
`lem:weil-pbc-finite-locally-constant-etale`, is a second label of
[thm-galois-lc-etale] in
[finite-etale-covers-the-fibre-functor-and-the-fundamental-group].
