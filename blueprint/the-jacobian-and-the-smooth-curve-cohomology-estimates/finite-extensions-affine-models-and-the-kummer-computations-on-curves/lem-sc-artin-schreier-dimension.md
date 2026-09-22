+++
id = "lem-sc-artin-schreier-dimension"
kind = "lemma"
title = "Artin–Schreier vanishing on a smooth curve"
order = 4536
lean = ["AlgebraicGeometry.Curve.h_artinSchreier_eq_zero_of_one_lt"]
uses = ["lem-sc-etale-affine-qcoherent", "lem-sc-ga-cohomology"]
+++
Let $C$ be a smooth separated curve over an algebraically closed field of
characteristic $p>0$. For the constant sheaf $\mathbf F_p$, one has
$H^q(C,\mathbf F_p)=0$ for $q>1$.

## Proof

By the compactification lemma and the affineness of a proper open of a
compactification, the curve is either proper or affine. In the affine case,
[lem-sc-etale-affine-qcoherent] gives $H^q(C,\mathbf G_a)=0$ for $q>0$, so
the Artin–Schreier long exact sequence gives $H^q(C,\mathbf F_p)=0$ for
$q>1$.

We now treat the proper case. The long exact sequence of the Artin–Schreier
sequence,
$$
0\to H^0(C,\mathbf F_p)\to H^0(C,\mathbf G_a)\xrightarrow{\ \wp\ }
H^0(C,\mathbf G_a)\to H^1(C,\mathbf F_p)\to H^1(C,\mathbf G_a)
\xrightarrow{\ \wp\ }H^1(C,\mathbf G_a)\to H^2(C,\mathbf F_p)\to0,
$$
(the terms $H^q(C,\mathbf G_a)$ vanish for $q\geq2$ by
[lem-sc-ga-cohomology]) identifies
$$
H^2(C,\mathbf F_p)=\operatorname{coker}\bigl(\wp:H^1(C,\mathcal O_C)\to H^1(C,\mathcal O_C)\bigr),
$$
where $\wp=F-1$ with $F$ the $p$-linear Frobenius endomorphism of the
finite-dimensional $k$-vector space $H^1(C,\mathcal O_C)$; this cokernel is
zero by the Lang–Steinberg theorem. Hence $H^q(C,\mathbf F_p)=0$ for $q>1$:
for $q\geq3$ the two adjacent $\mathbf G_a$ cohomology terms vanish, and the
case $q=2$ is the surjectivity just proved.

Unresolved dependencies: def:sc-curves, def:sc-constant-sheaves, def:weil-pbc-etale-cohomology, lem:sc-compactification, lem:sc-affine-open-proper, lem:sc-as-sequence, lem:sc-lang-steinberg
