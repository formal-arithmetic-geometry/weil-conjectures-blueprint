+++
id = "lem-sc-torus-homomorphism-monomial"
kind = "lemma"
title = "Homomorphisms from a split torus to $\\mathbf G_m$ are monomials"
order = 2045
uses = ["def-sc-gm-ga", "lem-sc-laurent-units"]
+++
Let $k$ be a field, $d\geq0$, and let
$\delta:\mathbf G_m^d\to\mathbf G_m$ be a morphism of $k$-group
schemes in the sense of [def-sc-gm-ga]. Writing $T_1,\dots,T_d$
for the coordinate functions of $\mathbf G_m^d$ and $t$ for the
coordinate function of $\mathbf G_m$, there are integers
$m_1,\dots,m_d$ with

$$
\delta^*(t)=T_1^{m_1}\cdots T_d^{m_d}
\qquad\text{in } k[T_1^{\pm1},\dots,T_d^{\pm1}].
$$

## Proof

By [def-sc-gm-ga] the coordinate rings of $\mathbf G_m^d$ and
$\mathbf G_m$ are $k[T_1^{\pm1},\dots,T_d^{\pm1}]$ and
$k[t,t^{-1}]$, and $\delta$ corresponds to the $k$-algebra map
$\delta^*$ with $F:=\delta^*(t)$. Multiplicativity of $\delta$
means $m_{\mathbf G_m}\circ(\delta\times\delta)= \delta\circ m_{\mathbf G_m^d}$; dualising, and using
$m_{\mathbf G_m}^*(t)=t\otimes t$ and
$m_{\mathbf G_m^d}^*(T_i)=T_i\otimes T_i$, this says

$$
F\otimes F=m^*(F),
$$

the right hand side being $F(TT')$, the image of $F$ under
$T_i\mapsto T_iT_i'$ in
$k[T_1^{\pm1},\dots,T_d^{\pm1}]\otimes_k k[T_1'^{\pm1},\dots,T_d'^{\pm1}]$. By
[lem-sc-laurent-units](b), $F=\lambda T^{\mathbf m}$ with
$\lambda\in k^\times$ and $\mathbf m\in\mathbf Z^d$; then
$F\otimes F=\lambda^2T^{\mathbf m}T'^{\mathbf m}$ and
$m^*(F)=\lambda T^{\mathbf m}T'^{\mathbf m}$, so
$\lambda^2=\lambda$ and $\lambda=1$.
