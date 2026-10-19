+++
id = "lem-per-smooth-pullback-t-exact"
kind = "lemma"
title = "Smooth pullback is perverse up to the shift"
lean = ["AlgebraicGeometry.Etale.DerivedCategory.isPerverseLE_upperStar", "AlgebraicGeometry.Etale.DerivedCategory.isPerverseGE_upperStar"]
order = 3086
uses = ["cor-pur-adic-and-rational-smooth-dualizing-complexes", "cor-sf-duality-pullback", "def-per-perverse-subcategories", "def-per-support-condition", "sk-def-sfb-bounded-constructible", "def-weil-pbc-scheme-conventions", "fix-cor-verdier-exchange", "lem-per-lisse-tensor-permanence", "prop-functor-package"]
+++
Let $f:X\to Y$ be a smooth
morphism of constant relative dimension $d$ between separated schemes
of finite type over a field $k$. On the bounded constructible categories
$\Dbc(-,\Qlb)$ of [sk-def-sfb-bounded-constructible], the functor $Lf^*[d]$ is exact for
the candidate subcategories of [def-per-perverse-subcategories]:

$$
Lf^*[d]\bigl({}^pD^{\le0}(Y)\bigr)\subset{}^pD^{\le0}(X),\qquad
Lf^*[d]\bigl({}^pD^{\ge0}(Y)\bigr)\subset{}^pD^{\ge0}(X).
$$
