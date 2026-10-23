+++
id = "det-lem-formal-closed-support-stratum"
kind = "lemma"
title = "Hom out of an extension by zero from a stratum"
order = 2156
uses = ["det-lem-formal-closed-support-derived", "sk-lem-coefficient-heart"]
+++
In the situation of [det-lem-formal-closed-support-derived], let
$u\colon S\hookrightarrow Z$ be an open immersion, $a=i\circ u\colon S\hookrightarrow X$,
and $a_!=i_*u_!$ (as in [sk-lem-coefficient-heart]). Let $L$ be a finite
locally projective $\Lambda_S$-module with dual
$L^\vee=\mathcal Hom_{\Lambda_S}(L,\Lambda_S)$. Then, naturally in
$K\in\D(X_{\mathrm{proét}},\Lambda)$,

$$
R\operatorname{Hom}_X(a_!L,K)\simeq R\operatorname{Hom}_Z(u_!L,R\underline\Gamma_ZK)
\simeq R\operatorname{Hom}_S(L,u^*R\underline\Gamma_ZK)
\simeq R\Gamma\bigl(S,L^\vee\otimes u^*R\underline\Gamma_ZK\bigr).
$$

In particular $\Hom_{\D(X_{\mathrm{proét}},\Lambda)}(a_!L,K[q])=H^q(S,L^\vee\otimes u^*R\underline\Gamma_ZK)$
for every $q$.
