+++
id = "lem-sc-second-kummer-divisors"
kind = "lemma"
title = "Second Kummer cohomology without a dimension assumption"
order = 1588
uses = ["def-sc-curves", "def-sc-kummer-sequence", "def-sc-picard-group", "def-weil-pbc-etale-cohomology", "lem-sc-divisor-class-curve", "lem-sc-function-field-cd-one", "lem-sc-generic-kummer-residues", "lem-sc-smooth-normal", "thm-sp-grothendieck"]
+++
For a smooth separated curve $C$
over algebraically closed $k$ and $n>0$ invertible in $k$,

$$
H^2(C,\mu_n)\simeq\operatorname{Pic}(C)/n,
$$

where $\mu_n$, the Picard group, and cohomology are as in
[def-sc-kummer-sequence], [def-sc-picard-group], [def-weil-pbc-etale-cohomology].

## Proof

Work componentwise and write $K=k(C)$.
Normality ([lem-sc-smooth-normal]) gives
$\eta_*\mu_n=\mu_n$: on every normal etale test object an
$n$-th root of unity in its rational functions is integral,
and therefore regular. The low-degree exact sequence of
[thm-sp-grothendieck] is

$$
H^1(K,\mu_n)\longrightarrow H^0(C,R^1\eta_*\mu_n)
\longrightarrow H^2(C,\mu_n)\longrightarrow H^2(K,\mu_n).
$$

The last term is zero by [lem-sc-function-field-cd-one].
The first two terms and their arrow are

$$
K^\times/K^{\times n}\longrightarrow
\bigoplus_{x\in C_{\rm cl}}\mathbf Z/n,\qquad
f\longmapsto (v_x(f)\bmod n)_x,
$$

by [lem-sc-generic-kummer-residues].
The cokernel is the divisor group modulo principal divisors
and $n$ times the divisor group. This is
$\operatorname{Pic}(C)/n$ by [lem-sc-divisor-class-curve].
