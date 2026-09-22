+++
id = "lem-kun-0F11"
kind = "lemma"
title = "Direct sums and finite cohomological dimension"
order = 6095
lean = ["AlgebraicGeometry.Etale.derivedPushforward_preservesCoproducts_of_cd"]
uses = ["def-weil-pbc-hypercohomology-filtrations", "def-kun-cd", "def-kun-rgamma-unbounded"]
+++
Let $n\ge1$, and let $f:X\to Y$ be a quasi-compact and quasi-separated
morphism with $\operatorname{cd}(f)<\infty$.

1. $Rf_*:D(X_{\Et},\mathbf Z/n\mathbf Z)\to D(Y_{\Et},\mathbf Z/n\mathbf Z)$
   commutes with set-indexed direct sums.
2. If $X$ is a qcqs scheme with $\operatorname{cd}(X)<\infty$, then
   $R\Gamma(X_{\Et},-):D(X_{\Et},\mathbf Z/n\mathbf Z)\to D(\mathbf Z/n\mathbf Z)$
   commutes with set-indexed direct sums.

## Proof

*Step 1 (sheaves).* A set-indexed direct sum of torsion sheaves is the
filtered colimit of its finite partial sums, with split-injective transition
maps, so for every $q$ the canonical map
$$
\bigoplus_iR^qf_*F_i\longrightarrow R^qf_*\Bigl(\bigoplus_iF_i\Bigr)
$$
is an isomorphism by the compatibility of direct image with filtered
colimits (and the same argument with $f$ the structure morphism gives the
statement for $R\Gamma(X_{\Et},-)$).

*Step 2 (complexes).* For $K_i\in D(X_{\Et},\mathbf Z/n\mathbf Z)$ the
hypercohomology spectral sequences for the $K_i$ and for $\bigoplus_iK_i$
have $E_2$-pages $R^pf_*\mathcal H^q(K_i)$ respectively
$R^pf_*\mathcal H^q(\bigoplus_iK_i)$, and
$\mathcal H^q(\bigoplus_iK_i)=\bigoplus_i\mathcal H^q(K_i)$, so Step 1
identifies the second $E_2$-page with the direct sum of the first. The
truncation construction of the spectral sequence is compatible with direct
sums, so the spectral sequence of the direct sum is the direct sum of the
spectral sequences; both converge in the half-plane sense, and a direct sum
of separated exhaustive filtrations is separated and exhaustive. Hence the
abutments agree:
$$
\mathcal H^n\Bigl(Rf_*\bigoplus_iK_i\Bigr)\cong\bigoplus_i\mathcal H^n(Rf_*K_i)\qquad(n\in\mathbf Z).
$$

The finiteness hypothesis $\operatorname{cd}(f)<\infty$ is not needed for
the argument and is retained only to match the classical formulation.

Unresolved dependencies: def:weil-pbc-scheme-conventions, lem:weil-pbc-direct-image-filtered-colimit, lem:weil-pbc-hypercohomology-convergence, def:weil-pbc-derived-categories
