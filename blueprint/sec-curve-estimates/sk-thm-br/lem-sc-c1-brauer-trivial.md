+++
id = "lem-sc-c1-brauer-trivial"
kind = "lemma"
title = "The Brauer group of a $C_1$ field"
lean = ["IsQuasiAlgClosed.finrank_eq_one_of_isCentral", "IsQuasiAlgClosed.subsingleton_brauerGroup", "IsQuasiAlgClosed.subsingleton_cohomologicalBrauerGroup", "Algebra.IsCentral.exists_algEquiv_matrix_of_isSepClosed", "Algebra.IsCentral.exists_unit_map_eq_conj", "Algebra.IsCentral.exists_isHomogeneous_eval_ne_zero", "IsQuasiAlgClosed.exists_eq_of_isHomogeneousCocycle", "AlgebraicGeometry.Scheme.GaloisCech.exactAt_two_cechComplex_gmSheaf"]
order = 1357
uses = ["def-sc-cr-field"]
+++
Let $K$ be a $C_1$ field ([def-sc-cr-field]). Then every
finite-dimensional central division algebra over $K$ is $K$ itself, so
the Brauer group of $K$ (central simple $K$-algebras up to Brauer
equivalence) vanishes, and the cohomological Brauer group vanishes as
well:

$$
\operatorname{Br}(K)=H^2(\operatorname{Spec}K_{\Et},\mathbf G_m)=0.
$$
