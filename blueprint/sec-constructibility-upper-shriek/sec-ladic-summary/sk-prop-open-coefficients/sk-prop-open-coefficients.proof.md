+++
kind = "proof"
of = "sk-prop-open-coefficients"
uses = ["sk-prop-integral-criterion", "sk-cor-geo-open-finiteness", "sk-lem-integral-models", "sk-cor-pe-bounded-continuity"]
+++
Let $K\in\Dbc(U,\mathcal O_E)$. Since $Rj_*$ commutes with $R\varprojlim$
[Stacks, Tag 099L](https://stacks.math.columbia.edu/tag/099L) and with cones, $Rj_*K$ is derived complete and its reduction
is $Rj_*$ of the reduction of $K$. That reduction comes from $U_{\acute{e}t}$, so
its direct image is the pullback of the étale one [Stacks, Tag 09A6](https://stacks.math.columbia.edu/tag/09A6), which is
bounded constructible by Corollary [sk-cor-geo-open-finiteness]. For $E$ and
$\overline{\mathbf Q}_\ell$ it suffices to treat the generators of
Lemma [sk-lem-integral-models](4), which come from integral objects by
inverting $\ell$ and by a colimit over finite extensions of $E$; $Rj_*$
commutes with both, as they are colimits of systems with a common lower
bound (Corollary [sk-cor-pe-bounded-continuity]).
