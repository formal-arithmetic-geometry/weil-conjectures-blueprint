+++
kind = "proof"
of = "sk-thm-sf-pf-adic"
uses = ["sk-prop-open-coefficients", "sk-cor-geo-open-finiteness", "sk-prop-proper-base-change-unbounded", "sk-prop-int-compactness", "sk-lem-int-tensor", "sk-thm-sf-pf-field", "sk-thm-sfb-proper-base-change", "sk-lem-sf-determination", "sk-prop-integral-criterion", "sk-lem-pe-derived-nakayama"]
+++
Use [sk-prop-open-coefficients] and [sk-prop-proper-base-change-unbounded], and extend the
projection formula from $\Dbc$ ([sk-thm-sfb-proper-base-change]) by [sk-lem-sf-determination] in
each variable.

In detail, the first assertion is the integral case of [sk-prop-open-coefficients]: $Rj_*K$ is
derived complete, since $Rj_*$ commutes with $\operatorname{R\lim}$ (Stacks, Tag 099L) and with
cones, and

$$
(Rj_*K)\otimes^{\mathbf L}_{\mathcal O_{E,X}}\mathbf F_{E,X}
\simeq Rj_*(K\otimes^{\mathbf L}_{\mathcal O_{E,U}}\mathbf F_{E,U})
$$

in $D(X_{\mathrm{proét}},\mathcal O_E)$, where $\mathbf F_E=\mathcal O_E/\pi_E$ is the residue
field, because reduction is a cone. The right side is bounded constructible by
[sk-cor-geo-open-finiteness], which applies to $\mathbf F_E$ since it is a finite free extension of
$\mathbf F_\ell$, and the integral criterion [sk-prop-integral-criterion] gives
$Rj_*K\in\Dbc(X,\mathcal O_E)$ ([det-thm-sf-pf-adic-open]).

Proper base change on $\Loc(\Dctf(-,\mathcal O_E))$ is the integral case of
[sk-prop-proper-base-change-unbounded], using the estimates of [sk-prop-int-compactness]
([det-thm-sf-pf-adic-base-change]). For the projection formula, let $p$ be proper,
$K\in\Dbc(X,\mathcal O_E)$ and $L\in\Dbc(Y,\mathcal O_E)$. The map

$$
Rp_*K\otimes^{\mathbf L}L\longrightarrow Rp_*(K\otimes^{\mathbf L}p^*L)
\quad\text{in }D(Y_{\mathrm{proét}},\mathcal O_E)
$$

is an isomorphism by the integral case of [sk-thm-sfb-proper-base-change]: both sides are
derived complete, by [sk-lem-int-tensor] and proper finiteness, its reduction modulo $\pi_E$ is
the torsion projection formula map in $D(Y_{\mathrm{proét}},\mathbf F_E)$, an isomorphism by
Stacks, Tag 0F0G, and derived Nakayama ([sk-lem-pe-derived-nakayama]) concludes. The categories
$\Loc(\Dbc(-,\mathcal O_E))$ are closed under $\otimes^{\mathbf L}$ by [sk-lem-int-tensor] and the
two-variable localizing argument, and $Rp_*$ preserves direct sums there, so
[sk-lem-sf-determination], applied in each variable as in [sk-thm-sf-pf-field], extends the
projection formula to all of $\Loc(\Dbc(-,\mathcal O_E))$ ([det-thm-sf-pf-adic-projection]).
