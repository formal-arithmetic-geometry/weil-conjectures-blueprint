+++
kind  = "proof"
of    = "pqf-lem-limit-qc-open-descends"
+++
*Affine pieces.* Let $W\subset S_i$ be an affine open. For $j\ge i$ its
preimage $W_j=f_{ji}^{-1}(W)\subset S_j$ is affine, being the preimage of
an affine open under the affine morphism $f_{ji}$, say
$W_j=\operatorname{Spec}R_j$, and $f_i^{-1}(W)=\varprojlim_{j\ge i}W_j$ is
affine with coordinate ring $R=\varinjlim_jR_j$: a filtered limit of affine
schemes with affine transition morphisms is the spectrum of the filtered
colimit of the coordinate rings. Every $g\in R$ is the image of some
$g_j\in R_j$, and then the principal open $D(g)\subset f_i^{-1}(W)$ equals
$f_j^{-1}(D(g_j))$ with $D(g_j)$ an affine open of $S_j$.

*A basis.* The opens $f_j^{-1}(W)$, with $j\in I$ and $W$ an affine open of
$S_j$, form a basis of the topology of $S$. Indeed, let $x\in U$ with
$U\subset S$ open. Fix an index $i$ and an affine open $W\ni f_i(x)$ of
$S_i$. The principal opens of the affine scheme $f_i^{-1}(W)$ form a basis
of it, so some $D(g)$ satisfies $x\in D(g)\subset U\cap f_i^{-1}(W)$, and by
the previous paragraph $D(g)=f_j^{-1}(D(g_j))$ with $D(g_j)$ affine.

*(1).* Since $V$ is quasi-compact, the basis gives finitely many indices
$i_1,\dots,i_m$ and affine opens $W_k\subset S_{i_k}$ with
$V=\bigcup_kf_{i_k}^{-1}(W_k)$. Choose $i\ge i_1,\dots,i_m$ and put
$V_i=\bigcup_kf_{ii_k}^{-1}(W_k)$. Each $f_{ii_k}^{-1}(W_k)$ is affine, so
$V_i$ is a quasi-compact open of $S_i$, and
$f_i^{-1}(V_i)=\bigcup_kf_{i_k}^{-1}(W_k)=V$.

*(2).* Choose $j\ge i,i'$ and replace $V_i$ and $V_{i'}$ by their preimages
in $S_j$; these are quasi-compact because affine morphisms are
quasi-compact, and the assertion is unchanged. So let $W,W'\subset S_j$ be
quasi-compact opens with $f_j^{-1}(W)=f_j^{-1}(W')$. It suffices to find
$i''\ge j$ with $f_{i''j}^{-1}(W)\subset f_{i''j}^{-1}(W')$: by symmetry the
reverse inclusion holds at some other index, and both inclusions persist
after pulling back to a common later index.

Write the quasi-compact $W$ as a finite union of affine opens
$A_1,\dots,A_m$. Fix one of them, $A=\operatorname{Spec}R_j$, and let
$R=\varinjlim_{l\ge j}R_l$ be the coordinate ring of the affine
$f_j^{-1}(A)$ as above. The open $W'\cap A$ of $A$ is a union of
principal opens $D(h)$, $h\in R_j$, and their preimages cover
$f_j^{-1}(A)\subset f_j^{-1}(W')$. As $f_j^{-1}(A)$ is affine, hence
quasi-compact, finitely many $h_1,\dots,h_n$ suffice, that is, their images
generate the unit ideal of $R$. A relation $\sum_ka_kh_k=1$ involves finitely
many elements of $R$, so it already holds in some $R_l$, $l\ge j$; then
$f_{lj}^{-1}(A)=\bigcup_kD(h_k)\subset f_{lj}^{-1}(W')$. Taking $i''$ at
least the indices obtained for $A_1,\dots,A_m$ gives
$f_{i''j}^{-1}(W)\subset f_{i''j}^{-1}(W')$, which proves (2).

*Clause (3).* Let $V_j\subset S_j$ be the preimage of $V_i$ for
$j\ge i$. These are quasi-compact opens of the $S_j$, the transition
morphisms $S_j\to S_i$ being affine and hence quasi-compact, and the
transition morphisms $V_{j'}\to V_j$ are the base changes of the affine
morphisms $S_{j'}\to S_j$, hence are affine. Moreover
$V=f_i^{-1}(V_i)=S\times_{S_i}V_i$ and
$V_j=S_j\times_{S_i}V_i$, the preimage of an open subscheme being its
fibre product. Let $T$ be a scheme with a compatible system of
morphisms $T\to V_j$ over the $S_j$. By the universal property of
the limit $S=\varprojlim_jS_j$ these induce a morphism $T\to S$,
whose composite with $f_i$ agrees with the given morphism to
$V_i\subset S_i$; hence $T\to S$ lands in $f_i^{-1}(V_i)=V$, and
the resulting morphism $T\to V$ is the unique one compatible with the
projections $V\to V_j$. Therefore $V$ represents the functor of the
system $\{V_j\}_{j\ge i}$, that is, $V=\varprojlim_{j\ge i}V_j$.
