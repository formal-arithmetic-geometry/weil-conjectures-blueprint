+++
id = "cor-pur-p1-purity"
kind = "theorem"
title = "Projective-line purity"
order = 2070
tags = ["latex:corollary"]
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-p1-integration", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "thm-pur-p1-decomposition", "thm-pur-p1-triangular", "thm-pur-td-criterion"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $Y$ be separated finite type and $q:\mathbf P^1_Y\to Y$. For
every $K\in D^b_{ctf}(Y,\Lambda)$ there is a canonical isomorphism

$$
Rq^!K\;\cong\;Lq^*K(1)[2],
$$

compatible with base change, and

$$
\omega_q=Rq^!\Lambda_Y\;\cong\;\Lambda_{\mathbf P^1_Y}(1)[2].
$$

## Proof

By [thm-pur-p1-triangular] the two triangular composites for
$(q,L_P)$ are the identity, so
[thm-pur-td-criterion] applies and gives
$Rq_!\dashv G_{L_P}$, hence $Rq^!(-)\cong Lq^*(-)\otimes^L L_P$
and $\omega_q\cong L_P$; the twist identifications of
[def-coefficient-twists-detailed] give the displayed form.
