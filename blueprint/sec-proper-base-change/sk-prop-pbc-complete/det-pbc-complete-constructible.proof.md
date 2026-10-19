+++
kind = "proof"
of = "det-pbc-complete-constructible"
+++
(1) By [sk-prop-integral-criterion] and [det-prop-integral-criterion-reductions],
$K$ is derived complete and every $K_n$ lies in $\Dbc(X,\mathcal O_E/\pi_E^n)$;
bounded constructible complexes with finite coefficients are classical by
[sk-thm-pe-constructible-comparison].

(2) By [det-thm-sfb-proper-base-change-integral] (1), $Rp_*K\in\Dbc(Y,\mathcal O_E)$.
Inverse image preserves $\Dbc(-,\mathcal O_E)$ ([sk-lem-integral-models] (3)), so
$g^*Rp_*K\in\Dbc(Y',\mathcal O_E)$ and $g'^*K\in\Dbc(X',\mathcal O_E)$, and both
are derived complete by [sk-prop-integral-criterion]. The completion maps are
then isomorphisms by [lemma-weil-pbc-completed-pullback-reduction] (3).

(3) The completion map is natural, so applied to $\operatorname{Ex}_K$ it gives
$\kappa_{Rp'_*g'^*K}\circ\operatorname{Ex}_K=R\varprojlim\operatorname{red}(\operatorname{Ex}_K)
\circ\kappa_{g^*Rp_*K}$. Under the identifications
$\operatorname{red}(g^*Rp_*K)\simeq g^*_{\operatorname{Tow}}Rp^{\operatorname{Tow}}_*\operatorname{red}(K)$
and $\operatorname{red}(Rp'_*g'^*K)\simeq Rp'^{\operatorname{Tow}}_*g'^*_{\operatorname{Tow}}\operatorname{red}(K)$
([lemma-weil-pbc-completed-pullback-reduction] (1),
[prop-weil-pbc-direct-image-limits] (2)), which are induced by the termwise
cone construction and therefore commute with units, counits and pullback
comparisons, $\operatorname{red}(\operatorname{Ex}_K)$ is
$\operatorname{Ex}^{\operatorname{Tow}}_{\operatorname{red}(K)}$. Moreover
$R\varprojlim\operatorname{red}(Rp'_*g'^*K)\simeq Rp'_*R\varprojlim\operatorname{red}(g'^*K)$
by [prop-weil-pbc-direct-image-limits] (1), (2), and $\kappa_{Rp'_*g'^*K}$
corresponds to $Rp'_*\kappa_{g'^*K}$ by [prop-weil-pbc-direct-image-limits] (3).
So the displayed equation says that $\operatorname{Ex}^{\mathrm{comp}}_K$,
precomposed with $\kappa_{g^*Rp_*K}$, equals $Rp'_*\kappa_{g'^*K}\circ
\operatorname{Ex}_K$. Since $\operatorname{Ex}^{\mathrm{comp}}_K$ is an isomorphism by
(1) and both completion maps are isomorphisms by (2), $\operatorname{Ex}_K$ is an
isomorphism. Its source is in $\Dbc(Y',\mathcal O_E)$ by (2), and so is its
target, by [det-thm-sfb-proper-base-change-integral] (1) for the proper
morphism $p'$.
