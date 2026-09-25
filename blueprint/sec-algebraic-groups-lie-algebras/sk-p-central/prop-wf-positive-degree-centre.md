+++
id = "prop-wf-positive-degree-centre"
kind = "theorem"
title = "Central element of positive degree"
order = 2679
tags = ["latex:proposition"]
uses = ["def-wf-algebraic-components", "def-wf-algebraic-radicals", "def-wf-arithmetic-monodromy-extension", "def-wf-degree-components", "def-wf-geometric-semisimplicity", "lem-wf-disconnected-geometric-centre", "lem-wf-inner-correction"]
+++
Assume $\rho$ is geometrically semisimple and the geometric monodromy identity component
$H=H_{\mathrm{geom}}^\circ$ is semisimple. Then the centre of the
locally finite-type group $G_{\mathrm{arith}}(\rho)$ contains an
algebraic-monodromy element of positive degree. More precisely, if

$$
\deg_Z:Z(G_{\mathrm{arith}}(\rho))(\overline{\mathbf Q}_\ell)
\longrightarrow\mathbf Z
$$

is the restriction of the degree projection in
[def-wf-arithmetic-monodromy-extension], then its kernel is finite
and its cokernel is finite.

## Proof

The hypothesis is geometric semisimplicity in the sense of
[def-wf-geometric-semisimplicity]. In the component notation of
[def-wf-degree-components], choose $z_0\in G^{[n]}$ centralizing
$H$ by
[lem-wf-inner-correction]. Let
$D=H_{\mathrm{geom}}/H$, a finite group by
[def-wf-algebraic-components]. A power $z_1=z_0^b$ acts trivially
on $D$, where $b$ is the order of its permutation action. For
$u\in H_{\mathrm{geom}}$, set

$$
c(u)=z_1uz_1^{-1}u^{-1}.
$$

Triviality of the action on $D$ gives $c(u)\in H$. For $h\in H$,
put $h'=u^{-1}hu\in H$. Using that $z_1$ centralizes $H$, we get

$$
c(u)h c(u)^{-1}
=z_1u h'u^{-1}z_1^{-1}=z_1hz_1^{-1}=h,
$$

so $c(u)\in Z(H)$. The latter group is finite because $H$ is
semisimple. Raising $z_1$ to the exponent $e$ of $Z(H)$ therefore
gives $z_2=z_1^e$ commuting with every element of
$H_{\mathrm{geom}}$: since $z_1$ commutes with $c(u)$, induction
gives $z_1^r u z_1^{-r}=c(u)^r u$, and $c(u)^e=1$.

It remains to commute with the degree-one generator $s=(1,1)$. The
commutator $d=sz_2s^{-1}z_2^{-1}$ has degree zero. Both $z_2$ and
$sz_2s^{-1}$ centralize $H_{\mathrm{geom}}$ (the latter because
$s$ normalizes that group), so $d\in Z(H_{\mathrm{geom}})$, which is
finite by [lem-wf-disconnected-geometric-centre]. Raise once more
to the exponent $f$ of this finite group and put $z=z_2^f$. Since
$z_2$ commutes with $d$,

$$
szs^{-1}=(sz_2s^{-1})^f=(dz_2)^f=d^fz_2^f=z_2^f,
$$

so $z$ commutes with both
$H_{\mathrm{geom}}$ and $s$, so it is central in the semidirect product
[def-wf-arithmetic-monodromy-extension]; its degree is
$nbef>0$.

The degree-zero part of the centre is contained in
$Z(H_{\mathrm{geom}})$, which is finite by
[lem-wf-disconnected-geometric-centre]; this proves finiteness of
the kernel. The image contains the positive integer $\deg(z)$, hence is
the subgroup $d\mathbf Z$ for some $d>0$, and the cokernel
$\mathbf Z/d\mathbf Z$ is finite. This is the precise meaning of the
degree statement; no degree map on a single finite-type algebraic group has
been asserted.
