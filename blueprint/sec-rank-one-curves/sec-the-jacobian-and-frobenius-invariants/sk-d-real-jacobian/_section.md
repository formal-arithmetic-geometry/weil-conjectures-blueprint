+++
id = "sk-d-real-jacobian"
kind = "proposition"
title = "Kummer, duality and the integral Tate module"
order = 647
lean = ["AlgebraicGeometry.JacobianTorsionDatum", "AlgebraicGeometry.JacobianTorsionDatum.tateModule"]
uses = ["sk-cor-jacobian-torsion", "sk-def-picard-pic", "sk-thm-picard-main", "sk-prop-av-tate-rank", "sk-prop-jacobian-descent", "sk-thm-curveestimate", "sk-thm-sf-identification"]
tags = ["sketch"]
+++
Let $C_0/k_0$ be a smooth proper geometrically connected curve with
Jacobian $J_0$, and put $A_n=\mathbf Z/\ell^n$. There are canonical compatible Galois-equivariant
identifications

$$
H^1(C,A_n(1))\simeq J[\ell^n](k),\qquad
\varprojlim_n H^1(C,A_n)
\simeq\Hom_{\Zl}(T_\ell J,\Zl).
$$

Here the transition maps are multiplication by $\ell$ on
$J[\ell^n](k)$ and reduction of coefficients on $H^1(C,A_n)$. If
arithmetic Frobenius on $T_\ell J$ has matrix $B$, then geometric
Frobenius on $\Hom_{\Zl}(T_\ell J,\Zl)$ has matrix $B^t$ in the dual
basis.

*Complement.* The data used are a *Jacobian torsion datum*: an abelian
variety $J_0/\Fq$ with Galois-equivariant isomorphisms
$J[\ell^n]\simeq\operatorname{Pic}(C)[\ell^n]$, compatible with
multiplication by $\ell$ and the $\ell$-th tensor power, and its Tate modules
$T_\ell J=\varprojlim_nJ[\ell^n]$, $V_\ell J=T_\ell J\otimes\Ql$; the roots of
unity $(\mu_{\ell^n},z\mapsto z^\ell)$ define $\Zl(1)$, on which geometric
Frobenius acts by $q^{-1}$ ([lem-wf-curve-kummer-jacobian-tate-module],
[lem-wf-geometric-jacobian-galois-action]).
