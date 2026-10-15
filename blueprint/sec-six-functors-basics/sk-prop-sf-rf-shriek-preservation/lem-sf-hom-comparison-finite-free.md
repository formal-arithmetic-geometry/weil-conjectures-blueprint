+++
id = "lem-sf-hom-comparison-finite-free"
kind = "lemma"
title = "The internal-Hom comparison for a bounded free model"
order = 2427
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-pbc-constructible-complexes", "def-weil-pbc-site-comparison-morphism", "def-weil-site-perfect-complex", "lem-sf-hom-finite-projective"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, an integer
$n\geq1$, $A=A_{E,n}$, and let $T$ be a scheme on which $\ell$ is
invertible. Let $P'$ be a bounded complex of finite free
$A_{T,\Et}$-modules, so that $P'$ is
site-perfect in the sense of
[def-weil-site-perfect-complex], and let $N$ be a bounded complex of
$A$-module sheaves with constructible cohomology on the small étale site
of $T$, in the sense of
[def-weil-pbc-constructible-complexes]. For the comparison morphism
$\nu_T:T_{\Proet}\to T_{\Et}$ of
[def-weil-pbc-site-comparison-morphism] the comparison map of
[def-weil-derived-pullback-tensor-hom],

$$
\nu_T^*R\mathcal H om_A(P',N)\longrightarrow
R\mathcal H om_A(\nu_T^*P',\nu_T^*N),
$$

is an isomorphism.
