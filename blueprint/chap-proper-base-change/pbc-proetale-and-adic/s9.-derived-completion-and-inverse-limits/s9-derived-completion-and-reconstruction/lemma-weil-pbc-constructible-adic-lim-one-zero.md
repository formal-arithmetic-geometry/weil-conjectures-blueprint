+++
id = "lemma-weil-pbc-constructible-adic-lim-one-zero"
kind = "lemma"
title = "Bounded constructible towers have no Milnor obstruction"
order = 1843
uses = ["def-weil-pbc-bounded-constructible-adic-tower", "lemma-weil-pbc-adic-lim-one-zero", "lemma-weil-pbc-adic-milnor-sequence"]
+++
If the reduction tower $K_\bullet$ attached to $K$ is uniformly bounded
constructible, then on every weakly contractible quasi-compact $U$ lying
over one of the displayed strata,

$$
H^i\left(U,R\varprojlim_nK_n\right)
\xrightarrow{\sim}\varprojlim_nH^i(U,K_n),
$$

and both sides vanish outside $[d_0,d_1]$.

## Proof

Fix $n$ and $i$. As $m$ increases, the image sheaves of
$H^i(K_m)\to H^i(K_n)$ form a descending chain of finite lisse subsheaves on
each displayed stratum. On each connected component their fibers are
descending chains of subgroups of a finite group, so they stabilize. There
are only finitely many strata and, by hypothesis, finitely many connected
components on each stratum; hence one index works globally. Exactness of
$\Gamma(U,-)$ identifies the
image of $H^i(U,K_m)\to H^i(U,K_n)$ with the sections of that image sheaf.
Consequently $(H^i(U,K_n))_n$ is Mittag–Leffler even when $U$ has
infinitely many connected components. The vanishing lemma now kills its
$\varprojlim{}^1$. The Milnor sequence is therefore the displayed
isomorphism, and uniform finite-level vanishing gives the last assertion.
