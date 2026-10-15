+++
kind = "proof"
of = "det-sfb-dc-restricted-functors-closed-image"
+++
Recall that $K\in\D(X_{\mathrm{proét}},\mathcal O_E)$ lies in $\Dbc(X,\mathcal O_E)$ iff it is derived $\pi_E$-complete and
$K\otimes^{\mathbf L}\mathcal O_E/\pi_E$ is bounded with constructible cohomology (the integral constructibility
criterion; boundedness of $K$ follows by derived Nakayama).

*Exactness and limits.* $j_!$ is exact on sheaves and preserves all limits (Stacks, Tag 09BP; this uses that
$j$ is quasi-compact). $i_*$ is exact (Stacks, Tag 09BM) and preserves limits (Stacks, Tag 09AA, and it is a
right adjoint). So both are computed termwise, preserve products of complexes and cones, hence derived
limits of sequences.

*Completeness.* $K$ is derived complete iff $K\to R\varprojlim_nK\otimes^{\mathbf L}\mathcal O_E/\pi_E^n$ is an
isomorphism. An exact $\mathcal O_E$-linear functor commutes with $-\otimes^{\mathbf L}\mathcal O_E/\pi_E^n$ (the cone of
$\pi_E^n$), and, preserving derived limits of sequences, preserves this isomorphism. Hence $j_!K$, $i_*K$ are
derived complete.

*Reductions.* $(j_!K)\otimes^{\mathbf L}\mathcal O_E/\pi_E=j_!(K\otimes^{\mathbf L}\mathcal O_E/\pi_E)$, and $j_!$ preserves
bounded constructible torsion complexes (add the closed complement as a zero stratum); similarly
$i_*$ preserves them (strata of $Z$ are locally closed in $X$; add $X\setminus Z$ as a zero stratum). So the
reductions are bounded constructible.

*Dévissage.* Given $K\in\Dbc(X,\mathcal O_E)$, choose by [sk-lem-int-integral-heart] a finite stratification on
whose strata $K$ is locally the completion of a bounded complex of finite free modules. Inducting on the
number of strata, take an open stratum $j\colon U\hookrightarrow X$ with closed complement $i$; the triangle
$j_!j^*K\to K\to i_*i^*K\to$ (open–closed localization) has outer terms of the required form, by the
preceding paragraphs and induction applied to $i^*K$ on $X\setminus U$.
