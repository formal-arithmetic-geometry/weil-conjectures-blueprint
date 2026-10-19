+++
kind  = "proof"
of    = "thm-pqf-immersion-descent"
+++
*Step 1: the descended open.* Each $T_\lambda$ is finite, hence affine,
over $S$ by [def-weil-pbc-scheme-conventions], so it is quasi-compact and
quasi-separated, and the transition morphisms, being $S$-morphisms between
schemes affine over $S$, are affine. The projection $N\to T_\lambda$ of a
filtered limit with affine transition morphisms is affine, hence
quasi-compact, so $N$ is quasi-compact, and so is $X$ because $\iota$ is
quasi-compact. Thus $V:=\iota(X)\subset N$ is a quasi-compact open
subscheme. By [pqf-lem-limit-qc-open-descends] there are an index
$\lambda_1$ and a quasi-compact open $U_{\lambda_1}\subset T_{\lambda_1}$
with $V=N\times_{T_{\lambda_1}}U_{\lambda_1}$; let $U_\lambda$ be the
preimage of $U_{\lambda_1}$ in $T_\lambda$ for $\lambda\ge\lambda_1$.
Clause (3) of the same lemma identifies $V$ with the filtered limit
$\varprojlim_{\lambda\ge\lambda_1}U_\lambda$, with affine transition
morphisms and quasi-compact $U_\lambda$, the projections being those of
$N$.

*Step 2: the immersion spreads out.* The morphism $\iota$ induces an
isomorphism $X\to V$, so $X$ is a closed subscheme of the limit
$\varprojlim_{\lambda\ge\lambda_1}U_\lambda$, and the composite
$X\to U_{\lambda_1}\to T_{\lambda_1}\to S$ is $\nu\circ\iota$, which is
locally of finite type by hypothesis. Hence
[pqf-lem-limit-immersion-descends] applies and the composite
$X\to U_\lambda$ is a closed immersion for all sufficiently large
$\lambda$. Fix such an index $\lambda_0\ge\lambda_1$.

*Step 3: factoring the immersion.* The composite
$h:X\to U_{\lambda_0}\hookrightarrow T_{\lambda_0}$ is an immersion,
and it is quasi-compact: for a quasi-compact open
$W\subset T_{\lambda_0}$ the intersection
$U_{\lambda_0}\cap W$ is quasi-compact by
[pqf-lem-qs-intersection-qc], since $T_{\lambda_0}$ is
quasi-separated and both $U_{\lambda_0}$ and $W$ are quasi-compact
opens, and $h^{-1}(W)=X\times_{U_{\lambda_0}}(U_{\lambda_0}\cap W)$ is
a closed subscheme of it — the base change of the closed immersion
$X\to U_{\lambda_0}$ — hence is quasi-compact. By the recorded input
Tag 01QV a quasi-compact immersion factors as an open immersion followed
by a closed immersion: there are a scheme $T$, an open immersion
$j:X\to T$ and a closed immersion $i:T\to T_{\lambda_0}$ with
$h=i\circ j$. In that construction $T$ is the closed subscheme of
$T_{\lambda_0}$ whose sheaf of ideals is the kernel of
$\mathcal O_{T_{\lambda_0}}\to h_*\mathcal O_X$, so that $X$ is the
fibre product $T\times_{T_{\lambda_0}}U_{\lambda_0}$ and $j$ is the
base change of the open immersion
$U_{\lambda_0}\hookrightarrow T_{\lambda_0}$ along the closed immersion
$i$; that open immersion is quasi-compact for the same reason as
$h$, and quasi-compactness is stable under base change, so $j$ is a
quasi-compact open immersion. By construction $i\circ j=h$ is the
composite $X\to N\to T_{\lambda_0}$.

*Step 4: the finitely presented stage.* If $S$ is locally Noetherian
([pqf-def-locnoeth]), then the finite morphism
$T_{\lambda_0}\to S$ is of finite presentation by
[pqf-lem-finite-fp-locnoeth].
