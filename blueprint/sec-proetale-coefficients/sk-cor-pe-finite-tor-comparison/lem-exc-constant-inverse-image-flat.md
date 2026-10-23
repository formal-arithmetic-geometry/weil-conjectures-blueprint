+++
id = "lem-exc-constant-inverse-image-flat"
kind = "lemma"
title = "Constant-coefficient inverse image preserves flat sheaves"
lean = ["CategoryTheory.flat_sheafPullback_obj", "AlgebraicGeometry.ProEtale.flat_comparisonUpperStar_obj", "AlgebraicGeometry.ProEtale.preservesFlat_comparisonUpperStar"]
order = 1055
uses = ["def-weil-derived-tensor", "def-weil-pbc-proetale-operations", "def-weil-pbc-site-comparison-morphism", "prop-weil-pbc-site-comparison-finite-level"]
+++
For a Noetherian commutative coefficient ring $A$, for instance a finite one, the
site inverse
image $\nu_T^*$ takes flat etale $A$-module sheaves
to flat pro-etale $A$-module sheaves. Flat means that
the ordinary tensor
product with the sheaf preserves injections of module sheaves.
