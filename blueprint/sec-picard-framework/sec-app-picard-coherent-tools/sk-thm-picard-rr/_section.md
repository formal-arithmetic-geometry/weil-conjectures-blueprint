+++
id = "sk-thm-picard-rr"
kind = "theorem"
title = "Riemann–Roch and coherent Serre duality"
order = 882
lean = ["AlgebraicGeometry.Scheme.eulerChar_unit_eq", "AlgebraicGeometry.Scheme.Modules.eulerChar_eq_degree_add", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.degree_dual_toModules", "AlgebraicGeometry.Scheme.Modules.degree_tensorObj", "AlgebraicGeometry.Scheme.Modules.exists_tensorObj_dual_toModules_iso", "AlgebraicGeometry.Scheme.serreDuality", "AlgebraicGeometry.Scheme.degree_relativeDifferentials", "AlgebraicGeometry.Scheme.Modules.degree_pullback", "AlgebraicGeometry.Scheme.arithmeticGenus_pullback", "AlgebraicGeometry.Scheme.Modules.finrankH_one_eq_zero_of_degree", "AlgebraicGeometry.Scheme.finrankH_zero_eq", "AlgebraicGeometry.Scheme.Modules.eulerChar_eq_coherentDegree_add", "AlgebraicGeometry.Scheme.isAmple_of_degree_pos", "AlgebraicGeometry.Scheme.isAffine_compl_of_isAmple"]
uses = ["sk-prop-picard-pic-split", "sk-lem-abelian-seesaw", "sk-prop-av-isogeny", "sk-def-picard-pic", "sec-abelian-varieties", "sec-nagata-compactification"]
tags = ["sketch"]
+++
For an invertible sheaf $\mathcal L$ on $C$ we have

$$
\chi(C,\mathcal L)=\deg\mathcal L+1-g,
\qquad
H^1(C,\mathcal L)^\vee
\simeq H^0(C,\omega_{C/k}\otimes\mathcal L^{-1}),
\qquad \deg\omega_{C/k}=2g-2.
$$

These identifications commute with field extension. In particular, if
$\deg\mathcal L>2g-2$, then

$$
H^1(C,\mathcal L)=0,
\qquad h^0(C,\mathcal L)=\deg\mathcal L+1-g.
$$

*Complements* (also proved in this sketch and used in this block). The
Riemann–Roch formula extends to coherent $\cF$ as
$\chi(\cF)=\deg\cF+\operatorname{rk}(\cF)(1-g)$, with
$\deg\cF=\dim_kH^0(C,\mathcal T)+\deg\det(\cF/\mathcal T)$ for the torsion
subsheaf $\mathcal T$; and:

1. **(G)** *positive degree $\Rightarrow$ ample:* a line bundle $\cL$
on $C$ with $\deg\cL>0$ is ample;
1. **(H)** *affine complement:* if $D$ is an effective Cartier divisor
on a proper $k$-scheme $X$ with $\cO_X(D)$ ample, then
$X\setminus\operatorname{Supp}(D)$ is affine.
