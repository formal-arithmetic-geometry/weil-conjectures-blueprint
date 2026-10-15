+++
id = "lem-pbc-h2-integral-open-extension-comparison"
kind = "lemma"
title = "Integral encoding commutes with open extension by zero"
uses = ["def-weil-pbc-extension-by-zero", "def-weil-pbc-inverse-image"]
lean = ["AlgebraicGeometry.Etale.integral_open_extension_comparison"]
+++
For any scheme X and abelian etale sheaf A `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), let E be the canonical equivalence from abelian groups to modules over ULift Z, obtained by the inverse of the forgetful Z-module equivalence and restriction along ULift Z = Z. For any open inclusion j:U -> X [def-weil-pbc-extension-by-zero], E(j_!j^*A) is isomorphic to j_!j^*E(A) [def-weil-pbc-inverse-image]. No curve, density, torsion or constructibility hypothesis is required.
