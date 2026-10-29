+++
kind = "proof"
of = "sk-prop-open-coefficients"
uses = ["sk-prop-integral-criterion", "sk-cor-geo-open-finiteness", "sk-lem-integral-models", "sk-cor-pe-bounded-continuity"]
+++
Recall that an integral complex lies in $\Dbc$ if it is derived complete with
constructible reduction modulo $\pi_E$ ([sk-prop-integral-criterion]). Let
$K\in\Dbc(U,\mathcal O_E)$. Since $Rj_*$ commutes with $R\varprojlim$
([Stacks, Tag 099L](https://stacks.math.columbia.edu/tag/099L)) and with cones, $Rj_*K$ is
derived complete and its reduction is $Rj_*$ of the reduction of $K$. That reduction comes
from $U_{\mathrm{ét}}$, so its direct image is the pullback of the étale one
([Stacks, Tag 09A6](https://stacks.math.columbia.edu/tag/09A6)), which is bounded
constructible by [sk-cor-geo-open-finiteness]. For $E$ and $\Qlb$ it suffices to treat the
generators of [sk-lem-integral-models] (4), which come from integral objects by inverting
$\ell$ and by a colimit over finite extensions of $E$; $Rj_*$ commutes with both, as they
are colimits of systems with a common lower bound ([sk-cor-pe-bounded-continuity]).
