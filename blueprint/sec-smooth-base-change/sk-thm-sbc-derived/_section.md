+++
id = "sk-thm-sbc-derived"
kind = "theorem"
title = "Smooth base change for classical torsion complexes"
order = 2213
uses = ["sk-def-bc", "sk-thm-smooth-base-change", "sk-lem-sbc-exchange-compatibility", "sk-thm-pe-direct-image-comparison", "sk-cor-pe-classical-derived"]
tags = ["sketch"]
+++
Consider a cartesian square with $u:X'\to X$, $f':X'\to Y'$, $f:X\to Y$, $g:Y'\to Y$, and
the exchange map $\operatorname{Ex}_{g,f}(K):g^*Rf_*K\to Rf'_*u^*K$ of
[sk-lem-sbc-exchange-compatibility].
Let $g$ be smooth and $f$ quasi-compact and
quasi-separated. Let $\Lambda$ be a discrete commutative ring
annihilated by an integer $n$ invertible on $Y$. For every

$$
 K\in D^+_{\mathrm{class}}(X_{\mathrm{pro\acute et}},\Lambda)
$$

the canonical map $\operatorname{Ex}_{g,f}(K)$ is an isomorphism in
$D^+_{\mathrm{class}}(Y'_{\mathrm{pro\acute et}},\Lambda)$.

In particular, for a classical $\Lambda$-module sheaf $F$ and all $q$,

$$
 g^*R^qf_*F\xrightarrow{\sim}R^qf'_*u^*F.
$$

*Complement.* In the Cartesian square of the complement of [sk-thm-smooth-base-change], with
$f$ smooth and $g$ quasi-compact and quasi-separated, let $\mathcal P$ be the set of primes
invertible on the base. The base-change map of [sk-def-bc] is an isomorphism

$$
Lf^*Rg_*K\xrightarrow{\ \sim\ }Rh_*Le^*K
$$

for bounded constructible $K$ ([sbc-thm-bounded-derived-smooth-base-change]),
for bounded $\mathcal P$-torsion $K$ ([sbc-thm-bounded-allowable-torsion]), and
for every $K\in D^+_{\mathcal P\text{-tor}}(T_{\Et})$
([sbc-thm-bounded-below-derived-smooth-base-change]).
