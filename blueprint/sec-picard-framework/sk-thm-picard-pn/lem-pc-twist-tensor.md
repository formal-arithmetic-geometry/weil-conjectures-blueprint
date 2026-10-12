+++
id = "lem-pc-twist-tensor"
kind = "lemma"
title = "Twists and tensor products"
order = 622
uses = ["def-pc-proj", "def-pc-projective-space-twist", "def-sc-invertible-module"]
+++
Let $A$ be a commutative ring, $n\ge0$,
$P=\operatorname{Proj}(A[x_0,\ldots,x_n])$ with standard affine opens
$U_i=D_+(x_i)$ and bases $e_i^{(d)}$ of $\mathcal O_P(d)|_{U_i}$, and let
$d,e\in\mathbf Z$ ([def-pc-projective-space-twist]). Then there is a
canonical isomorphism
$\mathcal O_P(d)\otimes_{\mathcal O_P}\mathcal O_P(e)\to\mathcal O_P(d+e)$
of [def-sc-invertible-module] whose restriction to $U_i$ sends
$e_i^{(d)}\otimes e_i^{(e)}$ to $e_i^{(d+e)}$.
