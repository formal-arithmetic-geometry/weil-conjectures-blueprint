+++
id = "lem-weil-pbc-finite-direct-image-exact"
kind = "lemma"
title = "Exactness of finite direct image"
order = 1558
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-finite-stalk-formula"]
+++
For finite $f$, the functor $f_*:\Ab(X_{\Et})\to\Ab(Y_{\Et})$ is exact.
Consequently $R^qf_*=0$ for $q>0$ and $Rf_*=f_*$ on $\Dplus(X_{\Et})$.

## Proof

By [lem-weil-pbc-finite-stalk-formula], a short exact sequence of sheaves
becomes, at every geometric stalk of the target, a finite direct sum of short
exact sequences at the geometric points of the finite fibre; since the stalk
functors are exact and jointly conservative, $f_*$ is exact. The vanishing of
the higher derived functors follows.
