+++
id = "sk-lem-formal-closed-support"
kind = "lemma"
title = "Sections with support in a closed subscheme"
order = 2279
uses = ["sk-prop-sf-open-closed-triangle", "sk-lem-coefficient-heart"]
tags = ["sketch"]
+++
Let $\Lambda$ be admissible, let $i\colon Z\hookrightarrow X$ be a closed immersion with open
complement $j\colon V\hookrightarrow X$, and let
$R\underline\Gamma_Z\colon D(X_{\mathrm{proét}},\Lambda)\to D(Z_{\mathrm{proét}},\Lambda)$ be the
local cohomology functor of [sk-prop-sf-open-closed-triangle],
$$
R\underline\Gamma_ZK=i^*\fib\bigl(K\longrightarrow Rj_*j^*K\bigr).
$$
For a sheaf $M$ of $\Lambda_X$-modules on $X_{\mathrm{proét}}$, let
$\underline\Gamma_Z(M)=i^*\ker(M\to j_*j^*M)$, the sheaf on $Z$ of sections of $M$ with support
in $Z$.

1. $R\underline\Gamma_Z$ is the right derived functor of $\underline\Gamma_Z$, and its adjunction
   with the direct image $i_*\colon D(Z_{\mathrm{proét}},\Lambda)\to D(X_{\mathrm{proét}},\Lambda)$
   holds in the form
   $R\operatorname{Hom}_X(i_*N,K)=R\operatorname{Hom}_Z(N,R\underline\Gamma_ZK)$.
2. Let $a=i\circ u\colon S\hookrightarrow X$ with $u\colon S\hookrightarrow Z$ an open immersion,
   and let $L$ be a finite locally projective $\Lambda_S$-module with dual $L^\vee$. Then
   naturally in $K\in D(X_{\mathrm{proét}},\Lambda)$, with $a_!$ as in [sk-lem-coefficient-heart],
   $$
   R\operatorname{Hom}_X(a_!L,K)=R\Gamma\bigl(S,L^\vee\otimes u^*R\underline\Gamma_ZK\bigr).
   $$
