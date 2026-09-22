+++
id = "sbc-thm-bounded-derived-smooth-base-change"
kind = "theorem"
title = "Bounded derived smooth base change"
order = 5153
lean = ["AlgebraicGeometry.smooth_base_change_bounded_constructible"]
uses = ["sbc-thm-smooth-base-change", "sbc-def-base-change-map", "sbc-def-base-change-square", "def-sbc-smooth-morphisms", "sbc-prop-extension-by-zero-and-arbitrary-base-change", "sbc-lem-finite-range-comparison"]
+++
In the square [sbc-def-base-change-square] of [sbc-thm-smooth-base-change]
with $f$ smooth and $g$ quasi-compact and quasi-separated, for every
$K\in\Dbc(T_{\Et},\Lambda)$,
$$
\operatorname{BC}_{f,g}(K):Lf^*Rg_*K\xrightarrow{\ \sim\ }Rh_*Le^*K
$$
in $D(X_{\Et},\Lambda)$, where the derived exchange is the one of
[sbc-def-base-change-map].

## Proof

Each $H^q(K)$ is constructible, hence by the finite stratification
filtration (the exact open–closed localization sequence and extension by
zero of [sbc-prop-extension-by-zero-and-arbitrary-base-change]) it is a
finite extension of extensions by zero of finite locally constant sheaves.
Finite locally constant sheaves are torsion with orders invertible on $S$
(the ring $\Lambda$ is annihilated by $N$), so [sbc-thm-smooth-base-change]
together with the compatibility of the base-change map with short exact
sequences gives the isomorphism on the $E_2$ page of the hypercohomology
spectral sequences; since $K$ is bounded,
[sbc-lem-finite-range-comparison] transfers the isomorphisms to the
abutments and gives the displayed isomorphism in the ambient derived
category.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, lem:weil-pbc-five-lemma-transfer, lem:weil-pbc-hypercohomology-convergence
