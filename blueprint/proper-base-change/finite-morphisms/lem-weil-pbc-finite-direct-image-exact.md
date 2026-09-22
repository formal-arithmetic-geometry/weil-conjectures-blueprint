+++
id = "lem-weil-pbc-finite-direct-image-exact"
kind = "lemma"
title = "Exactness of finite direct image"
order = 1072
lean = ["AlgebraicGeometry.Etale.exact_lowerStar_of_isFinite", "AlgebraicGeometry.Etale.isZero_rightDerivedLowerStar_of_isFinite"]
uses = ["lem-weil-pbc-finite-stalk-formula"]
+++
For finite $f$, the functor $f_*:\Ab(X_{\Et})\to\Ab(Y_{\Et})$ is exact.
Consequently $R^qf_*=0$ for $q>0$ and $Rf_*=f_*$ on $\Dplus(X_{\Et})$.

## Proof

By [lem-weil-pbc-finite-stalk-formula], a short exact sequence of sheaves
becomes, at every geometric stalk of the target, a finite direct sum of short
exact sequences at the geometric points of the finite fibre; since the stalk
functors are exact and jointly conservative, $f_*$ is exact. The vanishing of
the higher derived functors follows.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-direct-image, def:weil-pbc-geometric-stalks
