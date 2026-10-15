+++
id = "sk-lem-sp-p1"
kind = "lemma"
title = "The projective-line adjunction"
order = 1821
uses = ["sk-prop-geo-p1-adjunction", "sk-lem-geo-p1-cohomology", "sk-lem-geo-cartier"]
tags = ["sketch"]
+++
Fix $n\ge1$ and let $q:\mathbf P^1_S\to S$ be the projection. By
[sk-lem-geo-p1-cohomology], the unit and $c_1(\mathcal O_{\mathbf P^1_S}(1))$ give
an isomorphism in $D(S_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$, compatible with base
change,

$$
Rq_*(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S}\simeq(\mathbf Z/\ell^n\mathbf Z)_S\oplus(\mathbf Z/\ell^n\mathbf Z)_S(-1)[-2],
$$

and the *trace map*
$\operatorname{Tr}_q:Rq_*(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S}(1)[2]\to(\mathbf Z/\ell^n\mathbf Z)_S$
is the projection onto the twisted second summand; it sends
$c_1(\mathcal O_{\mathbf P^1_{\bar s}}(1))$ on each geometric fibre to $1$. Let
$\Delta$ be the diagonal of $\mathbf P^1_S\times_S\mathbf P^1_S$, cut out by
$x_0y_1-x_1y_0$, and $p_1,p_2$ the projections. [sk-lem-geo-cartier] gives its
cycle class
$\delta:\Delta_*(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S}\to(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]$,
the Kummer boundary of $\mathcal O(\Delta)$ with its canonical section,
compatible with every base change on $S$. With $\operatorname{Tr}_{p_i}$ the
pullback of $\operatorname{Tr}_q$, the diagonal integrates to $1$ along either
factor: $\operatorname{Tr}_{p_i}\circ Rp_{i*}\delta=\mathrm{id}$ for $i=1,2$.

**Lemma.** The functor
$Rq_*:\Dctf(\mathbf P^1_{S,\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)\to\Dctf(S_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$
is left adjoint to $K\mapsto q^*K(1)[2]$. The counit is integration along the
fibres,

$$
\varepsilon_K:Rq_*\bigl(q^*K(1)[2]\bigr)\simeq K\otimes^{\mathbf L}Rq_*(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S}(1)[2]
\xrightarrow{\ \mathrm{id}_K\otimes\operatorname{Tr}_q\ }K,
$$

and the unit is the class of the diagonal,

$$
\eta_M:M\simeq Rp_{2*}\Delta_*M\xrightarrow{\ Rp_{2*}(\delta\otimes p_1^*M)\ }Rp_{2*}p_1^*M(1)[2]\simeq q^*Rq_*M(1)[2],
$$

using the projection formulas and proper base change. Both commute with base
change on $S$.
