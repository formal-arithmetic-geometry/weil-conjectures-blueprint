+++
id = "sk-thm-sf-compatibility"
kind = "theorem"
title = "Compatibility of the six operations"
order = 3565
uses = ["sec-proetale-coefficients", "sec-proper-base-change", "sec-six-functors-basics", "sec-smooth-base-change", "sec-smooth-purity", "sk-prop-cohsm", "sk-prop-sf-open-closed-triangle", "sk-def-sf-categories", "sk-prop-scalar-six", "sk-def-sf-orientation", "sk-lem-sf-mate", "sk-thm-sf-ctf-stability", "sk-prop-sf-comp-coherence", "sk-prop-sf-comp-proper", "sk-prop-sf-pf-coherence", "sk-thm-sfb-qlbar-two-colimit", "sk-rem-sf-pf-done", "sk-thm-sf-comp-composition", "sk-thm-sf-kunneth-relative", "sk-thm-sf-package", "sk-thm-sf-tensor-hom", "sk-thm-sf-verdier-exchange"]
tags = ["sketch"]
+++
Fix an admissible coefficient ring $\Lambda$ of [def-sf-setting],
regarded as a condensed ring, so that the categories are the full
subcategories $\Dctf(X,\Lambda)\subseteq D(X_{\mathrm{pro\acute et}},\Lambda)$ of
[sk-def-sf-categories], and the six operations
$Lf^*,Rf_*,Rf_!,Rf^!,\otimes^L,\RHom$ of [sk-thm-sf-package], each typed
as there ([sk-rem-sf-typing]). The structure isomorphisms that relate them
— the composition isomorphisms, the units and counits of the two
adjunctions, the exchange transformations, the projection transformation,
the proper identification $Rf_!\cong Rf_*$, the tensor–Hom and Verdier
exchanges and the orientation — are compatible with each other, on the
categories on which [sk-thm-sf-package] types each of them:

1. **(1)** *Composition.* The composition isomorphisms
$L(gf)^*\cong Lf^*Lg^*$ ([det-prop-sfb-module-derived-factorization]),
$R(gf)_*\cong Rg_*Rf_*$ (its mate under $Lf^*\dashv Rf_*$),
$R(gf)_!\cong Rg_!Rf_!$ ([sk-thm-sf-comp-composition]) and
$R(gf)^!\cong Rf^!Rg^!$ ([sk-lem-sf-mate] (1)) are associative and
unital, and each isomorphism for a right adjoint is the mate of the one for
its left adjoint, so that the units and counits of $Lf^*\dashv Rf_*$ and
$Rf_!\dashv Rf^!$ are compatible with composition. The functor $Rf_!$ is
independent of the compactification, with comparison isomorphisms satisfying
the cocycle condition and compatible with the composition law
([sk-prop-sf-comp-coherence]).
1. **(2)** *Base change.* The exchange transformations
$\operatorname{Ex}_*$ and $\operatorname{Ex}_!$ of [det-def-sf-exchanges]
are natural in the square, the identity for the identity square and
compatible with horizontal and vertical pasting; $\operatorname{Ex}_!$ is
compatible with the refinement comparisons and the composition law of (1)
([det-prop-sf-cbc]), and for proper $f$ it is $\operatorname{Ex}_*$ under
$Rf_!\cong Rf_*$ ([sk-prop-sf-comp-proper]). Its mate is the dual base
change isomorphism $Rf^!Rg_*\cong Rg'_*Rf'^!$, natural in the square and
compatible with pasting ([thm-sf-dual-base-change]), and for smooth $f$ the
exceptional base change $Lg'^*Rf^!\cong Rf'^!Lg^*$ of [sk-prop-cohsm]
(G12) is the mate of $\operatorname{Ex}_!$.
1. **(3)** *Tensor product.* The projection transformation
$\operatorname{PF}$ is natural, the identity for $f=\mathrm{id}$,
associative for composable $f,g$ with respect to the composition law of
(1), independent of the compactification, equal for proper $f$ to the
direct-image projection formula through $Rf_!\cong Rf_*$, and compatible
with base change through $\operatorname{Ex}_!$ and the monoidality of
$Lg^*$ ([sk-prop-sf-pf-coherence]).
1. **(4)** *Internal Hom and duality.* The tensor–Hom exchange
$Rf_*\RHom_X(M,Rf^!N)\cong\RHom_Y(Rf_!M,N)$ of
[sk-thm-sf-tensor-hom] is built from the adjunctions and the inverse of
$\operatorname{PF}$, and is natural in $M$ and $N$. With
$\mathbb D=\RHom(-,\omega)$ and biduality
([det-prop-sf-biduality-general]), the Verdier exchange
$\mathbb D_YRf_!\cong Rf_*\mathbb D_X$ ([sk-thm-sf-verdier-exchange])
is compatible with composition ([sk-thm-sf-package] (6)), and its mate is
the isomorphism $\mathbb D_XLf^*\cong Rf^!\mathbb D_Y$, natural in $f$
([cor-sf-duality-pullback]).
1. **(5)** *Orientation.* For smooth $f$ the purity isomorphism
$\gamma_f:Lf^*(-)(d)[2d]\cong Rf^!$ of [sk-def-sf-orientation] is
compatible with composition through the isomorphism
$R(gf)^!\cong Rf^!Rg^!$ of (1), and with base change through the
exceptional base change of (2) — along arbitrary $g$ at $\Lambda=A_{E,n}$,
along étale $g$ at the other stages ([sk-thm-sf-package] (5)).
1. **(6)** *Products.* The relative Künneth isomorphism of
[sk-thm-sf-kunneth-relative] is compatible with symmetry, triple products,
base change and the projection formula.
1. **(7)** *Coefficients.* All of the maps above commute with the
coefficient comparisons of [sk-prop-scalar-six] (reduction modulo
$\pi_E^n$ and extension of scalars along maps of condensed rings), and at
field coefficients they are Weil-equivariant ([fix-prop-coherence]).

No compatibility of the Verdier exchange with base change along an arbitrary
$g$ is asserted, since $\mathbb D$ does not commute with $Lg^*$ in general.
