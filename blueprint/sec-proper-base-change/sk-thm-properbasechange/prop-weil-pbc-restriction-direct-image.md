+++
id = "prop-weil-pbc-restriction-direct-image"
kind = "theorem"
title = "Restriction of the direct image to bounded constructibles"
order = 1302
uses = ["def-weil-pbc-constructible-direct-image-finiteness", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-operations", "lem-sp-finite-filtration-induction", "thm-constructible-serre", "thm-sp-truncation-e2"]
tags = ["latex:proposition"]
+++
Let $\Lambda=P_n$ be as in
[def-weil-pbc-constructible-direct-image-finiteness], let $u:S\to T$ be a
morphism of schemes, and suppose $\mathrm{FIN}(u,\Lambda;c)$. Then the
ambient functor $Ru_*$ restricts to an exact triangulated functor
$$
 Ru_*:\Dbc(S_{\Proet},\Lambda)\longrightarrow\Dbc(T_{\Proet},\Lambda),
$$
and if $K\in\Dbc(S_{\Proet},\Lambda)$ has cohomology in $[a,b]$, then
$Ru_*K$ has cohomology in $[a,b+c]$.

## Proof

An object $K\in\Dbc(S_{\Proet},\Lambda)$ has constructible cohomology
sheaves $F_q=\mathcal H^q(K)$, zero outside the finite interval $[a,b]$. The
truncation-couple spectral sequence applied to the left exact $u_*$ gives
$$
 E_2^{p,q}=R^pu_*F_q\Longrightarrow\mathcal H^{p+q}(Ru_*K),
$$
with $E_2^{p,q}$ constructible for all $p,q$ by clause (i) of
[def-weil-pbc-constructible-direct-image-finiteness] and zero for $p>c$ by
clause (ii). For fixed $n=p+q$, the finite filtration of a convergent
spectral sequence exhibits $\mathcal H^n(Ru_*K)$ as a subquotient of a
finite extension of the constructible $E_\infty$-terms, hence constructible
by [thm-constructible-serre]; only $a\leq q\leq n$ and $p\leq c$
contribute, so $\mathcal H^n(Ru_*K)=0$ for $n\notin[a,b+c]$. Exactness is
the exactness of the ambient $Ru_*$ on the full triangulated subcategory
$\Dbc(S_{\Proet},\Lambda)$.
