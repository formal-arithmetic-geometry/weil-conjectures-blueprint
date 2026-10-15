+++
id = "sk-thm-picard-rr"
kind = "theorem"
title = "Riemann–Roch and coherent Serre duality"
order = 605
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-thm-picard-duality"]
lean = ["AlgebraicGeometry.Scheme.eulerChar_free_eq", "AlgebraicGeometry.Scheme.eulerChar_unit_eq", "AlgebraicGeometry.Scheme.finrankH_zero_eq", "AlgebraicGeometry.Scheme.isAmple_of_degree_pos", "AlgebraicGeometry.Scheme.isAffine_compl_of_isAmple"]
tags = ["sketch"]
+++
Fix a smooth projective geometrically connected curve $C/k$, and set
$g=\dim_kH^1(C,\cO_C)$. (Smooth proper geometrically connected curves
over a field are projective (Stacks Project, Tag 0A26), so this includes
the proper curves of the main text.) For an invertible sheaf $\cL$ on $C$,

$$
\chi(C,\cL)=\deg\cL+1-g,
\qquad
H^1(C,\cL)^\vee\simeq H^0(C,\omega_{C/k}\otimes\cL^{-1}),
\qquad \deg\omega_{C/k}=2g-2.
$$

These identifications commute with field extension. In particular, if
$\deg\cL>2g-2$, then

$$
H^1(C,\cL)=0,
\qquad h^0(C,\cL)=\deg\cL+1-g.
$$

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
