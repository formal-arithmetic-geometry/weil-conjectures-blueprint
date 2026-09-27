+++
id = "sk-thm-smooth-purity"
kind = "section"
title = "Finite-coefficient smooth purity"
order = 2008
uses = ["sk-def-purity-conv", "sk-lem-diag-reg", "sk-prop-an", "sk-prop-cohsm", "sk-thm-dnc"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_dualizingComplex_twistShift", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_twistShift"]
+++
*Theorem (sketch).*

In the conventions of [sk-def-purity-conv], let $f:X\to Y$ be smooth
separated of pure relative dimension $d$. Then

$$
\omega_f=Rf^{!}\Lambda_Y\ \cong\ \Lambda_X(d)[2d],
$$

canonically; for every $K\in D^b_{ctf}(Y,\Lambda)$ the tensor formula
[sk-prop-cohsm] (b) gives the purity isomorphism

$$
Rf^{!}K\ \cong\ Lf^{*}K(d)[2d].
$$

These isomorphisms are compatible with base change and with composition
of smooth morphisms (twist additivity).

## Proof

Put $W=X\times_YX$, let $p_1,p_2$ be its projections and let
$\Delta:X\hookrightarrow W$ be the diagonal.
*Step 1: the section invariant of the diagonal is $\omega_f$.* The
square with $p_1,p_2$ over $f$ is Cartesian and $p_1$ is the base change of
$f$, so $\omega_{p_1}\cong Lp_2^{*}\omega_f$ by [sk-prop-cohsm] (c). Since
$p_2\circ\Delta=\mathrm{id}_X$,

$$
\mathcal C(p_1,\Delta)=L\Delta^{*}\omega_{p_1}
\cong L\Delta^{*}Lp_2^{*}\omega_f\cong\omega_f .
$$

*Step 2: the deformation to the normal cone of that section.* $\Delta$
is a closed section of the smooth map $p_1$, with normal bundle
$N_\Delta\cong T_{X/Y}$ of rank $d$ by [sk-lem-diag-reg]. Applying
[sk-thm-dnc] to $(p_1,\Delta)$ gives

$$
\mathcal C(p_1,\Delta)\ \cong\ \mathcal C(\pi_T,0_T),\qquad
\pi_T:T_{X/Y}\to X .
$$

*Step 3: the other side is the Tate twist.* Vector-bundle purity
[sk-prop-an] applied to $\pi_T$ gives
$\omega_{\pi_T}=R\pi_T^{!}\Lambda_X\cong\Lambda_{T_{X/Y}}(d)[2d]$, and
pulling back along the zero section,

$$
\mathcal C(\pi_T,0_T)=L0_T^{*}\omega_{\pi_T}
\cong L0_T^{*}\Lambda_{T_{X/Y}}(d)[2d]\cong\Lambda_X(d)[2d].
$$

Combining the three steps gives $\omega_f\cong\Lambda_X(d)[2d]$. Every step
is canonical, by the uniqueness clause of [sk-thm-dnc]; base-change
compatibility follows from that of the diagonal, of [sk-thm-dnc] and of
[sk-prop-an], the normal bundle of the diagonal of a base change being the
base change of the normal bundle. Substitution into [sk-prop-cohsm] (b)
gives the purity map for every $K$. Compatibility with composition is
that of [sk-prop-cohsm] (a),(c) and of the twist.

Uses: [sk-def-purity-conv], [sk-lem-diag-reg], [sk-prop-an], [sk-prop-cohsm], [sk-thm-dnc]
