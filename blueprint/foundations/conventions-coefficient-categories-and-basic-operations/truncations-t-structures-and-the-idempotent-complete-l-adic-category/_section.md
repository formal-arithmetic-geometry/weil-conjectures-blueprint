+++
id = "truncations-t-structures-and-the-idempotent-complete-l-adic-category"
kind = "section"
title = "Truncations, t-structures and the idempotent-complete l-adic category"
order = 1344
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-karoubi-envelope", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-complete", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-intrinsic-completion", "def-weil-pbc-rational-category", "def-weil-t-structure", "lem-weil-karoubi-envelope-fully-faithful", "lem-weil-karoubi-envelope-triangulated", "lem-weil-pbc-finite-reduction-reconstruction", "lem-weil-pbc-reconstruction-uniform-tower", "prop-weil-pbc-scalar-extension", "thm-weil-karoubian-bounded-t"]
+++
Three subsections of the source are flattened here.

*The standard t-structure on the integral categories.* Levelwise canonical
truncation of an adic tower is again an adic tower exactly when a
Tor-compatibility condition holds above the truncation level; the source
carries that condition as an explicit hypothesis and exhibits a
counterexample showing it is not automatic
[prop-weil-pbc-levelwise-truncations]. Taking derived limits gives the
truncation functors of the integral category with their reductions,
cohomology and triangles [thm-weil-pbc-integral-truncations], hence a
bounded t-structure [prop-weil-pbc-integral-tstructure].

*Idempotent completeness of the rational categories.* The t-structure
descends to $\Dbc(T,E)$ with the localization functor t-exact
[prop-weil-localized-tstructure], and a triangulated category with a bounded
t-structure is Karoubian, so each finite stage is idempotent complete
[thm-weil-pbc-finite-stage-karoubian].

*The $\Qlb$ coefficient colimit.* The pair category $\mathcal P_T$ over the
filtered poset of finite $E/\Ql$ [def-weil-pbc-finite-stage-pair-category] is
additive with a common-stage calculus [prop-weil-pbc-common-stage-calculus],
its distinguished triangles are common-stage cone triangles
[def-weil-pbc-common-stage-cones], well defined
[prop-weil-pbc-cone-independence], and satisfying the Verdier axioms
[thm-weil-pbc-verdier-axioms]. Idempotents split over a single stage
[prop-weil-filtered-retract-descent], so $\Dbc(T,\Qlb):=\mathcal P_T$
[def-weil-pbc-qbar-category] is idempotent complete
[thm-weil-pbc-qbar-idempotent-complete],
[rem-ptr-weil-pbc-qbar-category-1] and triangulated over $\Qlb$
[thm-weil-pbc-idempotent-complete-triangulation]. Scalar-compatible families
of functors descend [prop-weil-pbc-descent-functors], which gives $\Qlb$
proper base change [thm-weil-pbc-qbar] and its geometric-fibre form
[cor-weil-pbc-geometric-fiber-qbar].
