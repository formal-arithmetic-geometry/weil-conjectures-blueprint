+++
id = "sk-prop-geo-p1-adjunction"
kind = "proposition"
title = "The projective-line adjunction"
order = 2357
uses = ["sk-lem-geo-p1-cohomology", "sk-lem-geo-cartier"]
tags = ["sketch"]
+++
Let $S$ and $p:\mathbf P^1_S\to S$ be as in [sk-lem-geo-p1-cohomology], and
assume in addition that $S$ is of finite type over the standing field $k$. The
functors
$Rp_*\colon D_{\mathrm{class}}((\mathbf P^1_S)_{\mathrm{proét}},\Lambda)\to D_{\mathrm{class}}(S_{\mathrm{proét}},\Lambda)$
and
$p^*(1)[2]\colon D_{\mathrm{class}}(S_{\mathrm{proét}},\Lambda)\to D_{\mathrm{class}}((\mathbf P^1_S)_{\mathrm{proét}},\Lambda)$
form an adjunction

$$
Rp_* \ \dashv\ p^*(1)[2],
\qquad\text{(G4)}
$$

with unit (G6) and counit (G7) below: for $M$ on $\mathbf P^1_S$ the unit is

$$
\eta_M:M=Rp_{2*}\Delta_*M\xrightarrow{Rp_{2*}(\delta\otimes p_1^*M)}Rp_{2*}\bigl(p_1^*M(1)[2]\bigr)\xrightarrow{\ \sim\ }p^*Rp_*M(1)[2],
\qquad\text{(G6)}
$$

where $p_1,p_2:\mathbf P^1_S\times_S\mathbf P^1_S\to\mathbf P^1_S$ are the
projections, $\Delta$ is the diagonal, $\delta:\Delta_*\Lambda\to\Lambda(1)[2]$
is its cycle class ([sk-lem-geo-cartier]) and the last arrow is proper base
change; for $N$ on $S$ the counit is

$$
\epsilon_N:Rp_*\bigl(p^*N(1)[2]\bigr)\xrightarrow{\ \sim\ }N\otimes_\Lambda^{\mathbf L}Rp_*\Lambda_{\mathbf P^1_S}(1)[2]\xrightarrow{1\otimes\operatorname{Tr}_p}N,
\qquad\text{(G7)}
$$

the first arrow being the projection formula and $\operatorname{Tr}_p$ the
trace (G3). Both are compatible with base change in the standing range (as
natural transformations of functors between the categories over $S'$, for
$g:S'\to S$) and with change of finite coefficients.

*Complement.* The triangle identities rest on the diagonal integrals (G5):
with $\operatorname{Tr}_{p_a}$ the base change of $\operatorname{Tr}_p$ along
$p_a$, one has $\operatorname{Tr}_{p_a}\circ Rp_{a*}\delta=\mathrm{id}_{\Lambda_{\mathbf P^1_S}}$
for $a=1,2$. Moreover both functors preserve the subcategories of constructible
complexes of finite Tor amplitude, so for $\Lambda=\mathbf Z/\ell^n\mathbf Z$ the
adjunction (G4), with the same unit and counit, restricts to
$Rp_*:\Dctf(\mathbf P^1_{S,\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)\rightleftarrows\Dctf(S_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z):p^*(-)(1)[2]$.
