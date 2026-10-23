+++
id = "lem-weil-pbc-finite-separable-multiplication-etale"
kind = "lemma"
title = "Multiplication of a finite separable extension is etale"
lean = ["Algebra.FormallyEtale.of_isSeparable", "Algebra.FormallyUnramified.isOpenImmersion_SpecMap_lmul", "AlgebraicGeometry.HasRingHomProperty.Spec_iff"]
order = 1794
+++
Let $k'/k$ be a field extension which is finite ($\dim_kk'<\infty$) and separable algebraic. Let $\mu:k'\otimes_kk'\to k'$, $a\otimes b\mapsto ab$, be the multiplication map. Then $\operatorname{Spec}\mu:\operatorname{Spec}k'\to\operatorname{Spec}(k'\otimes_kk')$ is etale; in particular $\mu$ is a smooth ring map.
