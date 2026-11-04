+++
kind  = "proof"
of    = "lem-sc-riemann-roch-large-degree"
+++
By Serre duality ([thm-sc-serre-duality-curve]),

$$
H^1(C,\mathcal L)^{\vee}\cong H^0\bigl(C,\mathcal L^{-1}\otimes\Omega^1_{C/k}\bigr).
$$

Here $\deg\Omega^1_{C/k}=2g-2$ ([lem-sc-canonical-degree]) and the degree
is additive under tensor products, with $\deg\mathcal L^{-1}=-d$
([lem-pc-degree-base-change](2)), so

$$
\deg\bigl(\mathcal L^{-1}\otimes\Omega^1_{C/k}\bigr)=(2g-2)-d\le-1<0 .
$$

A line bundle of negative degree has no nonzero global sections
([lem-sc-negative-degree-no-sections]), so the right-hand side vanishes
and $H^1(C,\mathcal L)=0$. Since also $H^q(C,\mathcal L)=0$ for $q\ge2$
(Grothendieck vanishing on the one-dimensional Noetherian scheme $C$),
Riemann–Roch ([lem-sc-riemann-roch], part (1)) gives

$$
\dim_kH^0(C,\mathcal L)=\chi(C,\mathcal L)=d+1-g.
$$
