+++
id = "det-cor-sf-direct-image-ctf-open-tor"
kind = "lemma"
title = "Scalar projection formula and the Tor bound for an open immersion"
order = 2709
uses = ["def-kun-cd", "lem-kun-0f10", "lem-kun-0f12", "def-weil-finite-tor-amplitude", "lem-exc-comparison-tor-interval", "prop-weil-pbc-comparison-direct-image"]
+++
Let $k$ be a separably closed field, $\ell\ne\operatorname{char}(k)$, $A$ a
finite commutative $\ell$-primary ring, and $j:U\hookrightarrow X$ an open
immersion of finite-type $k$-schemes. Let $d\ge\operatorname{cd}(j)$
([def-kun-cd]; finite by [lem-kun-0f10]). Let
$K\in D(U_{\mathrm{ét}},A)$ have Tor amplitude in $[a,b]$ in the sense of
[def-weil-finite-tor-amplitude]: $\mathcal H^r(K\otimes^{\mathbf L}_AN)=0$ for
$r\notin[a,b]$ and every $A$-module sheaf $N$ on $U_{\mathrm{ét}}$. Then:

1. for every $A$-module $M$, with constant sheaves $\underline M_X$,
   $\underline M_U=j^*\underline M_X$, the projection morphism

   $$
   (Rj_*K)\otimes^{\mathbf L}_A\underline M_X\longrightarrow
   Rj_*\bigl(K\otimes^{\mathbf L}_A\underline M_U\bigr)
   $$

   is an isomorphism in $D(X_{\mathrm{ét}},A)$;
2. $Rj_*K$ has Tor amplitude in $[a,b+d]$ on $X_{\mathrm{ét}}$;
3. $Rj_{\mathrm{proét},*}\nu_U^*K\cong\nu_X^*Rj_*K$ has Tor amplitude in
   $[a,b+d]$ against every module sheaf on $X_{\mathrm{proét}}$.
