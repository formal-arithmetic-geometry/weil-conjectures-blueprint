+++
id = "sk-thm-picard-twist"
kind = "lemma"
title = "Twisting to $h^0=1$ and $h^1=0$"
order = 894
lean = ["AlgebraicGeometry.Scheme.exists_isInvertible_twist"]
uses = ["sk-prop-picard-pic-split", "sk-lem-abelian-seesaw", "sk-def-picard-pic", "sk-thm-picard-perfect", "sk-thm-picard-rr", "sec-abelian-varieties", "sec-nagata-compactification", "sk-thm-picard-f-representable"]
tags = ["sketch"]
+++
Suppose that $k$ is separably closed. For every field extension
$k'/k$ and every invertible sheaf $\mathcal L$ on $C_{k'}$, there is an
invertible sheaf $\mathcal M_0$ on $C$ such that

$$
h^0(C_{k'},\mathcal L\otimes\mathcal M_{0,k'})=1,
\qquad H^1(C_{k'},\mathcal L\otimes\mathcal M_{0,k'})=0.
$$
