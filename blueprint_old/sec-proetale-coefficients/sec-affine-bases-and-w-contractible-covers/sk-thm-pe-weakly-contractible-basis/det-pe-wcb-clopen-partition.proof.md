+++
kind = "proof"
of = "det-pe-wcb-clopen-partition"
+++
Apply the covering condition of [def-weil-pbc-proetale-covering] to the affine open
$W=U$: there are finitely many indices $i_1,\dots,i_m$ and affine opens $V_k\subset
U_{i_k}$ whose images cover $U$. Put $V=V_1\sqcup\dots\sqcup V_m$, an affine scheme. The
map $V\to U$ is weakly étale (each $U_{i_k}\to U$ is weakly étale by
[lem-trf-weakly-etale-between-objects], and open immersions are weakly étale by
[det-pe-morphisms-etale-comparison]) and surjective. So $V=\operatorname{Spec}E$ with
$D\to E$ faithfully flat (flat and surjective on spectra) and weakly étale.

By [det-pe-wcb-split-cover] there is a section $s\colon U\to V$ over $U$. The $V_k$ are
clopen in $V$, so $U'_k:=s^{-1}(V_k)$ are clopen in $U$ and partition it. Discarding empty
ones, $g_k\colon U'_k\xrightarrow{s}V_k\subset U_{i_k}$ is a $U$-morphism, since $s$ is a
section over $U$.
