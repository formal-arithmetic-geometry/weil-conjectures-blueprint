+++
id = "sk-p-local"
kind = "proposition"
title = "Decomposition into local terms"
order = 3809
uses = ["sk-d-corr", "sk-d-integral", "sk-d-local-term", "sk-d-pairing", "sk-p-pairing", "sk-thm-sf-package"]
tags = ["sketch"]
+++
Let $E$ be proper over $s$ and suppose $E$ is a finite disjoint union
$E=\coprod_{\beta\in B}\beta$ of clopen subschemes, i.e. a finite family of open
immersions with closed, pairwise disjoint images covering $E$. Then for every
Borel–Moore section $\alpha:A_E\to\omega_E$ the integral is the sum of the
local terms:

$$
\int_E\alpha=\sum_{\beta\in B}\LT_\beta(\alpha).
$$

In particular, for the intersection support of an opposite pair,
$\int_E\langle u,v\rangle_{\mathrm{LV}}=\sum_{\beta\in B}\LT_\beta(u,v)$.
