+++
id = "conventions-coefficient-categories-and-basic-operations"
kind = "section"
title = "Conventions, coefficient categories, and basic operations"
order = 1365
uses = ["def-kun-separably-closed", "def-weil-derived-limit", "def-weil-finite-type-morphism", "def-weil-karoubi-envelope", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-cartesian-square", "def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-direct-image", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-etale-sum-extension", "def-weil-pbc-ind-etale-algebra", "def-weil-pbc-intrinsic-completion", "def-weil-pbc-inverse-image", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-operations", "def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions", "def-weil-scheme-morphism-properties", "def-weil-t-structure", "lem-sp-finite-filtration-induction", "lem-weil-karoubi-envelope-fully-faithful", "lem-weil-karoubi-envelope-triangulated", "lem-weil-pbc-closed-immersion-from-composite", "lem-weil-pbc-derived-cohomology-continuity", "lem-weil-pbc-etale-finite-data-descent", "lem-weil-pbc-etale-restriction-injectives", "lem-weil-pbc-etale-section-continuity", "lem-weil-pbc-finite-reduction-reconstruction", "lem-weil-pbc-flat-lfp-open", "lem-weil-pbc-ind-etale-stability", "lem-weil-pbc-noetherian-finite-components", "lem-weil-pbc-reconstruction-uniform-tower", "lemma-nagata-affine-finite-type-is-quasi-affine", "lemma-openclosed-point-ulift", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-heart-abelian", "prop-weil-pbc-geometric-stalks-exact", "prop-weil-pbc-inverse-image-exact", "prop-weil-pbc-kinjective-resolutions-exist", "prop-weil-pbc-proetale-constant-exact", "prop-weil-pbc-proetale-constant-ring-map", "thm-sp-truncation-e2", "thm-weil-karoubian-bounded-t", "thm-weil-pbc-universal-homeomorphism-invariance", "thm-weil-pbc-weak-etale-refinement"]
+++
This chapter fixes the common language: the arithmetic and geometric
conventions, the coefficient categories at each of the four stages
($A_{E,n}$, $\mathcal O_E$, $E$, $\Qlb$), and the six operations in
triangulated form. The six-functor package and its verification are
collected elsewhere; their placement there does not make them hypotheses
already proved here.

The coefficient tower is built in three steps: finite-torsion coefficients on
the small pro-etale site [def-weil-finite-torsion-constructibility], the
derived-complete integral stage
[def-weil-derived-complete-integral-detailed], and the two field stages
obtained by rationalization [def-weil-rationalization-karoubi] and by the
common-stage construction over all finite subextensions of $\Qlb$
[def-weil-algebraically-closed-coefficients]. Every operation defined in
[the-six-operations-in-triangulated-form] is given first at finite level and
then transported up this tower.

This chapter is chapter 1 of `weil_conjectures_detailed.tex` together with the
construction half of chapter 6, *The pro-etale comparison and coefficient
categories*. Chapter 1 states the tower; chapter 6 builds it, and the two are
interleaved here in dependency order rather than kept apart:

- [the-comparison-of-the-etale-and-pro-etale-sites] is the morphism of sites
and the bounded-below comparison [thm-weil-pbc-site-comparison] that lets a
statement proved on the etale site be read on the pro-etale one.
- [constructible-finiteness-for-the-complete-coefficients] cuts out the
constructible objects and shows they are a weak Serre subcategory
[thm-constructible-serre].
- [rational-coefficient-categories-and-finite-scalar-extensions] and
[truncations-t-structures-and-the-idempotent-complete-l-adic-category] build
the last two stages, ending in the common-stage $\Qlb$ category
[def-weil-pbc-qbar-category] with its t-structures, Verdier axioms and
idempotent completeness. They stand *before*
[rationalization-and-scalar-extension-to-the-algebraically-closed-stage],
which cites them.
- [closed-immersions-on-the-ambient-pro-etale-site] and
[closed-direct-image-and-the-ambient-open-closed-recollement] close the
chapter: the recollement is stated with the six operations, so it stands
after them.

The four theorems of chapter 6 that carry proper base change up this tower are
not here. They are in [chap-proper-base-change], where they continue the
S0--S10 route as its steps S8 and S10--S12. Nothing in this chapter cites
them.

Six of this chapter's identifiers already name objects imported earlier from
the sketch sources; those six carry the suffix `-detailed` here so that the two
readings coexist, as [foundations] records for the part as a whole.
