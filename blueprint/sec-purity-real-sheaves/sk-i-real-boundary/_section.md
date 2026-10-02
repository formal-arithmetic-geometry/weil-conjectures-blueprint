+++
id = "sk-i-real-boundary"
kind = "section"
title = "Boundary stalks and restriction to an open"
order = 2642
uses = ["sk-d-real-boundary", "sk-d-real-setup", "sk-d-real-weil"]
lean = ["AlgebraicGeometry.Scheme.isConstructibleSheaf_lowerStar", "AlgebraicGeometry.Scheme.isIso_unit_upperStarLowerStarAdjunction"]
+++
*Proposition (sketch).*

In the situation of [sk-d-real-boundary]: the sheaf $J=j_*\mathcal F$
is constructible, and $J_{\bar s}=V_s^{I_s}$ equivariantly for Frobenius.
If $\mathcal G$ is lisse on all of $C_0$, then
$\mathcal G\simeq j_*(\mathcal G|_{U_0})$. The map
$\pi_1(U)\to\pi_1(C)$ is surjective, and hence so is the Weil-group map
of [sk-d-real-weil].

## Proof

*Step 0 (normality).* $C_0$ is a smooth curve, hence normal and
integral, and an etale scheme over a normal integral scheme is a finite
disjoint union of open-and-closed normal integral schemes, normality
ascending along etale ring maps
([Stacks `033C`](https://stacks.math.columbia.edu/tag/033C)).
This is used in every step below.

*Step 1 (constructibility of $J$).* Trivialize $\mathcal F$ by a
finite etale surjection $p:P\to U_0$, so that $p^*\mathcal F$ is constant
with finite fibre $M_a$ on each connected component $P_a$. The
adjunction unit $\mathcal F\to p_*p^*\mathcal F$ is injective, being a
diagonal into a nonempty finite product on stalks, so
$J\hookrightarrow\prod_a(jp_a)_*\underline{M_a}$. Extend $P_a$ to the
normalization $g_a:Y_a\to C_0$ in $k(P_a)$, which is finite and restricts
over $U_0$ to $P_a$; by Step 3 below applied on the normal integral
$Y_a$, the constant sheaf extends, so
$(jp_a)_*\underline{M_a}=g_{a,*}\underline{M_a}$, which is constructible
because $g_a$ is finite. A finite product of constructible sheaves is
constructible, and on a Noetherian scheme a subobject of a constructible
sheaf is constructible; hence $J$ is.

*Step 2 (the boundary stalk).* The stalk of $J$ at a geometric
boundary point $\bar s$ is computed on the punctured strict henselian
trait at $s$. The strict-henselization stalk formula identifies it with
the invariants of the geometric generic stalk under the inertia group
$I_s=\Gal(\overline{K_s}/K_s^{\mathrm{sh}})$, i.e. with $V_s^{I_s}$,
where $K_s$ is the fraction field of the henselization as in
[sk-d-real-boundary] and $K_s^{\mathrm{sh}}\subset\overline{K_s}$ is
the fraction field of the strict henselization, the generic point of the
trait. Since $\Gal(K_s^{\mathrm{sh}}/K_s)=\Gal(\overline{k(s)}/k(s))$,
this is the kernel of
$\Gal(\overline{K_s}/K_s)\to\Gal(\overline{k(s)}/k(s))$ of
[sk-d-real-boundary], whereas $\Gal(\overline{K_s}/K_s)$ itself is the
decomposition group.
The Weil structures descend through the trait, so the identification is
equivariant for the residue Frobenius lift.

*Step 3 (lisse sheaves extend from a dense open).* For a finite
module $M$ on a normal integral Noetherian $Y$ and a nonempty open
$v:V\hookrightarrow Y$, the canonical map
$\underline M_Y\to v_*\underline M_V$ is an isomorphism: evaluate on an
affine etale $W\to Y$, decompose $W$ by Step 0, and note that each
component meets $W\times_YV$ because it is integral and $V$ is dense, so
a section over $W\times_YV$ is determined by, and extends to, a section
over $W$. For $\mathcal G$ lisse on $C_0$, trivialize as in Step 1 and
apply this componentwise; this gives
$\mathcal G\simeq j_*(\mathcal G|_{U_0})$.

*Step 4 (surjectivity on fundamental groups).* Let $W\to C$ be
connected finite etale. By Step 0 it is normal integral, hence its
restriction $W\times_CU$ is again integral, so connected: a connected
cover of $C$ stays connected over the nonempty open $U$. Equivalently
$\pi_1(U)\to\pi_1(C)$ is surjective. The Weil-group map of
[sk-d-real-weil] is the pullback of this one along the degree map to
$\mathbf Z$, so it is surjective too.

The detailed forms are Blueprint 07, `lem-fin-normal-open-lisse-image`
(Step 1), `lem-fin-normal-constant-open-image` (Step 3),
`lem-fin-etale-normal-components` (Steps 0 and 4),
`fin2-lem-lisse-trivialized-finite-etale` and
`lem-fin-normalization-extends-cover`; and Blueprint 12,
`lem-wf-boundary-stalk-invariants` (Step 2), resting on
Blueprint 02, `prop-weil-pbc-strict-henselization-stalk-formula`.

Uses: [sk-d-real-boundary], [sk-d-real-setup], [sk-d-real-weil]
