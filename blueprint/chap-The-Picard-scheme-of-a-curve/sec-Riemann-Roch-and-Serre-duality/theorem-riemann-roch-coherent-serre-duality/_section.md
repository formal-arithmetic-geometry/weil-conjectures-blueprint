+++
id = "theorem-riemann-roch-coherent-serre-duality"
kind = "theorem"
title = "Riemann–Roch and coherent Serre duality"
order = 1525
lean = ["AlgebraicGeometry.Scheme.Modules.eulerChar_eq_degree_add", "AlgebraicGeometry.Scheme.serreDuality", "AlgebraicGeometry.Scheme.degree_relativeDifferentials", "AlgebraicGeometry.Scheme.Modules.finrankH_one_eq_zero_of_degree", "AlgebraicGeometry.Scheme.finrankH_zero_eq"]
uses = ["proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "corollary-serre-duality-field-extension"]
+++
For an invertible sheaf $\mathcal L$ on $C$ we have

$$
\chi(C,\mathcal L)=\deg\mathcal L+1-g,
\qquad
H^1(C,\mathcal L)^\vee
\simeq H^0(C,\omega_{C/k}\otimes\mathcal L^{-1}),
\qquad \deg\omega_{C/k}=2g-2.
$$

In particular, if
$\deg\mathcal L>2g-2$, then

$$
H^1(C,\mathcal L)=0,
\qquad h^0(C,\mathcal L)=\deg\mathcal L+1-g.
$$
