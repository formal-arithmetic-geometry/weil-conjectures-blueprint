+++
id = "sk-d-ab-rankone"
kind = "definition"
title = "A split cyclic extension and rank-one characters"
order = 2867
uses = ["sk-d-monodromy"]
lean = ["SemidirectProduct.inrOfAddOne", "SemidirectProduct.degreeCharacter", "SemidirectProduct.finitePart"]
tags = ["sketch"]
+++
Let $P$ be a group and $\alpha$ an automorphism. Put
$W=P\rtimes_\alpha\mathbf Z$, with multiplication

$$
(u,n)(v,m)=(u\alpha^n(v),n+m),\qquad
\gamma=(1,1),\qquad \deg(u,n)=n.
$$

Identify $P$ with $P\times\{0\}$; every element has a unique form
$u\gamma^n$. For a field $E$, a rank-one character is a homomorphism
$\chi:W\to E^\times$. It has finite geometric image if $\chi(P)$ is
finite, and finite image if $\chi(W)$ is finite.
More generally, for a homomorphism $\chi:W\to A$ into a commutative
group $A$ (a rank-one character being the case $A=E^\times$), set
$z=\chi(\gamma)$ and define the functions

$$
\chi_z(w)=z^{\deg(w)},\qquad
\chi_{\mathrm{fin}}(w)=\chi(w)z^{-\deg(w)}.
$$
