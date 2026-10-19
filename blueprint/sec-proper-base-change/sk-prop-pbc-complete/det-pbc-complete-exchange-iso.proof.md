+++
kind = "proof"
of = "det-pbc-complete-exchange-iso"
+++
By [det-pbc-complete-exchange-map] (1), level $n$ of
$\operatorname{Ex}^{\operatorname{Tow}}_{\operatorname{red}(K)}$ is the exchange map
$\operatorname{Ex}_{K_n}\colon g^*Rp_*K_n\to Rp'_*g'^*K_n$ in
$D(Y'_{\mathrm{proét}},\mathcal O_E)$. It is the restriction of scalars along
$\mathcal O_{E,Y'}\to(\mathcal O_E/\pi_E^n)_{Y'}$ of the exchange map for $K_n$
as a complex of $(\mathcal O_E/\pi_E^n)$-modules: restriction of scalars is
exact, commutes with the module pullbacks (both rings are pulled back from the
point), and commutes with derived direct image. For the last point, let $J$ be
a K-injective complex of $(\mathcal O_E/\pi_E^n)_X$-modules and
$\rho\colon p_*J\to Rp_*J$ the canonical map in
$D(Y_{\mathrm{proét}},\mathcal O_E)$, with $J$ regarded as a complex of
$\mathcal O_{E,X}$-modules on the right. By
[Tag 0D6J](https://stacks.math.columbia.edu/tag/0D6J) (3), applied to the
ringed sites $(X_{\mathrm{proét}},(\mathcal O_E/\pi_E^n)_X)$ and
$(X_{\mathrm{proét}},\mathcal O_{E,X})$, both $p_*J$ and $Rp_*J$ map
isomorphically to the derived direct image of the underlying complex of abelian
sheaves, compatibly with $\rho$; so $\rho$ becomes an isomorphism in
$D(Y_{\mathrm{proét}},\mathbf Z)$, and it is an isomorphism because the forgetful
functor to abelian sheaves is exact and conservative. The same holds on $X'$
and $Y'$, and these identifications respect the units and counits defining
the exchange maps. The latter exchange map is an isomorphism by
[sk-cor-pbc-proet-finite] with $A=\mathcal O_E/\pi_E^n$, since $p$ is proper and
$K_n\in D^+_{\mathrm{class}}$. So every level of
$\operatorname{Ex}^{\operatorname{Tow}}_{\operatorname{red}(K)}$ is an isomorphism, and
$\operatorname{Ex}^{\operatorname{Tow}}_{\operatorname{red}(K)}$ is an isomorphism by
[det-pbc-complete-tower-calculus] (2): its cone has zero cohomology at every
level. Applying $R\varprojlim$, and composing with the two isomorphisms of
[det-pbc-complete-exchange-map] (2), shows that $\operatorname{Ex}^{\mathrm{comp}}_K$
is an isomorphism.
