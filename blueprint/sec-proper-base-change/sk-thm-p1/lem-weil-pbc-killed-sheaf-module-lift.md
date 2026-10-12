+++
id = "lem-weil-pbc-killed-sheaf-module-lift"
kind = "lemma"
title = "Lift an annihilated abelian sheaf to constant-ring-valued module sheaves"
uses = ["def-weil-pbc-cohomology-pullback", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.exists_module_sheaf_of_nsmul_id_eq_zero"]
source = "https://stacks.math.columbia.edu/tag/095T, First step of the parent proof: sectionwise module structure; construction implicit in Tag 03RW"
+++
Let $X$ be a scheme [def-weil-pbc-scheme-conventions], $n\geq0$, and $G$ an abelian sheaf on its small etale site `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)). If $n\operatorname{id}_G=0$, then there exists a sheaf $M$ valued in $\operatorname{Mod}(\operatorname{ULift}(\mathbf Z/n))$ [def-weil-pbc-etale-sheaves] whose underlying abelian sheaf is isomorphic to $G$.
