+++
id = "lem-pur-kummer-additivity"
kind = "lemma"
title = "Kummer additivity"
order = 1944
uses = ["def-coefficient-twists-detailed", "def-pur-affine-line-datum", "def-pur-conventions", "def-weil-derived-cohomology-sheaves", "def-weil-scheme-morphism-properties"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $T$ be a
separated finite-type
$k$-scheme. For a line bundle $M$ on $T$ let

$$
c_1(M):\Lambda_T\longrightarrow\Lambda_T(1)[2]
$$

be the class of the $A$-torsor of height $\ell^N$-th roots of a
trivialization of $M$, i.e. the image of the class of $M$ in
$H^1(T_{\Et},\mathbf G_m\otimes_{\mathbf Z}A)$ under the connecting
morphism of the Kummer exact sequence of
[def-pur-affine-line-datum] (the identification
$H^1(T_{\Et},\mathbf G_m)=\operatorname{Pic}(T)$ is the standard one:
the $A$-torsor of isomorphisms $\mathcal O_T\to M$ recovers $M$
as $(T\times M)/\mathbf G_m$).
Then

$$
c_1(M\otimes N)=c_1(M)+c_1(N),
$$

and $c_1$ is compatible with pullback and with base change.
