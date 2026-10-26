+++
kind = "proof"
of = "sk-prop-open-coefficients"
uses = ["sk-thm-sfb-proper-base-change", "sk-cor-geo-open-finiteness", "sk-lem-integral-models", "sk-cor-pe-bounded-continuity", "sk-cor-coefficient-heart-ii", "sk-prop-integral-criterion"]
+++
We follow [sk-thm-sfb-proper-base-change], with the open finiteness theorem
[sk-cor-geo-open-finiteness] in place of proper finiteness.

*Integral coefficients.* Let $K\in\Dbc(U,\mathcal O_E)$. Since $Rj_*$
commutes with $\operatorname{R\lim}$ (Stacks, Tag 099L) and with cones, $Rj_*K$
is derived complete. Reduction modulo $\pi_E$ commutes with $Rj_*$, because $K\otimes^{\mathbf L}\mathcal O_{E,U}/\pi_E$ is the cone of
multiplication by $\pi_E$ on $K$ and $Rj_*$ is exact; this is the same
observation as for the reduction of proper direct image in
[sk-thm-sfb-proper-base-change]. The reduction of $K$ is pulled back from a
bounded constructible complex on $U_{\mathrm{ét}}$. By Stacks, Tag 09A6, its
pro-étale direct image in $D(X_{\mathrm{proét}},\mathcal O_E/\pi_E)$ is the
pullback of its étale direct image in $D(X_{\mathrm{ét}},\mathcal O_E/\pi_E)$,
which is bounded constructible by [sk-cor-geo-open-finiteness], since the
coefficient ring $\mathcal O_E/\pi_E$ is a finite field of characteristic
$\ell$. Thus $Rj_*K$ is derived complete with bounded constructible reduction,
and [sk-prop-integral-criterion] gives $Rj_*K\in\Dbc(X,\mathcal O_E)$.

*Rational coefficients.* Inverting $\ell$ is the colimit of
$K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots$, and extension of scalars to
$\Qlb$ is a filtered colimit over finite extensions of $E$. Both are colimits
of systems with a common lower bound, so [sk-cor-pe-bounded-continuity] shows
that $Rj_*$ commutes with them. By the integral case, $Rj_*$ therefore maps
the generators of [sk-lem-integral-models](4) into $\Dbc(X,E)$, respectively
$\Dbc(X,\Qlb)$. Since these categories are triangulated
([sk-cor-coefficient-heart-ii]), $Rj_*$ preserves $\Dbc(-,E)$ and
$\Dbc(-,\Qlb)$.
