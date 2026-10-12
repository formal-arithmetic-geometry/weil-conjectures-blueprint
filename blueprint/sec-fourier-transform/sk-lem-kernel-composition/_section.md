+++
id = "sk-lem-kernel-composition"
kind = "proposition"
title = "P11: composition of kernel transforms"
order = 3015
lean = ["AlgebraicGeometry.Etale.kernelTransformCompIso"]
uses = ["sk-def-ft"]
tags = ["sketch"]
+++
Let $V\to S$, $V^\vee\to S$, $V'\to S$ be separated finite-type $S$-schemes,
let $\mathcal K\in\Dbc(V\times_SV^\vee,E)$ and
$\mathcal K'\in\Dbc(V^\vee\times_SV',E)$, and let

$$
\Phi_{\mathcal K}(K)=p_{2,!}(p_1^*K\otimes^L\mathcal K)[a],\qquad
\Phi_{\mathcal K'}(L)=q_{2,!}(q_1^*L\otimes^L\mathcal K')[b]
$$

be the kernel transforms with shifts $a$ and $b$. Then
$\Phi_{\mathcal K'}\circ\Phi_{\mathcal K}$ is the kernel transform with
kernel the *convolution*

$$
\mathcal K'\ast\mathcal K:=r_{13,!}\bigl(r_{12}^*\mathcal K\otimes^L
r_{23}^*\mathcal K'\bigr)\in\Dbc(V\times_SV',E)
$$

and shift $[a+b]$, the $r_{ij}$ being the projections of the triple product.
In particular $\FT_{\psi^{-1}}\FT_\psi$ is the kernel transform with kernel
$\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi$ and shift $[2r]$.
