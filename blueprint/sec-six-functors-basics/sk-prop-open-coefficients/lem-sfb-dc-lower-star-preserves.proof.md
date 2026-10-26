+++
kind  = "proof"
of    = "lem-sfb-dc-lower-star-preserves"
uses = ["sk-prop-integral-criterion", "sk-lem-integral-models", "sk-cor-pe-bounded-continuity", "sk-cor-coefficient-heart-ii"]
+++
This is Deligne's finiteness theorem for $Rf_*$ (SGA 4½, *Th. finitude*, 1.1), extended to
$\ell$-adic coefficients through the integral route. Let first $\Lambda=\underline{\cO}_E$ with
uniformizer $\pi_E$. By [sk-prop-integral-criterion], a complex $K$ is bounded constructible if
and only if it is derived complete and its reduction
$K_1=K\otimes^{\mathbf L}_{\cO_{E,X}}\cO_{E,X}/\pi_E$ is a bounded constructible complex pulled
back from the étale site. Now $Rf_*$ commutes with $\operatorname{R\lim}$, being a right adjoint,
and with cones, so it preserves derived completeness. It commutes with reduction modulo $\pi_E$,
because $K_1$ is the cone of multiplication by $\pi_E$ on $K$ and $Rf_*$ is exact. Since $K_1$
comes from the étale site, its pro-étale direct image is the pullback of its étale direct image
(\stacks{09A6}). Since $\ell$ is invertible on the finite type $k$-schemes $X$ and $Y$,
Deligne's theorem shows that this étale direct image is bounded with constructible cohomology.
Hence $Rf_*K$ is bounded constructible, by [sk-prop-integral-criterion] again.

For $\Lambda=\underline E$ and $\Lambda=\underline{\Qlb}$ it suffices to treat the generators of
[sk-lem-integral-models] (4): $Rf_*$ is exact and $\Dbc(Y,\Lambda)$ is triangulated
([sk-cor-coefficient-heart-ii]). These generators come from objects $a_!L_0$ of
$\Dbc(X,\cO_E)$ by inverting $\ell$ and, for $\Qlb$, by the filtered colimit over finite
extensions of $E$. Both are colimits of systems with a common lower bound, so $Rf_*$ commutes
with them by [sk-cor-pe-bounded-continuity] ($X$ is quasi-compact and quasi-separated). By the
integral case, $Rf_*$ maps the generators into $\Dbc(Y,E)$, respectively $\Dbc(Y,\Qlb)$.
