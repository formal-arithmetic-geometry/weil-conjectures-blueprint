+++
id = "lemma-degree-zero-top-cohomology"
kind = "lemma"
title = "Degree zero and top cohomology"
order = 1144
lean = ["AlgebraicGeometry.WeilGroup.globalSections_eq_invariants", "AlgebraicGeometry.WeilSheaf.nonempty_equiv_compactlySupportedCohomology_two", "AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_isLisse", "AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_zero", "AlgebraicGeometry.WeilSheaf.isPureOfWeightOver_compactlySupportedCohomology_two"]
+++
Let $U_0/\mathbf F_q$ be a smooth geometrically connected curve, let
$\mathcal F$ be a lisse Weil sheaf on $U_0$, and let $V$ be its
geometric generic fibre, a representation of the geometric fundamental
group $\pi_1(U)$.  There are canonical
Frobenius-equivariant identifications

$$
H^0(U,\mathcal F)=V^{\pi_1(U)},\qquad
H_c^2(U,\mathcal F)=V_{\pi_1(U)}(-1).
$$

There is no compactly supported cohomology outside degrees $0,1,2$.
If $U_0$ is affine, $H_c^0(U,\mathcal F)=0$.
If $\mathcal F$ is punctually of weights $\le a$, the weights of $H^0$
are at most $a$ and those of $H_c^2$ at most $a+2$.  If $\mathcal F$
is pure of weight $a$, the two groups, when nonzero, are pure of weights
$a$ and $a+2$, respectively.
