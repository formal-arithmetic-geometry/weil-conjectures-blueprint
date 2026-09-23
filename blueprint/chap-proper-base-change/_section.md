+++
id = "chap-proper-base-change"
kind = "section"
title = "Proper Base Change"
order = 631
uses = ["cor-chow-lemma-proper", "def-nagata-projective-space-base-change", "def-sp-composite-acyclicity", "def-sp-convergence", "def-sp-etale-dictionary", "def-sp-exact-couple", "def-sp-truncation-couple", "def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-direct-image", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "def-weil-pbc-henselian-terminology", "def-weil-pbc-injective-acyclicity", "def-weil-pbc-inverse-image", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-property-detailed", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit-detailed", "def-weil-pbc-underived-exchange-detailed", "lem-sp-couple-morphism", "lem-sp-finite-filtration-induction", "lem-sp-shift-identification", "lem-weil-pbc-closed-immersion-products", "lem-weil-pbc-closed-immersion-proper", "lem-weil-pbc-cohomology-filtered-colimit", "lem-weil-pbc-direct-image-filtered-colimit", "lem-weil-pbc-etale-degree-zero", "lem-weil-pbc-etale-finite-data-descent", "lem-weil-pbc-etale-section-continuity", "lem-weil-pbc-exchange-identity-pasting", "lem-weil-pbc-five-lemma-transfer", "lem-weil-pbc-geometric-stalk-conservative", "lem-weil-pbc-prime-factor-devissage", "lem-weil-pbc-proper-closed-image", "lem-weil-pbc-proper-composition", "lem-weil-pbc-proper-immersion-closed", "lem-weil-pbc-proper-to-separated", "lem-weil-pbc-qcqs-higher-direct-image", "lem-weil-pbc-torsion-filtered-union", "lem-weil-pbc-underived-proper-exchange", "lemma-nagata-projective-space-base-change-proper", "prop-weil-pbc-geometric-stalks-exact", "prop-weil-pbc-property-iff-acyclicity", "prop-weil-pbc-strict-henselization-stalk-formula-detailed", "thm-chow-lemma", "thm-sp-grothendieck", "thm-sp-grothendieck-base-change", "thm-sp-half-plane-convergence", "thm-sp-truncation-e2", "thm-weil-pbc-etale-cohomology-continuity", "thm-weil-pbc-stein-inputs", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Proper base change, in two readings that now sit in one tree.

The **route** is the S0--S10 spine of
[target-scope-and-proof-spine] and [ordered-dependency-spine], imported from
the sketch sources: it names the ten steps, states each one, and records in
[app-gap-ledger] and [imported-dependency-registry] exactly which inputs are
admitted rather than proved.

The **detailed realization** of steps S1--S7 is chapter 5 of
`weil_conjectures_detailed.tex`, merged in here as eighteen subsections, each
filed under the S-step it realizes:

- S1 [finite-morphisms]
- S2 [composition-and-proper-surjective-cancellation]
- S3 [scheme-theoretic-closure-and-affine-covers-of-the-generic-points],
[the-segre-product-model-and-its-glued-proper-surjection],
[spreading-out-chow-s-theorem-and-the-embedding-over-the-source],
[reduction-to-the-projective-line],
[symmetric-product-coordinates-and-the-reduction-of-projective-space]
- S4 [the-projective-line-over-a-strictly-henselian-base],
[finite-stage-killing-lisse-strata-and-generic-stalk-tests],
[constructibility-of-finite-pushforwards-and-gabber-s-comparison],
[finite-torsors-finite-etale-lifting-and-degree-one-classes],
[cohomology-comparison-and-strict-local-exchange-on-the-line]
- S5 [the-projective-line-over-an-arbitrary-base],
[the-eight-curve-assertions-on-cohomology-base-change],
[devissage-and-reduction-of-the-eight-curve-assertions],
[geometric-stalk-exchange-and-the-projective-line-comparison]
- S6 [finite-torsion-proper-base-change]
- S7 [bounded-below-torsion-complexes]

The S-step statements of the route and the detailed statements that realize
them are separate objects: the route's are the coarse reading the ledger is
written against, the detailed ones carry the proofs. Where the two state the
same thing the titles agree, as with [prop-weil-pbc-finite-morphism] and
[prop-weil-pbc-finite-morphisms], or [prop-weil-proet-finite-proper-base-change]
and [thm-weil-pbc-finite-torsion].

Two things the merge does not supply. S8--S10 --- the transport to the
pro-etale site, derived completion, and the complete pro-etale comparison ---
have no counterpart in chapter 5; they are chapter 6 of the detailed source
and are not imported yet, so those three steps still stand on the route's own
statements alone. And the detailed chapter's own order differs from the
route's numbering in one place: it proves the projective line first and
performs the reduction to it afterwards. The reduction is stated as an
implication, so filing it under S3 introduces no forward reference; the
subsections of this chapter read in an order in which nothing cites anything
later.

Every statement merged in is stated over the ambient etale-site language of
[foundations], and cites it: 344 `uses` edges from these eighteen subsections
land in [ambient-categories-sites-and-the-comparison-framework] and
[spectral-sequence-machinery], on 53 distinct objects. Two labels of the
detailed source remain unresolved, `thm:sc-main` in the curve part and
`lem:weil-pbc-finite-locally-constant-etale`, which the source never defines.
