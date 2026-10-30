+++
id = "sk-lem-formal-closed-support"
kind = "lemma"
title = "Sections with support in a closed subscheme"
order = 245
uses = ["sk-prop-sf-open-closed-triangle", "sk-lem-coefficient-heart"]
tags = ["sketch"]
+++
Let $\Lambda$ be admissible, let $i:Z\hookrightarrow X$ be a
closed immersion with open complement $j:V\hookrightarrow X$, and let
$R\underline\Gamma_Z:D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(Z_{\mathrm{pro}\acute{e}t},\Lambda)$ be the
local cohomology functor of Section [sec-pe-localization-completion],

$$
R\underline\Gamma_Z K=i^*\fib(K\longrightarrow Rj_*j^*K).
$$

For a sheaf $M$ of $\Lambda_X$-modules on $X_{\mathrm{pro}\acute{e}t}$, let
$\underline\Gamma_Z(M)=i^*\ker(M\to j_*j^*M)$, the sheaf on $Z$ of
sections of $M$ with support in $Z$.

1. $R\underline\Gamma_Z$ is the right derived functor of
   $\underline\Gamma_Z$, and its adjunction with the direct image
   $i_*:D(Z_{\mathrm{pro}\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ holds in
   the form $R\!\operatorname{Hom}_X(i_*N,K)=R\!\operatorname{Hom}_Z(N,R\underline\Gamma_ZK)$.
2. Let $a=i\circ u:S\hookrightarrow X$ with $u:S\hookrightarrow Z$ an
   open immersion, and let $L$ be a finite locally projective
   $\Lambda_S$-module with dual $L^\vee$. Then naturally in
   $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$

$$
R\!\operatorname{Hom}_X(a_!L,K)
=R\Gamma\bigl(S,L^\vee\otimes u^*R\underline\Gamma_ZK\bigr).
\tag{5.1}
$$
