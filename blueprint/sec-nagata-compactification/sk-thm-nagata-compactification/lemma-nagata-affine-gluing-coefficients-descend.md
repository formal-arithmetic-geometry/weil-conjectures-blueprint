+++
id = "lemma-nagata-affine-gluing-coefficients-descend"
kind = "lemma"
title = "All gluing coefficients occur at the selected stage"
order = 34
lean = ["AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.resLE_mem_localizationSubring_coeffSubring", "AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.exists_finset_closure_eq_coeffSubring", "AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.f_mem_coeffSubring", "AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.g_mem_coeffSubring"]
uses = ["def-nagata-affine-gluing-coefficient-stage", "lemma-nagata-finite-affine-gluing-presentation"]
+++
Each coefficient subring $A^{\mathrm{coeff}}_a\subseteq\Gamma(S,U_a)$ is
finitely generated and contains all basic-open elements $f_{abr}$ and
$g_{bar}$ of the chart $a$. Moreover, for all charts $a,b$, every $r$, and
every basic-open element $y$ of the chart $b$, the restriction of $y$ to
$D(f_{abr})$ lies in $A^{\mathrm{coeff}}_a[1/f_{abr}]\subseteq
\Gamma(S,D(f_{abr}))$; that is, the restricted overlap maps are defined at
the coefficient stage.
