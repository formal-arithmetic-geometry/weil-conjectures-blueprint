+++
kind = "proof"
of = "proposition-direct-image-along-open-immersion"
order = 591
uses = ["corollary-continuity-cohomology", "proposition-integral-constructibility-criterion", "lemma-integral-models", "corollary-open-direct-image-over-field"]
+++
For $\mathcal O_E$ we use the criterion of
Proposition [proposition-integral-constructibility-criterion], which
asks for derived completeness and constructible reduction. Let
$K\in\Dbc(U,\mathcal O_E)$. Since $Rj_*$ commutes with $R\varprojlim$
[Stacks, [099L](https://stacks.math.columbia.edu/tag/099L)], $Rj_*K$ is derived complete. Since $Rj_*$ also commutes with
cones, the reduction of $Rj_*K$ modulo $\pi_E$ is $Rj_*$ of the reduction
of $K$. That reduction comes from $U_{\acute{e}t}$. Its direct image is
therefore the pullback of the étale one [Stacks, [09A6](https://stacks.math.columbia.edu/tag/09A6)], which is bounded
constructible by Corollary [corollary-open-direct-image-over-field]. Both
conditions of the criterion hold, and so $Rj_*K\in\Dbc(X,\mathcal O_E)$.

For $E$ and $\overline{\mathbf Q}_\ell$ we reduce to the integral case. Since $Rj_*$ is
exact, the objects $K$ with $Rj_*K\in\Dbc$ form a triangulated
subcategory. It therefore suffices to treat the generators of
Lemma [lemma-integral-models](4). These come from integral objects by
inverting $\ell$ and by a colimit over finite extensions of $E$. Both
operations are filtered colimits of systems with a common lower bound,
and $Rj_*$ commutes with such colimits
(Corollary [corollary-continuity-cohomology]). Hence $Rj_*$ of a generator
is obtained from $Rj_*$ of an integral object by the same operations, and
it lies in $\Dbc$.
