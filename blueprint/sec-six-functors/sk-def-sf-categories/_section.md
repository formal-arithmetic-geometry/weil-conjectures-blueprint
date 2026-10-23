+++
id = "sk-def-sf-categories"
kind = "definition"
title = "Ambient categories and small subcategories"
order = 3325
uses = ["sk-def-purity-conv", "sk-prop-sf-open-closed-triangle", "sk-def-sfb-constructible", "sk-prop-integral-criterion"]
tags = ["sketch"]
+++
Fix a scheme $T$ and an admissible coefficient ring
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$ of [def-sf-setting],
regarded as a condensed ring, with coefficient sheaf
$\Lambda_T=p_T^*\Lambda$ on the small pro-étale site
([det-def-sfb-pulled-back-coefficients]). The *ambient* categories are the
ordinary derived categories of $\Lambda_T$-modules on $T_{\mathrm{pro\acute et}}$
([det-def-sfb-derived-categories])

$$
D(T,\Lambda)=D(T_{\mathrm{pro\acute et}},\Lambda),\quad D^+(T,\Lambda),\quad D^-(T,\Lambda),\quad D^b(T,\Lambda),
$$

together with, for a set of primes $P$ invertible on $T$, the full
subcategory $D^+_{P\text{-tor}}(T,\Lambda)$ of complexes whose geometric
stalks are torsion with prime divisors in $P$
(sbc-def-derived-categories-with-allowable-torsion). The *small*
categories are the full subcategories

$$
\Dbc(T,\Lambda)\subseteq D^b(T,\Lambda),\qquad
\Dctf(T,\Lambda)\subseteq\Dbc(T,\Lambda),\qquad
D_c^{[a,b]}(T,\Lambda)\subseteq\Dbc(T,\Lambda)
$$

of bounded complexes with constructible cohomology sheaves, of those of
finite Tor amplitude over $\Lambda_T$, and of those with cohomology
concentrated in $[a,b]$ ([sk-def-sfb-constructible],
[det-def-sfb-bounded-constructible]). For $\Lambda=\mathcal O_E,E,\Qlb$ one has
$\Dctf=\Dbc$ ([lem-integral-ctf-equals-bc]).

For finite $\Lambda=A_{E,n}$, and only there, the same definitions may be read
on the small étale site of def:weil-pbc-etale-site, with
$\Dbc(T_{\mathrm{\acute et}},A)$, $\Dctf(T_{\mathrm{\acute et}},A)$ and
$D_c^{[a,b]}(T_{\mathrm{\acute et}},A)$ as in
def:weil-finite-torsion-constructibility, def:weil-finite-tor-amplitude and
def:weil-constructible-intervals; the comparison $\nu_T^*$ identifies them
with the pro-étale categories above ([def-sf-setting]).
