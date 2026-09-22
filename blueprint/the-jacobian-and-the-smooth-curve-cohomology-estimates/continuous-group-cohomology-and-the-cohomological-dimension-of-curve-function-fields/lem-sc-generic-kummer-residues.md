+++
id = "lem-sc-generic-kummer-residues"
kind = "lemma"
title = "The generic Kummer residue sheaf"
order = 4527
lean = ["AlgebraicGeometry.Curve.r1genericPushforward_mu_iso"]
uses = ["prop-weil-pbc-strict-henselization-stalk-formula"]
+++
Let $C/k$ be a smooth integral separated curve, with $k$ algebraically
closed. Let $n>0$ be invertible in $k$, let $\mu_n$ be the sheaf of $n$-th
roots of unity, and let $\eta:\operatorname{Spec}k(C)\to C$ be the generic
point. Valuations at closed points give an isomorphism
$$
R^1\eta_*\mu_n\ \simeq\ \bigoplus_{x\in C_{\rm cl}}i_{x*}\mathbf Z/n.
$$

## Proof

Kummer's polynomial construction gives $H^1(E,\mu_n)=E^\times/E^{\times n}$
for any field $E$; the next term $H^1(E,\mathbf G_m)$ is zero by Hilbert 90.

On a quasi-compact étale curve $V\to C$, its generic fibre is a finite
disjoint union of fields. Take the valuations of a representing rational
function at the closed points of $V$. Only finitely many valuations are
nonzero, so these maps land in the direct sum. They commute with étale
restriction: an étale extension of discrete valuation rings has ramification
index one. They therefore define the displayed map after sheafification of
the cohomology presheaf.

At a geometric closed point the strict-henselization stalk formula
[prop-weil-pbc-strict-henselization-stalk-formula]
identifies the map with
$$
E^\times/E^{\times n}\longrightarrow\mathbf Z/n,\qquad a\longmapsto v(a)\bmod n,
$$
where $E$ is the fraction field of the strict local ring $R$. This is a
discrete valuation ring, by regularity of smooth curves. Every unit of $R$
has an $n$-th root: choose a root in its separably closed residue field and
lift it by Hensel's lemma, since the derivative is a unit. A uniformizer has
valuation one. Thus the stalk map is bijective. Both generic stalks are
zero. The isomorphism follows from the exactness of geometric stalks.

Unresolved dependencies: def:sc-curves, def:sc-function-field, def:sc-kummer-sequence, def:sc-divisor, lem:sc-smooth-regular, lem:sc-regular-dim1-dvr, prop:weil-pbc-geometric-stalks-exact
