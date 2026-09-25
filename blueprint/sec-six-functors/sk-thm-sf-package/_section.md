+++
id = "sk-thm-sf-package"
kind = "section"
title = "The six-operations package"
order = 2376
uses = ["sk-cor-sf-direct-image-ctf", "sk-lem-sf-flat-model", "sk-lem-sf-twist-interchange", "sk-prop-cohsm", "sk-prop-nagata-sketch-comp-category", "sk-prop-sf-biduality-general", "sk-prop-sf-cbc", "sk-prop-sf-comp-coherence", "sk-prop-sf-comp-proper", "sk-prop-sf-comparison", "sk-prop-sf-dualizable-biduality", "sk-prop-sf-existence", "sk-prop-sf-finiteness", "sk-prop-sf-kunneth-ordinary", "sk-prop-sf-pf-coherence", "sk-prop-sf-pf-reduction", "sk-prop-sf-rf-shriek-preservation", "sk-rem-sf-matrix", "sk-thm-nagata-compactification", "sk-thm-properbasechange", "sk-thm-purity-transport", "sk-thm-sf-comp-composition", "sk-thm-sf-ctf-stability", "sk-thm-sf-direct-image-tor-amplitude", "sk-thm-sf-dual-perfect", "sk-thm-sf-global-duality", "sk-thm-sf-hom-ctf", "sk-thm-sf-identification", "sk-thm-sf-kunneth-relative", "sk-thm-sf-pf-adic", "sk-thm-sf-pf-field", "sk-thm-sf-pf-finite", "sk-thm-sf-pf-proetale", "sk-thm-sf-tensor-hom", "sk-thm-sf-verdier-exchange", "sk-thm-smooth-base-change", "sk-thm-smooth-purity"]
+++
*Theorem (sketch).*

Fix the coefficient stages of [sk-def-sf-setting] and let $f:X\to Y$ be a
separated finite-type morphism of finite-type $k$-schemes. Then the six
operations of [sk-def-sf-operations] exist as functors of the ambient
categories, they descend to the small categories as in [sk-rem-sf-typing],
and they satisfy:

2pt
1. **(1)** *Adjunctions.* $Lf^*:D(Y,\Lambda)\to D(X,\Lambda)$ is left
adjoint to $Rf_*:D^+(X,\Lambda)\to D^+(Y,\Lambda)$; and, whenever $f$ carries
the ambient datum, the ambient functor
$Rf_!:D(X,\Lambda)\to D(Y,\Lambda)$ is left adjoint to the ambient functor
$Rf^{\times}:D(Y,\Lambda)\to D(X,\Lambda)$ of [sk-def-sf-operations] (v), the
restriction of this adjunction to the small categories exhibiting
$Rf^!:\Dctf(Y,\Lambda)\to\Dctf(X,\Lambda)$ as right adjoint of
$Rf_!:\Dctf(X,\Lambda)\to\Dctf(Y,\Lambda)$; units and counits are compatible
with composition, refinements and exchanges
(fix-prop-adjunctions, and [sk-prop-sf-existence] for the existence of
the ambient adjoint).
1. **(2)** *Base change.* $\operatorname{Ex}_!:Lg^*Rf_!\cong Rf'_!Lg'^*$
for every Cartesian square ([sk-prop-sf-cbc]);
$\operatorname{Ex}_*:Lg^*Rf_*\cong Rf'_*Lg'^*$ for proper $f$
([sk-thm-properbasechange]) and for smooth $g$ ([sk-thm-smooth-base-change]) — each an
isomorphism of functors at the categories typed in [sk-def-sf-exchanges].
1. **(3)** *Projection formula.* $\operatorname{PF}_{f,K,L}$ is an
isomorphism in $D^+(Y,\Lambda)$ at every coefficient stage, natural and
coherent
([sk-thm-sf-pf-finite], [sk-prop-sf-pf-reduction],
[sk-thm-sf-pf-adic], [sk-thm-sf-pf-field], [sk-thm-sf-pf-proetale],
[sk-prop-sf-pf-coherence]); the interface
fix-prop-projection-formula is discharged ([sk-rem-sf-pf-done]).
1. **(4)** *Compactifications and proper coincidence.*
$Rf_!=R\bar f_*j_!$ is independent of the compactification with the composition
law $R(gf)_!\cong Rg_!Rf_!$, and $Rf_!\cong Rf_*$ for proper $f$
([sk-prop-sf-comp-coherence], [sk-thm-sf-comp-composition],
[sk-prop-sf-comp-proper]).
1. **(5)** *Orientation.* For smooth $f$ of pure relative dimension $d$
there is a canonical, natural, base-change and composition compatible
isomorphism $Rf^!K\cong Lf^*K(d)[2d]$ of functors
$\Dctf(Y,\Lambda)\to\Dctf(X,\Lambda)$; in particular
$\omega_f\cong\Lambda_X(d)[2d]$ ([sk-thm-smooth-purity], with
[sk-thm-purity-transport] for the remaining coefficient stages).
1. **(6)** *Duality.* $\mathbb D_X:\Dctf(X,\Lambda)\to\Dctf(X,\Lambda)$,
$\mathbb D_X=\RHom_X(-,\omega_X)$, is a contravariant exact anti-equivalence
with $\mathbb D_X\mathbb D_X\cong \mathrm{id}$ ([sk-prop-sf-biduality-general]); the Verdier exchange
$\mathbb D_YRf_!\cong Rf_*\mathbb D_X$, an isomorphism in $D^+(Y,\Lambda)$,
holds ([sk-thm-sf-verdier-exchange]);
for perfect $K$ one has $\mathbb D_XK\cong K^\vee(d)[2d]$
([sk-thm-sf-dual-perfect], [sk-prop-sf-dualizable-biduality]); global
duality $\RG_c(X,K)^\vee\cong\RG(X,\mathbb D_XK)$, an isomorphism in the point
category, holds
([sk-thm-sf-global-duality]); and the derived Poincaré pairing is perfect
and is the duality isomorphism ([sk-thm-sf-identification]).
1. **(7)** *Relative product.*
$R(f\times_Bg)_!(K\boxtimes L)\cong Rf_!K\otimes^LRg_!L$, an isomorphism in
$D^+(B,\Lambda)$, with the supported
form for closed subschemes ([sk-thm-sf-kunneth-relative]).
1. **(8)** *Stability.* The operations descend to the constructible and
finite-Tor subcategories exactly as typed in [sk-thm-sf-ctf-stability] and
[sk-rem-sf-matrix], with the explicit amplitude shifts
$[a,b+2d]$ for $Rf_*$, $[a+c,b+d]$ for $\otimes^L$, $[c-b-2d,d'-a+2d]$
for $\RHom$ of objects with amplitudes $[a,b],[c,d']$ on a scheme of
dimension $\le d$ ($[c-b,d'-a]$ for a site-perfect first argument), and $-2d$, $2c$, $2d+1$ for $Rf^!$ in the smooth, closed and general
cases.

## Proof

Every clause is one of the propositions of §§ *What the earlier chapters prove* or
§§ *What this section proves*, with the following assembly.
Clause (1) is fix-prop-adjunctions together with
[sk-prop-sf-existence], the latter being unconditional on the ordinary
étale derived categories and conditional on $\operatorname{FullCD}$ on the
pro-étale sites, which [sk-prop-sf-fullcd-etale-origin] supplies on the
étale-origin class — enough for every clause below, all of which are typed
on the small categories ([sk-rem-sf-fullcd-scope]). Clause (2) is [sk-prop-sf-cbc], [sk-thm-properbasechange] and
[sk-thm-smooth-base-change] respectively: the first is proved in Chapter 17, the second
in §[sec-proper-base-change], the third in §[sec-smooth-base-change],
and none of them uses anything proved
in this section except the definitions. Clause (3) is the projection-formula
chain of §§ *What this section proves*: the finite case [sk-thm-sf-pf-finite] reduces to
the compact-support projection formula of the framework chapter, and
[sk-prop-sf-pf-reduction], [sk-thm-sf-pf-adic], [sk-thm-sf-pf-field] and
[sk-thm-sf-pf-proetale] transport it to the remaining stages, with
[sk-prop-sf-pf-coherence] for the coherence. Clause (4) is
[sk-thm-nagata-compactification] and [sk-prop-nagata-sketch-comp-category]
for the compactifications themselves, and [sk-prop-sf-comp-coherence],
[sk-thm-sf-comp-composition], [sk-prop-sf-comp-proper] of
§§ *What this section proves* for the independence, the composition law and proper
coincidence. Clause (5) is
[sk-thm-smooth-purity] of §[sec-smooth-purity], with
[sk-prop-cohsm] for the tensor form and [sk-thm-purity-transport] for the
$\mathcal O_E$, $E$ and $\Qlb$ stages; it is what makes the orientation of
[sk-def-sf-orientation] a theorem. Clause (6) is
[sk-prop-sf-biduality-general] (Chapter 1), [sk-thm-sf-verdier-exchange]
and [sk-thm-sf-global-duality] and [sk-thm-sf-identification]
(§§ *What this section proves*, using [sk-thm-sf-tensor-hom]), with
[sk-prop-sf-dualizable-biduality], [sk-lem-sf-twist-interchange] and
[sk-thm-sf-dual-perfect] for the perfect case. Clause (7) is
[sk-thm-sf-kunneth-relative], whose proof uses clause (2), clause (3) and
clause (4). Clause (8) is [sk-thm-sf-ctf-stability], whose proof uses
[sk-lem-sf-flat-model], [sk-thm-sf-direct-image-tor-amplitude],
[sk-cor-sf-direct-image-ctf], [sk-thm-sf-hom-ctf],
[sk-prop-sf-finiteness], [sk-prop-sf-comparison] and
[sk-prop-sf-rf-shriek-preservation]. No clause assumes a property that is
not proved in the blueprint: the *Conditional on* lines of
[sk-prop-sf-existence], [sk-prop-sf-biduality-general] and
[sk-thm-sf-ctf-stability] are the
complete list of what is conditional, and they are restated in the ledger
below.

Uses: `\Cref{cor:sf-direct-image-ctf}`, `\Cref{lem:sf-flat-model}`, `\Cref{lem:sf-twist-interchange}`, `\Cref{prop:cohsm}`, `\Cref{prop:nagata-sketch-comp-category}`, `\Cref{prop:sf-biduality-general}`, `\Cref{prop:sf-cbc}`, `\Cref{prop:sf-comp-coherence}`, `\Cref{prop:sf-comp-proper}`, `\Cref{prop:sf-comparison}`, `\Cref{prop:sf-dualizable-biduality}`, `\Cref{prop:sf-existence}`, `\Cref{prop:sf-finiteness}`, `\Cref{prop:sf-kunneth-ordinary}`, `\Cref{prop:sf-pf-coherence}`, `\Cref{prop:sf-pf-reduction}`, `\Cref{prop:sf-rf-shriek-preservation}`, `\Cref{rem:sf-matrix}`, `\Cref{thm:nagata-compactification}`, `\Cref{thm:properbasechange}`, `\Cref{thm:purity-transport}`, `\Cref{thm:sf-comp-composition}`, `\Cref{thm:sf-ctf-stability}`, `\Cref{thm:sf-direct-image-tor-amplitude}`, `\Cref{thm:sf-dual-perfect}`, `\Cref{thm:sf-global-duality}`, `\Cref{thm:sf-hom-ctf}`, `\Cref{thm:sf-identification}`, `\Cref{thm:sf-kunneth-relative}`, `\Cref{thm:sf-pf-adic}`, `\Cref{thm:sf-pf-field}`, `\Cref{thm:sf-pf-finite}`, `\Cref{thm:sf-pf-proetale}`, `\Cref{thm:sf-tensor-hom}`, `\Cref{thm:sf-verdier-exchange}`, `\Cref{thm:smooth-base-change}`, `\Cref{thm:smooth-purity}`
