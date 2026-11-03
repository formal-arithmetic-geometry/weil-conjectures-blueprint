+++
kind  = "proof"
of    = "lem-trf-open-square-exchange"
+++
Restriction along an open immersion is localization of the site:
an object $V\to U$ is also an object over $Y$.
For a sheaf $Q$ on $Y'$, the direct-image formula gives

$$
(j^*g_*Q)(V)=Q(V\times_Y Y')
=(g_{U*}j'^*Q)(V).
$$

The equality respects restrictions and coverings on the site of
[def-weil-pbc-proetale-site]. Thus $j^*g_*=g_{U*}j'^*$,
with all comparison maps specified on sections.

The exact functor $j'^*$ preserves injectives and K-injectives:
its left adjoint $j'_!$ is exact by
[def-weil-extension-by-zero]. For K-injectives this follows
directly by applying the adjunction to Hom complexes against an
acyclic complex. Thus a K-injective resolution of $Q$ computes
both sides of

$$
j^*Rg_*Q\simeq Rg_{U*}j'^*Q,
$$

using [def-weil-derived-direct-image]. Taking left adjoints,
with the exact inverse-image pullbacks of
[def-weil-derived-pullback-tensor-hom], gives
$Lg^*j_!\simeq j'_!Lg_U^*$. This defines $b_g$.
On $U'$ the section equality is the identity, so its mate has the
stated normalization. The section equalities for two pasted squares
compose to the equality for the outer square. The uniqueness of
left adjoints with their adjunction data proves the pasting and
identity assertions. This proof uses no claim that ordinary
geometric stalks detect arbitrary pro-etale sheaves.
