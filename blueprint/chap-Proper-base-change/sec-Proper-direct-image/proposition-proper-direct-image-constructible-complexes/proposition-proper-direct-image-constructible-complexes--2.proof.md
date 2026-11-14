+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--2"
order = 425005
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-exact-products--2", "proposition-milnor-sequence--2", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "proposition-proper-direct-image-constructible-complexes--1", "proposition-comparison-etale-derived-category--5", "definition-compactification-refinement--1"]
+++
*Integral coefficients.* Let $K\in\Dbc(X,\mathcal O_E)$. We first show that $Rp_*K\in\Dbc(Y,\mathcal O_E)$, by computing its reduction as in (4.15) below. By
Proposition [proposition-integral-constructibility-criterion] and
Lemma [lemma-bounds-finite-reductions], $K$ is derived complete with
bounded classical finite reductions. Hence
Proposition [proposition-proper-base-change-complete-integral] applies.
It shows that $Rp_*K$ is derived complete, and it gives a canonical comparison
of reductions

$$
(Rp_*K)\otimes^{\mathbf L}\mathcal O_{E,Y}/\pi_E
\simeq Rp_*(K\otimes^{\mathbf L}\mathcal O_{E,X}/\pi_E).
$$

The right side of (4.15) is constructible and
bounded. Indeed, it is the direct image of a torsion complex pulled back
from $X_{\acute{e}t}$ [Stacks, [09B1](https://stacks.math.columbia.edu/tag/09B1)]. So it is the pullback to $Y_{\mathrm{pro}\acute{e}t}$ of the
direct image in $D(Y_{\acute{e}t},\mathbf F_E)$ [Stacks, [09A6](https://stacks.math.columbia.edu/tag/09A6)]. The latter is
constructible by the finiteness theorem for proper direct image
with torsion coefficients [Stacks, [0GL0](https://stacks.math.columbia.edu/tag/0GL0)]. It is bounded because $p$ has
finite cohomological dimension [Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)]. Now
Proposition [proposition-integral-constructibility-criterion] gives
$Rp_*K\in\Dbc(Y,\mathcal O_E)$.

*Source:* the proof of Proposition [proposition-proper-direct-image-constructible-complexes].
