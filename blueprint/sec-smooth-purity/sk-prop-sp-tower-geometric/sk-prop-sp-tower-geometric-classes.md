+++
id = "det-sp-tower-classes"
kind = "definition"
title = "Kummer and diagonal classes of towers"
order = 3019
uses = ["det-sp-coefficient-towers-abelian", "det-sp-tower-shriek-levels"]
+++
Let $S$ be a scheme.

1. *Kummer tower.* In the abelian category of towers of abelian sheaves on
   $S_{\mathrm{proét}}$ the sequence
   $$
   0\longrightarrow(\mu_{\ell^n})_n\longrightarrow(\mathbb G_m,(\cdot)^\ell)
   \xrightarrow{\ ((\cdot)^{\ell^n})_n\ }(\mathbb G_m,\mathrm{id})\longrightarrow0
   $$
   is exact, where the middle tower has $\mathbb G_m$ at every level with
   transitions the $\ell$-th power map, the right tower has identity
   transitions, and $(\mu_{\ell^n})_n$ has the $\ell$-power map as transitions.
2. *First Chern class.* For a line bundle $L$ on $S$, its class in
   $H^1(S,(\mathbb G_m,\mathrm{id}))$ has a boundary in
   $H^2(S,(\mu_{\ell^n})_n)$, i.e. a morphism
   $(\mathbf Z/\ell^n)_n\to(\mu_{\ell^n})_n[2]$ of $(\mathbf Z/\ell^n)_n$-modules;
   extending coefficients gives
   $c_1(L):\mathcal O_{E,S}/\ell^\bullet\to(\mathcal O_{E,S}/\ell^\bullet)(1)[2]$ in
   $D(\operatorname{Tow}(S,\mathcal O_E))$, whose level $n$ is the finite Kummer class
   $c_1(L)$ with coefficients $\mathcal O_E/\ell^n$.
3. *Diagonal class.* The version with supports, applied to the diagonal
   Cartier divisor $\Delta\subset\mathbf P^1_S\times_S\mathbf P^1_S$ with its
   canonical section, gives
   $\delta_\bullet:\Delta_*\mathcal O_{E,\mathbf P^1_S}/\ell^\bullet\to
   (\mathcal O_{E,\mathbf P^1_S\times_S\mathbf P^1_S}/\ell^\bullet)(1)[2]$, whose level
   $n$ is the finite diagonal class.
4. *Splitting.* The unit and $c_1(\mathcal O(1))$ define an isomorphism in
   $D(\operatorname{Tow}(S,\mathcal O_E))$, for $q:\mathbf P^1_S\to S$,
   $$
   \mathcal O_{E,S}/\ell^\bullet\oplus(\mathcal O_{E,S}/\ell^\bullet)(-1)[-2]
   \xrightarrow{\ \sim\ }Rq_{*,\bullet}\mathcal O_{E,\mathbf P^1_S}/\ell^\bullet,
   $$
   and $\operatorname{Tr}_{q,\bullet}$ denotes the projection onto the twisted
   summand.
