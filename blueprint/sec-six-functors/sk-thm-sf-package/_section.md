+++
id = "sk-thm-sf-package"
kind = "theorem"
title = "The six-operations package"
order = 2514
uses = ["sk-cor-sf-direct-image-ctf", "sk-def-sf-admissible", "sk-def-sf-operations", "sk-lem-sf-flat-model", "sk-lem-sf-mate", "sk-lem-sf-twist-interchange", "sk-prop-cohsm", "sk-prop-nagata-sketch-comp-category", "sk-prop-sf-cbc", "sk-prop-sf-comp-coherence", "sk-prop-sf-comp-proper", "sk-prop-sf-comparison", "sk-prop-sf-dualizable-biduality", "sk-prop-sf-finiteness", "sk-prop-sf-kunneth-ordinary", "sk-prop-sf-pf-reduction", "sk-prop-sf-rf-shriek-preservation", "sk-rem-sf-matrix", "sk-thm-nagata-compactification", "sk-thm-properbasechange", "sk-thm-purity-transport", "sk-thm-sf-direct-image-tor-amplitude", "sk-thm-sf-dual-perfect", "sk-thm-sf-global-duality", "sk-thm-sf-hom-ctf", "sk-thm-sf-identification", "sk-thm-sf-kunneth-relative", "sk-thm-sf-pf-adic", "sk-thm-sf-pf-field", "sk-thm-sf-pf-finite", "sk-thm-sf-pf-proetale", "sk-thm-sf-tensor-hom", "sk-thm-smooth-base-change", "sk-thm-smooth-purity"]
lean = ["AlgebraicGeometry.Etale.SixOperationsPackage", "AlgebraicGeometry.Etale.sixOperationsPackage"]
tags = ["sketch"]
+++
Fix the coefficient stages of [sk-def-sf-setting] and let $f:X\to Y$ be a
separated finite-type morphism of finite-type $k$-schemes. Then the six
operations of [sk-def-sf-operations] exist as functors of the ambient
categories, they descend to the small categories as in [sk-rem-sf-typing],
and they satisfy:

1. **(1)** *Adjunctions.* The functor $Lf^*$ is exact, hence preserves
bounded-below objects, and its restriction
$Lf^*:D^+(Y,\Lambda)\to D^+(X,\Lambda)$ is left adjoint to
$Rf_*:D^+(X,\Lambda)\to D^+(Y,\Lambda)$:
$\operatorname{Hom}_{D^+(X,\Lambda)}(Lf^*K,L)\cong \operatorname{Hom}_{D^+(Y,\Lambda)}(K,Rf_*L)$, naturally in
$K\in D^+(Y,\Lambda)$ and $L\in D^+(X,\Lambda)$ (both functors typed between
the same pair of categories); the constructible exceptional adjoint
$Rf^!:\Dctf(Y,\Lambda)\to\Dctf(X,\Lambda)$ of [sk-def-sf-operations] (vi) is
right adjoint to $Rf_!:\Dctf(X,\Lambda)\to\Dctf(Y,\Lambda)$,
unconditionally, with units and counits compatible with composition,
refinements and exchanges ([thm-sf-ambient-adjoint-class],
[sk-prop-sf-rf-shriek-preservation], [sk-lem-sf-mate] (1)); and, whenever $f$ carries the ambient datum of
[sk-def-sf-admissible] (1), the ambient functor
$Rf_!:D(X,\Lambda)\to D(Y,\Lambda)$ is left adjoint to the ambient functor
$Rf^{\times}:D(Y,\Lambda)\to D(X,\Lambda)$ of [sk-def-sf-operations] (v),
whose restriction to $\Dctf$ then agrees with $Rf^!$ (that datum fails in
general, [sk-rem-sf-fullcd-scope]).
1. **(2)** *Base change.* For every Cartesian square the exchange
transformation $\operatorname{Ex}_!:Lg^*Rf_!\to Rf'_!Lg'^*$ of
[sk-def-sf-exchanges] is a natural isomorphism with exactly the typing of
[sk-prop-sf-cbc] — at $\Lambda=A_{E,n}$ on $D^+$ of the small étale site
and on the étale-origin complexes of the pro-étale site; at
$\mathcal O_E,E,\Qlb$ only on $\Dbc$ of the adic pro-étale categories, as
the completed exchange, and never on the discrete non-torsion coefficients of
the small étale site, exactly as for $\operatorname{Ex}_*$ below; it is the
identity for the identity square,
compatible with pasting of squares, independent of the compactification
(compatible with the refinement comparisons of [sk-prop-sf-comp-coherence])
and compatible with the composition law of [sk-thm-sf-comp-composition],
the last two on the étale-origin complexes of [sk-def-sf-operations] (iv)
([sk-prop-sf-cbc]).
The exchange transformation $\operatorname{Ex}_*:Lg^*Rf_*\to Rf'_*Lg'^*$ is a
natural isomorphism for proper $f$ ([sk-thm-properbasechange]) and for
smooth $g$ ([sk-thm-smooth-base-change]), *with the following typing
only*: (a) at a finite stage $\Lambda=A_{E,n}$, as functors
$D^+(X,\Lambda)\to D^+(Y',\Lambda)$ on the small étale site and on the
étale-origin complexes of the pro-étale site (for smooth $g$ on the bounded
constructible ones); (b) at the stages
$\mathcal O_E$, $E$, $\Qlb$, only on $\Dbc$ of the pro-étale (adic)
categories — derived-complete $\mathcal O_E$-complexes whose reductions are
of étale origin, their rationalizations and the $\Qlb$-colimit, with
$\operatorname{Ex}_*$ the completed exchange — where it is deduced from (a)
by derived limits over the finite reductions and then transported by
rationalization and scalar extension, exactly as the projection formula is in
[sk-thm-sf-pf-adic] and [sk-thm-sf-pf-field]. No
assertion is made for the discrete non-torsion coefficients $\mathcal O_E,E,\Qlb$
on the small étale site, where $\operatorname{Ex}_*$ is not an isomorphism in
general.
1. **(3)** *Projection formula.* $\operatorname{PF}_{f,K,L}$ is an
isomorphism in $D^+(Y,\Lambda)$ at every coefficient stage, natural and
coherent, including compatible with base change through the
$\operatorname{Ex}_!$ of clause (2) (the base-change clause of
[sk-prop-sf-pf-coherence])
([sk-thm-sf-pf-finite], [sk-prop-sf-pf-reduction],
[sk-thm-sf-pf-adic], [sk-thm-sf-pf-field], [sk-thm-sf-pf-proetale],
[sk-prop-sf-pf-coherence]).
1. **(4)** *Compactifications and proper coincidence.*
$Rf_!=R\bar f_*j_!$ is independent of the compactification with the composition
law $R(gf)_!\cong Rg_!Rf_!$, and $Rf_!\cong Rf_*$ for proper $f$
([sk-prop-sf-comp-coherence], [sk-thm-sf-comp-composition],
[sk-prop-sf-comp-proper]).
1. **(5)** *Orientation.* For smooth $f$ of pure relative dimension $d$
the purity map $\gamma_{f,K}:Lf^*K(d)[2d]\to Rf^!K$ (the orientation of
[sk-def-sf-orientation]) is a natural isomorphism of functors
$\Dctf(Y,\Lambda)\to\Dctf(X,\Lambda)$; in particular
$\omega_f\cong\Lambda_X(d)[2d]$ ([sk-thm-smooth-purity], with
[sk-thm-purity-transport] for the remaining coefficient stages). It is
compatible with composition of smooth morphisms (twist additivity, through
the mate isomorphism $R(gf)^!\cong Rf^!Rg^!$ of [sk-lem-sf-mate]) and with
base change — along arbitrary $g$ at $\Lambda=A_{E,n}$, along étale $g$ at
the other stages — where the base-change isomorphism
$Lg'^*Rf^!\to Rf'^!Lg^*$ of [sk-prop-cohsm] (G12) is the mate of
$\operatorname{Ex}_!$ under $Rf_!\dashv Rf^!$ and $Rf'_!\dashv Rf'^!$; under
$\gamma_f,\gamma_{f'}$ it becomes the canonical isomorphism
$Lg'^*Lf^*\cong Lf'^*Lg^*$, i.e. the trace (the exceptional counit read
through $\gamma$) is compatible with $\operatorname{Ex}_!$. At
$\Lambda=A_{E,n}$ it is compatible with the exceptional Künneth map: for
smooth $f_i:X_i\to Y_i$ of pure relative dimensions $d_i$ and
$L_i\in\Dctf(Y_i,\Lambda)$, the map $\alpha$ of [sk-def-sf-kv-maps] (ii)
corresponds under $\gamma_{f_1}\boxtimes\gamma_{f_2}$ and
$\gamma_{f_1\times f_2}$ to the canonical pullback–tensor isomorphism
$Lf_1^*L_1(d_1)[2d_1]\boxtimes Lf_2^*L_2(d_2)[2d_2]\cong
L(f_1\times f_2)^*(L_1\boxtimes L_2)(d_1+d_2)[2d_1+2d_2]$ (the smooth step of
the proof of [sk-thm-sf-kunneth-verdier]; the Künneth–Verdier
isomorphism itself stays outside the package).
1. **(6)** *Duality.* With $\omega_X=Ra_X^!\Lambda$ formed from the
constructible exceptional adjoint of [sk-def-sf-operations](vi) (no
admissibility datum is assumed; [sk-prop-sf-biduality-general] is
unconditional),
$\mathbb D_X:\Dctf(X,\Lambda)\to\Dctf(X,\Lambda)$,
$\mathbb D_X=\RHom_X(-,\omega_X)$ with $\omega_X=Ra_X^!\Lambda$, is a
contravariant exact anti-equivalence,
and the biduality morphism $\delta_K:K\to\mathbb D_X\mathbb D_XK$ (the
tensor–Hom transpose of the evaluation
$K\otimes^L_\Lambda\mathbb D_XK\to\omega_X$) is a natural isomorphism
$\delta:\mathrm{id}\xrightarrow{\sim}\mathbb D_X\mathbb D_X$
([sk-prop-sf-biduality-general]). For every separated finite-type $f$,
the Verdier exchange map
$\varepsilon_{f,M}:\mathbb D_Y(Rf_!M)\to Rf_*\mathbb D_X(M)$ of
[sk-thm-sf-verdier-exchange] — the tensor–Hom isomorphism of
[sk-thm-sf-tensor-hom] at $N=\omega_Y$ followed by
$Rf_*\RHom_X(M,-)$ of the mate isomorphism $Rf^!\omega_Y\cong\omega_X$ —
is a natural isomorphism in $D^+(Y,\Lambda)$ for $M\in\Dctf(X,\Lambda)$; it
is compatible with composition: for $X\xrightarrow{f}Y\xrightarrow{g}Z$,
$\varepsilon_{gf,M}$ agrees, through $\mathbb D_Z(\alpha_{g,f})$ and
$R(gf)_*\cong Rg_*Rf_*$, with
$Rg_*(\varepsilon_{f,M})\circ\varepsilon_{g,Rf_!M}$ (associativity of
$\operatorname{PF}$, [sk-prop-sf-pf-coherence], and the mate calculus
[sk-lem-sf-mate]). No compatibility of
$\varepsilon$ with base change along an arbitrary $g$ is asserted
($\mathbb D$ does not commute with $Lg^*$ in general).
Unconditionally, for $X$ smooth of pure dimension $d$ and perfect $K$, the
orientation-induced
isomorphism $\theta_K:\mathbb D_XK\xrightarrow{\sim}K^\vee(d)[2d]$ of
[sk-thm-sf-dual-perfect] is natural in $K$
([sk-thm-sf-dual-perfect], [sk-prop-sf-dualizable-biduality]); the
global duality map $\RG_c(X,K)^\vee\to\RG(X,\mathbb D_XK)$ of
[sk-thm-sf-global-duality] is an isomorphism in the point category; and the
derived Poincaré pairing is perfect and is the duality isomorphism
([sk-thm-sf-identification]).
1. **(7)** *Relative product.*
The relative Künneth map
$\kappa^{\mathrm{rel}}_{K,L}:R(f\times_Bg)_!(K\boxtimes L)\to
Rf_!K\otimes^LRg_!L$ of [sk-thm-sf-kunneth-relative] (the composite of the
composition law, the inverse projection transformations for $q$ and $g$ and
the inverse of $\operatorname{Ex}_!$) is a natural isomorphism in
$D^+(B,\Lambda)$, compatible with symmetry, triple products, base change
$B'\to B$ and the projection formula as stated there (the symmetry and
base-change compatibilities rest on the base-change clause of
[sk-prop-sf-pf-coherence], i.e. on clause (3)), with its
compact-support form on closed subschemes ([sk-thm-sf-kunneth-relative]).
1. **(8)** *Stability.* The operations descend to the constructible and
finite-Tor subcategories exactly as typed in [sk-thm-sf-ctf-stability] and
[sk-rem-sf-matrix], with the explicit amplitude shifts
$[a,b+2d]$ for $Rf_*$, $[a+c,b+d]$ for $\otimes^L$, $[c-b-2d,d'-a+2d]$
for $\RHom$ of objects with amplitudes $[a,b],[c,d']$ on a scheme of
dimension $\le d$ ($[c-b,d'-a]$ for a site-perfect first argument), and
for $Rf^!$ the shifts of [sk-prop-sf-rf-shriek-preservation]: $-2d$ for
$f$ smooth of pure relative dimension $d$, $[a,b]\mapsto[a,b+2d+1]$ for a
closed immersion into a target of dimension $\le d$ (a target-dimension
bound; no codimension-only bound is asserted for arbitrary closed
immersions), and $[a,b]\mapsto[a-2D,b+2\dim Y+1]$ in the general case, $D$
the maximal embedding dimension of the affine charts.
