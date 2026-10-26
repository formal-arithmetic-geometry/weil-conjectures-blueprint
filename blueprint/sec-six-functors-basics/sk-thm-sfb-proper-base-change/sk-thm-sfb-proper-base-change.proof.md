+++
kind  = "proof"
of    = "sk-thm-sfb-proper-base-change"
uses = ["sk-thm-properbasechange", "sk-cor-pbc-proet-finite", "det-pbc-complete-constructible", "sk-cor-pe-bounded-continuity", "sk-cor-coefficient-heart-ii", "sk-prop-sfb-cartesian-coefficients", "sk-prop-integral-criterion", "sk-lem-pe-derived-nakayama"]
+++
*Finite coefficients.* For finite $A$, proper constructible finiteness and a uniform
cohomological bound give bounded constructibility; the constant-module projection formula
gives a finite Tor bound. The details are in [sk-prop-ctf-finite-proper]. Proper base change is
[sk-thm-properbasechange] on the étale sites, transported to an isomorphism in
$D(Y'_{\mathrm{proét}},A)$ by its finite instance [sk-cor-pbc-proet-finite]; the projection
formula is the classical torsion formula (\stacks{0F0G}) in $D(Y_{\mathrm{ét}},A)$, transported
to $D(Y_{\mathrm{proét}},A)$ under the same comparison. Details:
[det-thm-sfb-proper-base-change-finite].

*Integral coefficients.* Let $K\in\Dbc(X,\cO_E)$. The complex $Rp_*K$ is derived complete.
Indeed, $K$ is derived complete if and only if
$\operatorname{R\lim}(\cdots\xrightarrow{\pi_E}K\xrightarrow{\pi_E}K)=0$, and $Rp_*$ commutes
with $\operatorname{R\lim}$ because it is a right adjoint. Moreover, reduction modulo $\pi_E$
commutes with $Rp_*$:
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
[sk-prop-integral-criterion], $Rp_*K\in\Dbc(Y,\cO_E)$.

Consider the projection formula map in $D(Y_{\mathrm{proét}},\cO_E)$ and the base change map in
$D(Y'_{\mathrm{proét}},\cO_E)$ for constructible integral complexes. By the preceding paragraph
and [sk-lem-integral-models] (3), the sources and targets of these maps are derived complete,
and their reductions modulo $\pi_E$ are the projection formula map and the proper base change
map with torsion coefficients. The first is an isomorphism by the projection formula for
torsion coefficients (\stacks{0F0G}). The second is an isomorphism by [sk-thm-properbasechange]
and [sk-cor-pbc-proet-finite], which apply because the finite reductions are bounded below
complexes pulled back from the étale site (see also [sk-prop-pbc-complete],
[det-pbc-complete-constructible] and \stacks{09C9}). Thus each integral map is a morphism
between derived complete complexes whose reduction modulo $\pi_E$ is an isomorphism, and by
derived Nakayama ([sk-lem-pe-derived-nakayama]) it is an isomorphism. Details:
[det-thm-sfb-proper-base-change-integral].

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
