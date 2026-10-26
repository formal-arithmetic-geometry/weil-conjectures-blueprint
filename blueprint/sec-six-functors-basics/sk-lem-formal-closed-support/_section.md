+++
id = "sk-lem-formal-closed-support"
kind = "lemma"
title = "Sections with support in a closed subscheme"
order = 2132
uses = ["sk-lem-coefficient-heart", "sk-prop-sf-open-closed-triangle"]
tags = ["sketch"]
+++
[sk-lem-coefficient-heart] (3) gives a constructible sheaf with coefficients $E$ or $\Qlb$ a
finite filtration whose subquotients are of the form $a_!L$, with $a\colon S\hookrightarrow X$
locally closed and $L$ lisse on $S$. To reduce statements about $R\operatorname{Hom}(a_!L,-)$
to cohomology on $S$ we use the functor $R\underline\Gamma_Z$ of sections with support in a
closed subscheme $Z$.

Let $\Lambda$ be admissible, and let $i\colon Z\hookrightarrow X$ be a closed immersion with
open complement $j\colon V\hookrightarrow X$. For a sheaf $M$ of $\Lambda_X$-modules on
$X_{\mathrm{proét}}$ let $\underline\Gamma_Z(M)=i^*\ker(M\to j_*j^*M)$, the sheaf on $Z$ of
sections of $M$ with support in $Z$, and let
$R\underline\Gamma_Z\colon D(X_{\mathrm{proét}},\Lambda)\to D(Z_{\mathrm{proét}},\Lambda)$ be its
right derived functor.

1. $R\underline\Gamma_Z$ is right adjoint to the direct image $i_*$ from
   $D(Z_{\mathrm{proét}},\Lambda)$ to $D(X_{\mathrm{proét}},\Lambda)$, also in the form
   $R\operatorname{Hom}_X(i_*A,K)=R\operatorname{Hom}_Z(A,R\underline\Gamma_ZK)$, and
   $$
   R\underline\Gamma_ZK=i^*\fib\bigl(K\longrightarrow Rj_*j^*K\bigr)\quad\text{in }D(Z_{\mathrm{proét}},\Lambda).
   $$
2. Let $a=i\circ u\colon S\hookrightarrow X$ with $u\colon S\hookrightarrow Z$ an open immersion,
   and let $L$ be a finite locally projective $\Lambda_S$-module with dual $L^\vee$. Then
   naturally in $K\in D(X_{\mathrm{proét}},\Lambda)$
   $$
   R\operatorname{Hom}_X(a_!L,K)=R\Gamma\bigl(S,L^\vee\otimes u^*R\underline\Gamma_ZK\bigr).
   $$
