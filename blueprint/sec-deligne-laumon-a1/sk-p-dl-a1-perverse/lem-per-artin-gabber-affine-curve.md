+++
id = "lem-per-artin-gabber-affine-curve"
kind = "lemma"
title = "Affine pushforward is perverse up to the relative dimension"
order = 3987
uses = ["def-per-perverse-subcategories", "def-weil-derived-cohomology-sheaves", "def-weil-open-closed-recollement", "det-def-sfb-bounded-constructible", "def-weil-pbc-scheme-conventions", "fix-cor-verdier-exchange", "lem-sc-cohomological-dimension", "sk-thm-sf-ctf-stability", "sk-thm-sfb-shriek-base-change", "sk-lem-coefficient-heart", "sk-thm-sfb-qlbar-two-colimit", "sk-lem-stratified-lattice", "sk-prop-scalar-six", "sk-prop-integral-criterion", "def-pe-derived-complete", "lem-weil-pbc-mittag-leffler", "sbc-thm-finiteness-finite-type", "prop-sf-open-closed-triangle-all-stages"]
+++
Let $f:X\to Y$ be an
affine morphism of finite
type between separated schemes of finite type over a field $k$,
whose geometric fibers have dimension at most $d$ (the instance used
here is $d=1$: the projection
$p_2:\mathbf A^1_{k_0}\times\mathbf A^1_{k_0}\to\mathbf A^1_{k_0}$
and its base changes). Then, for the perverse subcategories of
$\Dbc(-,\Qlb)$ ([det-def-sfb-bounded-constructible], [def-per-perverse-subcategories]),

$$
Rf_!\bigl({}^pD^{\le0}(X)\bigr)\subset{}^pD^{\le d}(Y),\qquad
Rf_!\bigl({}^pD^{\ge0}(X)\bigr)\subset{}^pD^{\ge -d}(Y).
$$

In the relative-dimension-one instance the $!$-pushforward is exact
for the perverse subcategories up to the shift by one.
