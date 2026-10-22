+++
id = "sk-thm-picard-rr"
kind = "theorem"
title = "Riemann–Roch and coherent Serre duality"
order = 605
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sec-abelian-varieties", "sec-nagata-compactification", "sk-def-picard-pic", "sk-prop-picard-pic-split"]
lean = ["AlgebraicGeometry.Scheme.eulerChar_unit_eq", "AlgebraicGeometry.Scheme.Modules.eulerChar_eq_degree_add", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.degree_dual_toModules", "AlgebraicGeometry.Scheme.Modules.degree_tensorObj", "AlgebraicGeometry.Scheme.Modules.exists_tensorObj_dual_toModules_iso", "AlgebraicGeometry.Scheme.serreDuality", "AlgebraicGeometry.Scheme.degree_relativeDifferentials", "AlgebraicGeometry.Scheme.Modules.degree_pullback", "AlgebraicGeometry.Scheme.arithmeticGenus_pullback", "AlgebraicGeometry.Scheme.Modules.finrankH_one_eq_zero_of_degree", "AlgebraicGeometry.Scheme.finrankH_zero_eq", "AlgebraicGeometry.Scheme.Modules.eulerChar_eq_coherentDegree_add", "AlgebraicGeometry.Scheme.isAmple_of_degree_pos", "AlgebraicGeometry.Scheme.isAffine_compl_of_isAmple"]
tags = ["sketch"]
+++
Fix a smooth proper curve $C/k$ with $H^0(C,\cO_C)=k$, and set
$g=\dim_kH^1(C,\cO_C)$. (For smooth proper $C$, the condition
$H^0(C,\cO_C)=k$ is equivalent to geometric connectedness, and such curves
are projective (Stacks Project, Tag 0A26).) For an invertible sheaf $\cL$ on $C$,

$$
\chi(C,\cL)=\deg\cL+1-g,
\qquad
H^1(C,\cL)^\vee\simeq H^0(C,\omega_{C/k}\otimes\cL^{-1}),
\qquad \deg\omega_{C/k}=2g-2.
$$

In particular, if
$\deg\cL>2g-2$, then

$$
H^1(C,\cL)=0,
\qquad h^0(C,\cL)=\deg\cL+1-g.
$$

The genus and the degree are invariant under extension of the ground
field.

Here $\deg\cL=\deg D=\sum_xn_x[\kappa(x):k]$ for any divisor
$D=\sum_xn_x\,x$ with $\cL\cong\cO_C(D)$ (well defined, since principal
divisors have degree $0$), and $\chi(C,\cL)=h^0(C,\cL)-h^1(C,\cL)$.

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
