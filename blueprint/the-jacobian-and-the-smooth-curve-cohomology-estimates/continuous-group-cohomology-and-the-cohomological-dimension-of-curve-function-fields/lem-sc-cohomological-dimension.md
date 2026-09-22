+++
id = "lem-sc-cohomological-dimension"
kind = "lemma"
title = "Cohomological dimension of a smooth curve"
order = 4526
lean = ["AlgebraicGeometry.Curve.cohomology_eq_zero_of_two_lt"]
uses = ["prop-weil-pbc-strict-henselization-stalk-formula", "lem-sc-generic-cohomology-comparison", "lem-sc-function-field-cd-one", "lem-sc-zero-generic-acyclic"]
+++
For a smooth separated curve $C$ over an algebraically closed field and any
torsion étale sheaf $F$, one has $H^q(C,F)=0$ for $q>2$.

## Proof

Work on one of the finitely many disjoint integral components of the smooth
curve. By [lem-sc-generic-cohomology-comparison] it suffices to treat
$\eta_*M$.

At a closed point the strict local ring of $C$ is a discrete valuation ring,
by regularity of smooth curves together with the preservation of regularity
and dimension under étale localization. Its fraction field is algebraic over
$k(C)$: a strict henselization is a filtered union of étale neighborhoods
and their fraction fields are finite separable extensions. By the
strict-henselization stalk formula [prop-weil-pbc-strict-henselization-stalk-formula] and
[lem-sc-function-field-cd-one],
$R^q\eta_*M=0$ for $q>1$. The sheaf $R^1\eta_*M$ has zero generic
restriction, hence is acyclic by [lem-sc-zero-generic-acyclic].

The ordinary Grothendieck spectral sequence for sections composed with
$\eta_*$ has terms $H^a(C,R^b\eta_*M)$ and converges to $H^{a+b}(k(C),M)$.
Direct image takes injectives to injectives because its left adjoint is
exact, so the required acyclicity holds. The only row above $b=0$ is $b=1$,
and its only possibly nonzero term is at $a=0$. For total degree $q>2$ there
are thus no differentials into or out of $H^q(C,\eta_*M)$. It equals
$H^q(k(C),M)=0$, by [lem-sc-function-field-cd-one].

Unresolved dependencies: def:sc-curves, def:weil-pbc-etale-sheaves, def:weil-pbc-etale-cohomology, lem:sc-smooth-regular, lem:sc-regular-dim1-dvr, thm:sp-grothendieck
