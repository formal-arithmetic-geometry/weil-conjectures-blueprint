+++
id = "lem-per-smooth-pullback-t-exact"
kind = "lemma"
title = "Smooth pullback is perverse up to the shift"
order = 3986
uses = ["cor-pur-adic-and-rational-smooth-dualizing-complexes", "def-per-perverse-subcategories", "def-per-support-condition", "det-def-sfb-bounded-constructible", "def-weil-pbc-scheme-conventions", "def-weil-derived-pullback-tensor-hom", "fix-prop-adjunctions", "fix-prop-projection-formula", "thm-sf-comp-composition", "lem-per-lisse-tensor-permanence", "prop-functor-package"]
+++
Let $f:X\to Y$ be a smooth
morphism of constant relative dimension $d$ between separated schemes
of finite type over a field $k$. On the bounded constructible categories
$\Dbc(-,\Qlb)$ of [det-def-sfb-bounded-constructible], the functor $Lf^*[d]$ is exact for
the candidate subcategories of [def-per-perverse-subcategories]:

$$
Lf^*[d]\bigl({}^pD^{\le0}(Y)\bigr)\subset{}^pD^{\le0}(X),\qquad
Lf^*[d]\bigl({}^pD^{\ge0}(Y)\bigr)\subset{}^pD^{\ge0}(X).
$$
