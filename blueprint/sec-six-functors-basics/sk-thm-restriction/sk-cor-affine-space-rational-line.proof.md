+++
kind = "proof"
of = "det-cor-affine-space-rational-line"
+++
(1) $j^*$ and $j_!$ are exact and preserve direct sums on the ambient
pro-étale derived categories, and they preserve $\Dbc$ (pullback and extension
by zero of a lisse sheaf on a stratum are again of this form). So the full
subcategories of objects sent into $\Loc(\Dbc)$ are localizing and contain
$\Dbc$, hence $j_!$ and $j^*$ preserve the localizing categories. The
adjunction $j_!\dashv j^*$ on the ambient categories restricts to these full
subcategories.

(2) $p=q\circ j$ is a compactification of $p$ with $q$ proper, and $Rp_!$ on
the localizing categories is defined by compactifications
([sk-prop-sf-existence]), so $Rp_!\simeq Rq_*\circ j_!$.

(3) By [sk-prop-p1-adjunction-rational], $Rq_*\dashv q^*(1)[2]$ on the
localizing categories. Composing adjunctions, $Rq_*j_!\dashv j^*q^*(1)[2]$,
and $j^*q^*=(qj)^*=p^*$; the Tate twist and shift commute with $j^*$. So
$Rp_!\dashv p^*(1)[2]$. Since $p^!$ is also right adjoint to $Rp_!$, the
uniqueness of right adjoints gives a unique isomorphism
$p^!\simeq p^*(1)[2]$ compatible with the counits. (This is the
$\ell$-adic analogue of [cor-amb-affine-space-adjunction] for $d=1$.)
