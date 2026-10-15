+++
kind = "proof"
of = "det-thm-sf-pf-adic-open"
+++
*Completeness.* $K=R\varprojlim_n K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n$ and
$Rj_*$ commutes with $R\varprojlim$ (both are right adjoints of exact functors,
Stacks, Tag 099L), so $Rj_*K$ is the derived limit of the
$Rj_*(K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n)$, and it is derived complete.

*Reduction.* $K\otimes^{\mathbf L}\mathbf F_{E,U}$ is the cone of
multiplication by $\pi_E$ on $K$. $Rj_*$ is exact and $\mathcal O_E$-linear, so
it carries this cone to the cone of $\pi_E$ on $Rj_*K$, which is
$(Rj_*K)\otimes^{\mathbf L}\mathbf F_{E,X}$.

*Constructibility of the reduction.* $K\otimes^{\mathbf L}\mathbf F_{E,U}$ is
a bounded constructible complex of $\mathbf F_E$-modules pulled back from the
étale site, and its pro-étale direct image is the pullback of the étale direct
image (Stacks, Tag 09A6). The latter is bounded constructible by
[sk-cor-geo-open-finiteness], applicable because $\mathbf F_E$ is a finite
field of characteristic $\ell$ (a finite free extension of $\mathbf F_\ell$).

*Conclusion.* $Rj_*K$ is derived complete with bounded constructible reduction
modulo $\pi_E$, so the residue criterion (Stacks, Tag 09C1; compare
[sk-prop-integral-criterion]) gives $Rj_*K\in\Dbc(X,\mathcal O_E)$.
