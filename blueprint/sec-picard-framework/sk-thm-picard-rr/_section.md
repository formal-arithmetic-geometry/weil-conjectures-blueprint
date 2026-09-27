+++
id = "sk-thm-picard-rr"
kind = "section"
title = "Riemann–Roch for curves, and its geometric corollary"
order = 705
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.Scheme.riemannRoch", "AlgebraicGeometry.Scheme.isAmple_of_degree_pos", "AlgebraicGeometry.Scheme.isAffine_compl_of_isAmple"]
+++
*Theorem (sketch).*

Let $X$ be a smooth proper curve over $k$ and $\cF$ coherent, with
$\chi(\cF)=\sum_q(-1)^q\dim_kH^q(X,\cF)$.

1. ****(RR)**** $\chi(\cF)=\deg\cF+\rk(\cF)(1-g)$; in
particular $\chi(\cO_X)=1-g$, and for a line bundle of degree $d$
with $d\ge2g-1$: $h^0(\cL)=d+1-g$.
1. ****(G)**** *positive degree $\Rightarrow$ ample:* if
$\cL$ is a line bundle on $X$ with $\deg\cL>0$, then $\cL$ is ample
($h^0(\cL^{\otimes m})=m\deg\cL+1-g$ grows, and base-point
freeness and the separation of points follow by subtracting a point
one at a time).
1. ****(H)**** *affine complement:* if $\cL$ is ample
and $D$ an effective Cartier divisor with $\cL\cong\cO_X(D)$, then
$X\setminus\operatorname{Supp}(D)$ is affine.

## Proof

(RR): by additivity of $\chi$ in short exact sequences, the torsion
part of $\cF$ (for which $\chi$ is the length, i.e. the degree) and a
filtration of the locally free quotient reduce the formula to line
bundles, where it is $\chi(\cO_X(D))=\deg D+\chi(\cO_X)$ with
$\chi(\cO_X)=1-g$; for $d\ge2g-1$, [sk-thm-picard-duality] gives
$H^1(\cL)^\vee\cong H^0(\omega_X\otimes\cL^{-1})=0$, the latter of
negative degree, whence $h^0(\cL)=d+1-g$. (G): by (RR), $h^0(\cL^{\otimes m})\ge m\deg\cL+1-g\to\infty$; reducing the degree by a point $P$ lowers
$h^0$ by exactly $1$ until $h^0\le1$, whence the base-point-free
statement for $m\gg0$ and then the very-ample statement, exactly as
in the twist lemma below. (H): classical (the complement of an
ample effective divisor is affine).
