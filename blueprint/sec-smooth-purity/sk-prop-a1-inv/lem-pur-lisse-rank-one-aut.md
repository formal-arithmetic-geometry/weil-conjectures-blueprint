+++
id = "lem-pur-lisse-rank-one-aut"
kind = "lemma"
title = "Automorphisms of a rank-one finite locally constant sheaf"
order = 3251
uses = ["def-pur-conventions", "def-weil-derived-pullback-tensor-hom", "def-weil-scheme-morphism-properties"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $T$ be a separated
finite-type $k$-scheme and let $L,M$ be finite locally constant
$\Lambda$-sheaves of rank one on $T$.

1. The canonical map $\Lambda_T\to\mathcal Hom(L,L)$,
$1\mapsto\operatorname{id}_L$, is an isomorphism; hence every
endomorphism of $L$ is multiplication by a unique locally
constant function $T\to\Lambda$, and
$\operatorname{Aut}(L)=\Gamma(T,\Lambda_T^\times)$ is the group
of locally constant units.
1. Any two isomorphisms $\varphi,\psi:L\to M$ differ by a unique
automorphism of $M$: there is a unique locally constant unit
$u\in\Gamma(T,\Lambda_T^\times)$ with $\psi=u\cdot\varphi$.
In particular, for every geometric point $\bar t$ of $T$ and
every unit $v\in\Lambda^\times$ there is an isomorphism
$\psi:L\to M$ with $\psi_{\bar t}=v\cdot\varphi_{\bar t}$,
namely $\psi=v\cdot\varphi$ for the constant unit $v$.
