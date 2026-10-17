+++
id = "sk-thm-sbc-karoubian"
kind = "theorem"
title = "Bounded t-structures on the condensed constructible categories"
order = 1444
uses = ["sk-def-sfb-bounded-constructible", "sk-lem-int-integral-heart", "sk-lem-coefficient-heart", "sk-cor-coefficient-heart-ii", "sk-prop-sfb-finite-extension-compatibility", "sk-prop-sfb-qlbar-colimit-x", "prop-weil-heart-abelian", "lem-weil-heart-short-exact-triangles"]
tags = ["sketch"]
+++
Let $T$ be a standing scheme, $E/\Ql$ a finite extension inside $\Qlb$, and
$\Lambda\in\{\mathcal O_E,E,\Qlb\}$, regarded as a condensed ring. The
condensed category $\Dbc(T,\Lambda)\subset D(T_{\Proet},\Lambda)$
([sk-def-sfb-bounded-constructible]) carries a bounded t-structure, the
restriction of the standard one, with heart $\Cons(T,\Lambda)$, and it is
idempotent complete.

1. *The t-structure restricts.* $\Dbc(T,\Lambda)$ is a triangulated
subcategory of $D(T_{\Proet},\Lambda)$ ([sk-lem-int-integral-heart] (1) for
$\mathcal O_E$, [sk-cor-coefficient-heart-ii] for $E$ and $\Qlb$). For
$K\in\Dbc(T,\Lambda)$ the standard truncations $\tau^{\le m}K$ and
$\tau^{\ge m}K$, computed in $D(T_{\Proet},\Lambda)$, have as cohomology sheaves
either $H^i(K)$ or $0$; they are therefore bounded with constructible
cohomology and lie in $\Dbc(T,\Lambda)$. So the standard t-structure restricts
to $\Dbc(T,\Lambda)$, and it is bounded because every object is bounded. Its
heart consists of the complexes concentrated in degree $0$, that is of the
constructible $\Lambda_T$-modules $\Cons(T,\Lambda)$, an abelian subcategory of
$\Mod(T_{\Proet},\Lambda)$ with exact inclusion ([sk-lem-int-integral-heart]
(1), [sk-lem-coefficient-heart] (1)). Extension of scalars along
$\mathcal O_E\to E\to F\to\Qlb$ is flat ($E_T=\mathcal O_{E,T}[1/\ell]$ by
[sk-prop-sfb-qlbar-colimit-x], and [sk-prop-sfb-finite-extension-compatibility]),
hence t-exact for these t-structures.
1. *Idempotent completeness is automatic.* The ambient category
$D(T_{\Proet},\Lambda)$ has countable coproducts, so it is idempotent complete.
A full triangulated subcategory closed under direct summands is then
idempotent complete as well. $\Dbc(T,\Lambda)$ is closed under direct
summands: if $K\cong K'\oplus K''$, each $H^i(K')$ is the image of an
idempotent endomorphism of the constructible sheaf $H^i(K)$, hence
constructible since $\Cons(T,\Lambda)$ is closed under kernels and cokernels.
No Karoubi envelope is needed.

As for any t-structure, the heart is abelian ([prop-weil-heart-abelian]) and
short exact sequences in it are distinguished triangles
([lem-weil-heart-short-exact-triangles]).
