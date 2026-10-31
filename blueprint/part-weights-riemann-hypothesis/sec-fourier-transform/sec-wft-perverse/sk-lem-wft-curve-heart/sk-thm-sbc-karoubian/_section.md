+++
id = "sk-thm-sbc-karoubian"
kind = "theorem"
title = "Bounded t-structures on the condensed constructible categories"
order = 2222
uses = ["sk-prop-sf-open-closed-triangle", "sk-prop-sfb-qlbar-colimit-x", "prop-weil-heart-abelian", "lem-weil-heart-short-exact-triangles"]
+++
Let $T$ be a standing scheme, $E/\Ql$ a finite extension inside $\Qlb$, and
$\Lambda\in\{\mathcal O_E,E,\Qlb\}$, regarded as a condensed ring. The
condensed category $\Dbc(T,\Lambda)\subset D(T_{\Proet},\Lambda)$
([det-def-sfb-bounded-constructible]) carries a bounded t-structure, the
restriction of the standard one, with heart $\Cons(T,\Lambda)$, and it is
idempotent complete.

1. *The t-structure restricts.* $T$ is of finite type over $k$, hence
topologically Noetherian, so $\Dbc(T,\Lambda)$ is a triangulated
subcategory of $D(T_{\Proet},\Lambda)$ ([det-def-sfb-bounded-constructible]). For
$K\in\Dbc(T,\Lambda)$ the standard truncations $\tau^{\le m}K$ and
$\tau^{\ge m}K$, computed in $D(T_{\Proet},\Lambda)$, have as cohomology sheaves
either $H^i(K)$ or $0$; they are therefore bounded with constructible
cohomology and lie in $\Dbc(T,\Lambda)$. So the standard t-structure restricts
to $\Dbc(T,\Lambda)$, and it is bounded because every object is bounded. Its
heart consists of the complexes concentrated in degree $0$, that is of the
constructible $\Lambda_T$-modules $\Cons(T,\Lambda)$. Kernels and cokernels in
the heart are computed in $\Mod(T_{\Proet},\Lambda)$: for $f\colon A\to B$ in
$\Cons(T,\Lambda)$ with cone $S\in\Dbc(T,\Lambda)$, they are $H^{-1}(S)=\ker f$
and $H^0(S)=\operatorname{coker}f$ ([lem-weil-heart-short-exact-triangles] (3)),
the kernel and cokernel of $f$ as sheaves, and these are constructible because
$S\in\Dbc(T,\Lambda)$. Hence $\Cons(T,\Lambda)$ is closed under kernels and
cokernels in $\Mod(T_{\Proet},\Lambda)$, an abelian subcategory with exact
inclusion. Extension of scalars along $\mathcal O_E\to E\to F\to\Qlb$ is
flat: $E_T=\mathcal O_{E,T}[1/\ell]$ and $\overline{\mathbf Q}_{\ell,T}\cong\varinjlim_F F_T$ are
filtered colimits ([sk-prop-sfb-qlbar-colimit-x]), and $F\cong E^{[F:E]}$ as
condensed $E$-modules, so $F_T\cong E_T^{[F:E]}$ is free, $p_T^*$ preserving
finite direct sums ([det-def-sfb-pulled-back-coefficients]). Hence extension of
scalars is t-exact for these t-structures.
1. *Idempotent completeness is automatic.* The ambient category
$D(T_{\Proet},\Lambda)$ has countable coproducts, so it is idempotent complete
([Stacks, Tag 05QW](https://stacks.math.columbia.edu/tag/05QW)).
A full triangulated subcategory closed under direct summands is then
idempotent complete as well. $\Dbc(T,\Lambda)$ is closed under direct
summands: if $K\cong K'\oplus K''$, each $H^i(K')$ is the image of an
idempotent endomorphism of the constructible sheaf $H^i(K)$, hence
constructible since $\Cons(T,\Lambda)$ is closed under kernels and cokernels.
No Karoubi envelope is needed.

As for any t-structure, the heart is abelian ([prop-weil-heart-abelian]) and
short exact sequences in it are distinguished triangles
([lem-weil-heart-short-exact-triangles]).
