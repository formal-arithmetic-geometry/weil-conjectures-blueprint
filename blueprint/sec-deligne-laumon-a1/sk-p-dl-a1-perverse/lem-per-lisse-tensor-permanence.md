+++
id = "lem-per-lisse-tensor-permanence"
kind = "lemma"
title = "Permanence under a lisse tensor"
lean = ["AlgebraicGeometry.Etale.DerivedCategory.SupportCondition.tensor", "AlgebraicGeometry.Etale.DerivedCategory.isPerverseLE_tensor", "AlgebraicGeometry.Etale.DerivedCategory.isPerverseGE_tensor"]
order = 3085
uses = ["def-per-perverse-subcategories", "def-per-support-condition", "sk-def-sfb-bounded-constructible", "sk-lem-coefficient-heart", "def-weil-pbc-scheme-conventions", "lem-per-dual-lisse-tensor"]
+++
Let $X$ be smooth of pure
dimension $d$, let $K\in D^b_c(X,\overline{\mathbf Q}_\ell)$
([sk-def-sfb-bounded-constructible]) and let $\mathcal L$ be a lisse
$\overline{\mathbf Q}_{\ell,X}$-module ([sk-lem-coefficient-heart]). Then

$$
K\in{}^pD^{\le0}(X)\ \Longrightarrow\
K\otimes^L\mathcal L\in{}^pD^{\le0}(X),
\qquad
K\in{}^pD^{\ge0}(X)\ \Longrightarrow\
K\otimes^L\mathcal L\in{}^pD^{\ge0}(X),
$$

and the analogous assertions hold for the shifted subcategories.
