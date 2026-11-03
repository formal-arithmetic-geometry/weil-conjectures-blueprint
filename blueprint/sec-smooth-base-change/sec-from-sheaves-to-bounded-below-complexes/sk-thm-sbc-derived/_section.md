+++
id = "sk-thm-sbc-derived"
kind = "theorem"
title = "Smooth base change for classical torsion complexes"
order = 414
uses = ["sk-def-bc", "sk-thm-smooth-base-change", "sk-lem-sbc-exchange-compatibility", "sk-thm-pe-direct-image-comparison", "sk-cor-pe-classical-derived"]
tags = ["sketch"]
+++
In (9.1), let $g$ be smooth and $f$ quasi-compact and
quasi-separated. Let $\Lambda$ be a discrete commutative ring
annihilated by an integer $n$ invertible on $Y$. For every

$$
K\in D^+_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\Lambda)
$$

the canonical map (9.2) is an isomorphism.

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
