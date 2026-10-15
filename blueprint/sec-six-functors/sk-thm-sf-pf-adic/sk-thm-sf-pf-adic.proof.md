+++
kind = "proof"
of = "sk-thm-sf-pf-adic"
uses = ["sk-prop-open-coefficients", "sk-cor-geo-open-finiteness", "sk-prop-proper-base-change-unbounded", "sk-prop-int-compactness", "sk-def-sfb-dc-restricted-functors", "sk-thm-sf-pf-field"]
+++
The first assertion is the integral case of [sk-prop-open-coefficients]. In
detail: $Rj_*K$ is derived complete by Stacks, Tag 099L, and

$$
(Rj_*K)\otimes^{\mathbf L}_{\mathcal O_{E,X}}\mathbf F_{E,X}
\simeq Rj_*(K\otimes^{\mathbf L}_{\mathcal O_{E,U}}\mathbf F_{E,U})
$$

in $D(X_{\mathrm{proét}},\mathcal O_E)$, where $\mathbf F_E=\mathcal O_E/\pi_E$
is the residue field, because reduction is a cone. The right side is bounded
constructible by [sk-cor-geo-open-finiteness], which applies to $\mathbf F_E$
since it is a finite free extension of $\mathbf F_\ell$, and the residue
criterion (Stacks, Tag 09C1) gives $Rj_*K\in\Dbc(X,\mathcal O_E)$.

Proper base change on $\Loc(\Dctf(-,\mathcal O_E))$ is the integral case of
[sk-prop-proper-base-change-unbounded], using the estimates of
[sk-prop-int-compactness]. For the projection formula, let $p$ be proper,
$K\in\Dbc(X,\mathcal O_E)$ and $L\in\Dbc(Y,\mathcal O_E)$. Both sides of

$$
Rp_*K\otimes^{\mathbf L}L\longrightarrow Rp_*(K\otimes^{\mathbf L}p^*L)
\quad\text{in }D(Y_{\mathrm{proét}},\mathcal O_E)
$$

are derived complete, by [sk-def-sfb-dc-restricted-functors] and proper
finiteness. Its reduction modulo $\pi_E$ is the torsion projection formula map
in $D(Y_{\mathrm{proét}},\mathbf F_E)$, an isomorphism by Stacks, Tag 0F0G. The
cone is derived complete with zero reduction modulo $\pi_E$, so it vanishes by
derived Nakayama (Stacks, Tag 099I). The categories $\Loc(\Dbc(-,\mathcal O_E))$
are closed under $\otimes^{\mathbf L}$ by [sk-def-sfb-dc-restricted-functors]
and the two-variable localizing argument, and $Rp_*$ preserves direct sums
there, so the localizing argument of [sk-thm-sf-pf-field] extends the
projection formula to all of $\Loc(\Dbc(-,\mathcal O_E))$.
