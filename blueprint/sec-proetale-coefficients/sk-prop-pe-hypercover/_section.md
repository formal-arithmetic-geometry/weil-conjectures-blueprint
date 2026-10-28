+++
id = "sk-prop-pe-hypercover"
kind = "proposition"
title = "Weakly contractible hypercovers"
order = 998
uses = ["sk-thm-pe-weakly-contractible-basis", "sk-cor-pe-wc-sections", "sk-prop-pe-left-complete"]
tags = ["sketch"]
+++
For bounded-below complexes, weakly contractible objects give explicit cochain complexes
computing cohomology.

Let $U$ be a quasi-compact, quasi-separated object of $X_{\mathrm{proét}}$. There is a
hypercover $W_\bullet\to U$ whose term in every simplicial degree is one affine weakly
contractible object. If $K\in D^+(X_{\mathrm{proét}},\mathcal R)$ is represented by a
complex $K^\bullet$ vanishing below degree $a$, then

$$
R\Gamma(U,K)\simeq\operatorname{Tot}\bigl(K^b(W_r)\bigr)_{r\geq0,\ b\geq a}.
$$

The cosimplicial differential is the alternating sum of pullbacks along face maps, combined
with $(-1)^r$ times the differential of $K^\bullet$. In total degree $q$ this complex has the
finite sum $\bigoplus_{0\leq r\leq q-a}K^{q-r}(W_r)$.

For a single sheaf this is the cochain complex $M(W_0)\to M(W_1)\to M(W_2)\to\cdots$, which
may be nonzero in every degree, so the hypercover gives no bound on cohomological dimension.
The sum in each total degree is finite because $K^\bullet$ is bounded below. For unbounded
$K$ the correct formula is $R\Gamma(U,K)\simeq R\varprojlim_nR\Gamma(U,\tau_{\geq-n}K)$, by
[sk-prop-pe-left-complete], and the hypercover complex is applied to each truncation.
