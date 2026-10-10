+++
id = "sk-thm-picard-rr"
kind = "theorem"
title = "Riemann–Roch for curves, and its geometric corollary"
order = 705
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.Scheme.eulerChar_free_eq", "AlgebraicGeometry.Scheme.eulerChar_unit_eq", "AlgebraicGeometry.Scheme.finrankH_zero_eq", "AlgebraicGeometry.Scheme.isAmple_of_degree_pos", "AlgebraicGeometry.Scheme.isAffine_compl_of_isAmple"]
tags = ["sketch"]
+++
Let $X$ be a smooth proper curve over $k$ with $H^0(X,\cO_X)=k$ (e.g.
the base change to any field of a smooth projective curve over an
algebraically closed field), of genus $g=\dim_kH^1(X,\cO_X)$ (as in the
conventions; flat base change preserves $h^0$ and $h^1$), and $\cF$
coherent, with $\chi(\cF)=\sum_q(-1)^q\dim_kH^q(X,\cF)$.

*Degrees.* For a divisor $D=\sum_xn_x\,x$ ($x$ closed points)
put $\deg D=\sum_xn_x[\kappa(x):k]$. Principal divisors have degree
$0$ (for $f\in k(X)\setminus k$, $\operatorname{div}f=f^*(0)-f^*(\infty)$
for the finite flat $f:X\to\mathbf P^1_k$, both of degree $[k(X):k(f)]$),
and every line bundle is $\cL\cong\cO_X(D)$ (divisor of a nonzero
rational section), so $\deg\cL:=\deg D$ is well defined and additive.
For coherent $\cF$ with torsion subsheaf $\mathcal T$ and locally free quotient
$\mathcal E=\cF/\mathcal T$ of rank $\rk\cF$, put
$\deg\cF:=\sum_x\operatorname{length}_{\cO_{X,x}}(\cT_x)[\kappa(x):k]+\deg(\det\mathcal E)$
$=\dim_kH^0(X,\mathcal T)+\deg(\det\mathcal E)$.

1. **(RR)** $\chi(\cF)=\deg\cF+\rk(\cF)(1-g)$; in
particular $\chi(\cO_X)=1-g$, and for every line bundle
$\deg\cL=\chi(\cL)-\chi(\cO_X)$, i.e. the divisor degree agrees with
the $\chi$-degree used for the Picard scheme below (so the two
definitions of $\Pic^0$, as kernel of either degree, coincide); and
for a line bundle of degree $d$ with $d\ge2g-1$: $h^0(\cL)=d+1-g$.
1. **(G)** *positive degree $\Rightarrow$ ample:* if
$\cL$ is a line bundle on $X$ with $\deg\cL>0$, then $\cL$ is ample
($h^0(\cL^{\otimes m})=m\deg\cL+1-g$ grows, and after base change to
$\bar k$, where all closed points are rational, base-point freeness and
the separation of points and tangent vectors follow from (RR) by
subtracting one or two points; over a general $k$ subtracting a closed
point $P$ changes $h^0$ by $[\kappa(P):k]$, not by $1$).
1. **(H)** *affine complement:* if $D$ is an effective Cartier divisor
on $X$ such that $\cO_X(D)$ is ample, then
$X\setminus\operatorname{Supp}(D)$ is affine (this part holds for any
proper $k$-scheme $X$; smoothness, dimension one and $H^0(X,\cO_X)=k$
are not needed).
