+++
kind  = "proof"
of    = "sk-thm-sfb-proper-base-change"
uses = ["sk-thm-properbasechange", "sk-cor-pbc-proet-finite", "sk-cor-pe-bounded-continuity", "sk-cor-coefficient-heart-ii", "sk-prop-sfb-cartesian-coefficients"]
+++
*Finite coefficients.* For finite $A$, proper constructible finiteness and a uniform
cohomological bound give bounded constructibility; the constant-module projection formula
gives a finite Tor bound. The details are in [sk-prop-ctf-finite-proper]. Proper base change is
[sk-thm-properbasechange] on the étale sites, transported to an isomorphism in
$D(Y'_{\mathrm{proét}},A)$ by its finite instance [sk-cor-pbc-proet-finite]; the projection
formula is the classical torsion formula (\stacks{0F0G}) in $D(Y_{\mathrm{ét}},A)$, transported
to $D(Y_{\mathrm{proét}},A)$ under the same comparison. Details:
[det-thm-sfb-proper-base-change-finite].

*Integral coefficients.* Let $K\in\Dbc(X,\cO_E)$. The complex $Rp_*K$ is derived complete by
\stacks{099L}. Reduction modulo $\pi_E$ commutes with $Rp_*$:
$$
(Rp_*K)\otimes^{\mathbf L}\cO_{E,Y}/\pi_E\simeq Rp_*(K\otimes^{\mathbf L}\cO_{E,X}/\pi_E)
\quad\text{in }D(Y_{\mathrm{proét}},\cO_E).
$$
Indeed, $K\otimes^{\mathbf L}\cO_{E,X}/\pi_E$ is the cone of multiplication by $\pi_E$ on $K$, and
the exact functor $Rp_*$ commutes with this cone. The right side is the direct image of a
complex with torsion coefficients, which is pulled back from $X_{\mathrm{ét}}$ (\stacks{09B1});
its direct image in $D(Y_{\mathrm{proét}},\cO_E/\pi_E)$ is the pullback to $Y_{\mathrm{proét}}$ of
its direct image in $D(Y_{\mathrm{ét}},\cO_E/\pi_E)$ (\stacks{09A6}). The étale direct image is
constructible by the finiteness theorem for proper direct image with torsion coefficients
(\stacks{0GL0}), and bounded because $p$ has finite cohomological dimension (\stacks{0F10}). By
[sk-lem-integral-models] (2), $Rp_*K\in\Dbc(Y,\cO_E)$.

For constructible integral inputs, the canonical projection formula map in
$D(Y_{\mathrm{proét}},\cO_E)$ and the base change map in $D(Y'_{\mathrm{proét}},\cO_E)$, built from
the adjunctions and the usual maps between tensor products and inverse images, have derived
complete source and target, by the preceding paragraph and [sk-lem-integral-models] (3).
Their reductions modulo $\pi_E$ are the torsion projection formula and proper base change
maps. The first is an isomorphism by the projection formula for torsion coefficients
(\stacks{0F0G}). The second is an isomorphism by [sk-thm-properbasechange] and
[sk-cor-pbc-proet-finite]: the finite reductions are bounded below classical complexes, so
their canonical exchange maps are isomorphisms in $D(Y'_{\mathrm{proét}},\cO_E/\pi_E)$.
([sk-prop-pbc-complete] gives a completed integral version; here the inverse images of
constructible complexes are already complete.) Hence the cone of each integral map is derived
complete and has zero reduction modulo $\pi_E$. Such a complex is zero (derived Nakayama):
using the filtration of $\cO_E/\pi_E^n$ with subquotients $\cO_E/\pi_E$, its reductions modulo
every $\pi_E^n$ vanish, and a derived complete complex is the derived inverse limit of these
reductions. Hence the integral maps are isomorphisms. (Proper base change also follows
directly from \stacks{09C9}, since the inverse image of a constructible integral complex is
already derived complete.) Details: [det-thm-sfb-proper-base-change-integral].

*Rational coefficients.* For $K\in\Dbc(X,\cO_E)$, the complex $K[1/\ell]$ is the colimit of
$K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots$, a system with a common lower bound, so
[sk-cor-pe-bounded-continuity] gives
$$
Rp_*(K[1/\ell])\simeq(Rp_*K)[1/\ell]\quad\text{in }D(Y_{\mathrm{proét}},E).
$$
In the same way, $Rp_*$ commutes with extension of scalars to a finite $F/E$, as functors
$D(X_{\mathrm{proét}},E)\to D(Y_{\mathrm{proét}},F)$ (which is a finite direct sum, by
[sk-prop-sfb-cartesian-coefficients] (2)) and, by [sk-cor-pe-bounded-continuity] again, with the
filtered colimit $\QbarX\otimes_{E_X}-=\varinjlim_FF_X\otimes_{E_X}-$. Thus $Rp_*$ commutes with
inverting $\ell$ and with extension of scalars to $\Qlb$. By the integral case, $Rp_*$
therefore maps the generators of [sk-lem-integral-models] (4) into $\Dbc(Y,E)$ and
$\Dbc(Y,\Qlb)$, and since $\Dbc(Y,E)$ and $\Dbc(Y,\Qlb)$ are triangulated
([sk-cor-coefficient-heart-ii]), $Rp_*$ preserves $\Dbc(-,E)$ and $\Dbc(-,\Qlb)$. For the
projection formula and proper base change, rationalize the integral isomorphisms and extend
to all inputs by dévissage in each variable along the same generators. The maps involved are
the canonical ones, so the resulting isomorphisms satisfy the usual compatibilities with
composition. Details: [det-thm-sfb-proper-base-change-rational].

For the $\ell$-adic fields, an earlier version of this argument reduces proper base change on
$\Dbc(-,E)$ to bounded constructible integral complexes $K_0$ with $K=E\otimes K_0$
([sk-thm-sfb-rationalization-comparison]), writes $K_0=\operatorname{R\lim}_nK_0/\pi_E^n$ and
checks the exchange map on each torsion reduction, where it is the étale exchange morphism;
for $\Qlb$ one descends to a finite $E$ ([sk-thm-sfb-qlbar-two-colimit]).
