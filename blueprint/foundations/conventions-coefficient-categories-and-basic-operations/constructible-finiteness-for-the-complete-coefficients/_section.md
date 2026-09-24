+++
id = "constructible-finiteness-for-the-complete-coefficients"
kind = "section"
title = "Constructible finiteness for the complete coefficients"
order = 1476
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-constructible-complexes", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-etale-site", "def-weil-pbc-intrinsic-completion", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-operations", "def-weil-pbc-scheme-conventions", "def-weil-pbc-site-comparison-morphism", "lem-sp-finite-filtration-induction", "lem-weil-pbc-comparison-pullback", "lem-weil-pbc-flat-lfp-open", "lem-weil-pbc-noetherian-finite-components", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-comparison-direct-image", "prop-weil-pbc-geometric-stalks-exact", "prop-weil-pbc-inverse-image-exact", "thm-constructible-serre", "thm-sp-truncation-e2"]
+++
The complete proper base-change theorem of the previous section is cut down
to the bounded constructible complete category
[def-weil-pbc-bounded-constructible-complete]. The hypotheses are isolated
as three named predicates on a square: the finiteness and amplitude
condition $\mathrm{FIN}(u,\Lambda;c)$
[def-weil-pbc-constructible-direct-image-finiteness], the amplification
condition $\mathrm{AMP}(\square;c)$
[def-weil-pbc-finite-level-amplification] with its four containments
`prop-weil-pbc-amplification-consequences`, the witness compatibility
$\mathrm{WIT}(\square)$ [def-weil-pbc-witness-compatibility] and the tower
preservation $\mathrm{TOW}(\square)$ [def-weil-pbc-tower-preservation].
$\mathrm{FIN}$ makes $Ru_*$ restrict with an amplitude shift by $c$
[prop-weil-pbc-restriction-direct-image], resting on the weak Serre property
of constructible sheaves [thm-constructible-serre] and its
Noetherian subobject refinement
[lem-weil-pbc-constructible-subobjects-noetherian]; pullback preserves the
interval outright [lem-weil-pbc-pullback-preserves-bounded-constructible].
A proper morphism with geometric fibres of dimension at most $e$ satisfies
$\mathrm{FIN}(f,\Lambda;2e)$ [thm-weil-pbc-direct-image-finiteness-proper],
hence all three predicates hold for a proper square
[thm-weil-pbc-amplification-proper], all four objects of the square stay
bounded constructible complete [prop-weil-pbc-preservation-constructible],
and the base-change isomorphism restricts
[cor-weil-pbc-constructible-complete], including in the geometric-fibre form
`cor-weil-pbc-geometric-fiber-complete`.
