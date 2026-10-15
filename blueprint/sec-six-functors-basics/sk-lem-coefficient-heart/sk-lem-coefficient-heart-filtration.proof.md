+++
kind  = "proof"
of    = "det-lem-coefficient-heart-filtration"
+++
For an open immersion $v$, the counit $v_!v^*F\to F$ is injective (check on the open, where
it is the identity, and on the closed complement, where the source vanishes). For
$V_{k-1}\subseteq V_k$, the map $v_{k-1!}v_{k-1}^*F\to F$ factors through $v_{k!}v_k^*F$, so the
$F_k$ form an increasing chain of subsheaves with $F_0=0$ and $F_m=F$ (as $V_m=X$).

Let $w\colon V_{k-1}\hookrightarrow V_k$, with closed complement $S_k$ in $V_k$, and
$c\colon S_k\hookrightarrow V_k$. The localization sequence on $V_k$,
$$
0\to w_!w^*G\to G\to c_*c^*G\to0,\qquad G=v_k^*F,
$$
is exact (check on $V_{k-1}$ and on $S_k$, using $w^*w_!=\mathrm{id}$, $c^*w_!=0$,
$c^*c_*=\mathrm{id}$, $w^*c_*=0$ and [det-lem-coefficient-heart-common-stratification] (3)).
Apply the exact functor $v_{k!}$: since $v_{k!}w_!=v_{k-1!}$ and $v_{k!}c_*=a_{k!}$ (the
factorization $a_k=i\circ u$ through the closure and $v_k\circ c$ give the same extension by
zero, as both restrict to $F|_{S_k}$ on $S_k$ and to $0$ elsewhere), we get
$0\to F_{k-1}\to F_k\to a_{k!}(F|_{S_k})\to0$. Finally $F|_{S_k}$ is lisse by the choice of
the stratification ([det-lem-coefficient-heart-closure]).
