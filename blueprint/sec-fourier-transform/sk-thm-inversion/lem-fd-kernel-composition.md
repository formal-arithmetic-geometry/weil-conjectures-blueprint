+++
id = "lem-fd-kernel-composition"
kind = "lemma"
title = "Composition of kernel transforms"
order = 4172
uses = ["def-fd-kernel", "def-fd-transform", "prop-functor-package"]
+++
Let $V\to S$, $V^\vee\to S$, $V''\to S$ be separated finite-type
$S$-schemes, let $\mathcal K\in D^b_c(V\times_SV^\vee,E)$ and
$\mathcal K'\in D^b_c(V^\vee\times_SV'',E)$, and let

$$
\Phi_{\mathcal K}(K)=p_{2,!}(p_1^*K\otimes^L\mathcal K)[a],\qquad
\Phi_{\mathcal K'}(L)=q_{2,!}(q_1^*L\otimes^L\mathcal K')[b]
$$

be the corresponding kernel transforms, with $p_i,q_i$ the projections of
$V\times_SV^\vee$ and $V^\vee\times_SV''$ and shifts $a,b$. Then
$\Phi_{\mathcal K'}\circ\Phi_{\mathcal K}$ is the kernel transform with
kernel the *convolution*

$$
\mathcal K'\ast\mathcal K:=r_{13,!}\bigl(r_{12}^*\mathcal K\otimes^L
r_{23}^*\mathcal K'\bigr)\in D^b_c(V\times_SV'',E)
$$

and shift $[a+b]$, the $r_{ij}$ being the projections of the triple
product $V\times_SV^\vee\times_SV''$. In particular
$\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi$ is the kernel
transform with kernel $\mathcal K_{\psi^{-1}}\ast\mathcal K_\psi$ and shift
$[2r]$.
