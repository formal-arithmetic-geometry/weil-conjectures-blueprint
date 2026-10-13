+++
id = "prop-sf-closed-immersion-unit"
kind = "theorem"
title = "The closed-immersion exceptional unit"
order = 2204
tags = ["latex:proposition"]
uses = ["def-weil-ambient-exceptional-adjoint", "def-weil-exceptional-inverse-image", "def-weil-open-closed-recollement", "def-weil-scheme-morphism-properties", "lem-exc-proetale-closed-exact", "lem-exc-proetale-closed-support", "prop-weil-open-closed-recollement-adjunctions"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$, an integer $n\in\mathbf
Z_{\geq1}$, and put $A=A_{E,n}$. Let $T$ be a Noetherian scheme on which
$\ell$ is invertible (for instance a finite-type scheme over a field in which
$\ell$ is invertible), and let $i:Z\hookrightarrow T$ be a closed immersion
[def-weil-scheme-morphism-properties], with complementary
open immersion $j$, as in the open-closed recollement
[def-weil-open-closed-recollement]. Let $Ri^!$ be the right adjoint of the
direct image $i_*=Ri_*$ on the ambient ordinary derived categories of the
small pro-etale sites, as in [lem-exc-proetale-closed-support]. Then for
every $Q\in D(Z_{\mathrm{proet}},A)$ the adjunction unit is an isomorphism

$$
Q\xrightarrow{\ \eta_i^!\ }Ri^!Ri_*Q .
$$

No boundedness or constructibility of $Q$ is required. In particular, for the
constructible exceptional adjoint $Ri^!$ of
[def-weil-exceptional-inverse-image] — which exists without the ambient datum
of [def-weil-ambient-exceptional-adjoint], that datum being false in general —
computed with the compactification
$Z\xrightarrow{\mathrm{id}}Z\xrightarrow{i}T$ so that $Ri_{!,n}=Ri_*$,
for $Q\in D^b_c(Z,A)$ the unit of the adjunction
$\Hom_T(Ri_!K,L)\cong\Hom_Z(K,Ri^!L)$ of
[def-weil-exceptional-inverse-image] is an isomorphism
$Q\xrightarrow{\sim}Ri^!Ri_*Q$.
