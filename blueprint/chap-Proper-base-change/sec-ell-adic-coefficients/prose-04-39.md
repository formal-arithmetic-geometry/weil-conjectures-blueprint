+++
id = "prose-04-39"
kind = "hidden"
title = "$\\ell$-adic coefficients (1)"
order = 413
+++
Pro-étale proper base change
(Theorem [theorem-proper-base-change-classical-pro]) concerns
[classical](@definition-classical-pro-etale-sheaves) complexes with [torsion](@definition-torsion-sheaves) cohomology sheaves. For a finite ring $A$
it therefore applies, with $\Lambda=A$, to every $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,A)}$ for
schemes of finite type over $k$, because bounded [constructible](@definition-constructible-sheaves) complexes
on quasi-compact quasi-separated schemes are [classical](@definition-classical-pro-etale-sheaves)
(Theorem [theorem-comparison-constructible-sheaves]). For
$\mathcal O_E$, however, the theorem gives proper base change only at each finite
level $\mathcal O_E/\pi_E^n$, and we must pass to the limit. Later
statements of this kind make this passage once and for all, by the reduction
principle of Section [sec-Reduction-to-finite-coefficients]; here we make it directly.

The difficulty is completeness: the inverse image
$g^*:D(\href{@definition-small-pro-etale-site}{Y_{\mathrm{pro}\acute{e}t}},\mathcal O_E)\to D(\href{@definition-small-pro-etale-site}{Y'_{\mathrm{pro}\acute{e}t}},\mathcal O_E)$,
which is exact on sheaves of modules, need not preserve [derived
completeness](@definition-derived-adic-completeness). We therefore complete after pulling back.
