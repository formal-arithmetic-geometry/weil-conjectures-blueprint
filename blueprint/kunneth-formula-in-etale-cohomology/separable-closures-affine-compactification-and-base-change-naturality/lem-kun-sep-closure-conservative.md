+++
id = "lem-kun-sep-closure-conservative"
kind = "lemma"
title = "Conservativity of base change to a separable closure"
order = 6104
lean = ["AlgebraicGeometry.Etale.pullback_sepClosure_conservative"]
uses = ["def-kun-separably-closed", "lem-kun-stalk-as-pullback"]
+++
Let $X$ be a scheme over a field $K$. Every geometric point of $X$ factors
through $X_{K^{\mathrm{sep}}}$, and consequently the pullback functor along
$X_{K^{\mathrm{sep}}}\to X$ is conservative: a morphism of abelian sheaves (or
of derived objects) on $X_{\Et}$ is an isomorphism if and only if its pullback
to $(X_{K^{\mathrm{sep}}})_{\Et}$ is an isomorphism.

## Proof

Let $\bar x:\Spec(\Omega)\to X$ be a geometric point; $\Omega$ is
algebraically closed and contains $\kappa(x)$, hence contains the algebraic
closure of $K$, in particular $K^{\mathrm{sep}}$, so $\bar x$ factors as
$\Spec(\Omega)\to X_{K^{\mathrm{sep}}}\to X$. If $\alpha$ becomes an
isomorphism after pullback to $X_{K^{\mathrm{sep}}}$, then its stalk at
$\bar x$ (the pullback along $\bar x$, see [lem-kun-stalk-as-pullback]) is an
isomorphism as it factors through the pullback along
$\Spec(\Omega)\to X_{K^{\mathrm{sep}}}$; all stalks are isomorphic, so
$\alpha$ is an isomorphism by the conservativity of geometric stalks (and
[lem-kun-stalk-faithful-derived] in the derived case).

Unresolved dependencies: def:weil-pbc-geometric-stalks, lem:weil-pbc-geometric-stalk-conservative, def:weil-pbc-scheme-conventions
