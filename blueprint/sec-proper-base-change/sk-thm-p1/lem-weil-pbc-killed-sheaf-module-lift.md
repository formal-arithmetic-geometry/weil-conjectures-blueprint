+++
id = "lem-weil-pbc-killed-sheaf-module-lift"
kind = "lemma"
title = "Lift an annihilated abelian sheaf to constant-ring-valued module sheaves"
uses = ["def-weil-pbc-cohomology-pullback", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.exists_module_sheaf_of_nsmul_id_eq_zero"]
order = 1871
+++
Let $X$ be a scheme [def-weil-pbc-scheme-conventions], $n\geq0$, and $G$ an abelian sheaf on its small etale site. If $n\operatorname{id}_G=0$, then there exists a sheaf $M$ of $\mathbf Z/n\mathbf Z$-modules on the small etale site of $X$ [def-weil-pbc-etale-sheaves] whose underlying abelian sheaf is isomorphic to $G$.
