+++
id = "sk-lem-coprojection"
kind = "lemma"
title = "Co-projection for a closed immersion"
order = 1946
uses = ["sk-def-purity-conv"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_derivedTensor_of_isInvertible"]
tags = ["sketch"]
+++
Let $\Lambda$ be a finite commutative ring with a Tate twist datum, let
$i:Z\hookrightarrow X$ be a closed immersion, let
$K\in D^b_{ctf}(X,\Lambda)$ and let $L$ be an *invertible* object of
$D^b_{ctf}(X,\Lambda)$ (on the small étale sites). Then there is an isomorphism

$$
Ri^{!}\bigl(K\otimes^{\mathbb L}_{\Lambda_X}L\bigr)\ \cong\
Ri^{!}K\otimes^{\mathbb L}_{\Lambda_Z}Li^{*}L :
$$

an invertible tensor factor passes through $i^{!}$ at the
cost of restricting it. In particular, for $f:X\to Y$ with $f'=f\circ i$ and
$B$ invertible on $Y$, taking $L=Lf^{*}B$ and using
$Li^{*}Lf^{*}B\cong Lf'^{*}B$ gives

$$
Ri^{!}\bigl(K\otimes^{\mathbb L}_{\Lambda_X}Lf^{*}B\bigr)\ \cong\
Ri^{!}K\otimes^{\mathbb L}_{\Lambda_Z}Lf'^{*}B ;
$$

and for the Tate twists $L=\Lambda_X(m)[2m]$, whose restriction is
$\Lambda_Z(m)[2m]$, it reads
$Ri^{!}(K(m)[2m])\cong(Ri^{!}K)(m)[2m]$.
Iterating, for
$p_1,p_2:W=X\times_YX\to X$, $\Delta:W\supset X$ and $\omega_f$ invertible:

$$
R\Delta^{!}\bigl(Lp_1^{*}\omega_f\otimes^{\mathbb L}Lp_2^{*}\omega_f\bigr)
\ \cong\
\bigl(R\Delta^{!}\Lambda_W\bigr)\otimes^{\mathbb L}
L\Delta^{*}Lp_1^{*}\omega_f\otimes^{\mathbb L}L\Delta^{*}Lp_2^{*}\omega_f .
$$
