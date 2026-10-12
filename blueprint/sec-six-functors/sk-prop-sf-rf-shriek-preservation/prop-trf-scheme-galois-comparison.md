+++
id = "prop-trf-scheme-galois-comparison"
kind = "theorem"
title = "Comparison of scheme and Galois pullbacks"
order = 2416
tags = ["latex:proposition"]
uses = ["def-trf-scheme-frobenius", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions", "lem-trf-absolute-frobenius-site", "prop-trf-frobenius-factorization"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, let $X_0$ be a
finite-type $k_0$-scheme,
put $X=X_0\times_{k_0}k$, and let $A$ be a finite commutative ring
annihilated by an integer invertible in $k$. The $q$-power scheme
Frobenius $\Phi$ and the
geometric-Frobenius automorphism
$g_\gamma$ of [def-trf-scheme-frobenius] induce, on the
small pro-etale site of $X$,
natural isomorphisms of derived categories

$$
\kappa:L\Phi^*\xrightarrow{\ \sim\ }Lg_\gamma^*,
$$

and, for every $m\geq1$, a multiplicative iterate

$$
\kappa^{(m)}:L\Phi^m{}^*\xrightarrow{\ \sim\ }Lg_\gamma^{m*}.
$$

The isomorphisms are compatible with the factorization of
[prop-trf-frobenius-factorization]: scheme Frobenius and geometric
Galois Frobenius differ by a universal homeomorphism, namely the
absolute $q$-power Frobenius.
