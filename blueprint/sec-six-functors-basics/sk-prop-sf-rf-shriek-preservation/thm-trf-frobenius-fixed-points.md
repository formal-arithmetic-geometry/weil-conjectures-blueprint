+++
id = "thm-trf-frobenius-fixed-points"
kind = "theorem"
title = "Scheme-theoretic Frobenius fixed points"
lean = ["AlgebraicGeometry.ProEtale.WeilComplex.IsModelFrobenius.finite_fixedPoints", "AlgebraicGeometry.ProEtale.WeilComplex.IsModelFrobenius.mem_finitePoints_of_fixedPoint", "AlgebraicGeometry.ProEtale.WeilComplex.IsModelFrobenius.sum_fixedPoints"]
order = 2433
uses = ["def-trf-fixed-scheme", "def-trf-graph-correspondence", "def-trf-scheme-frobenius", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, let $X_0$ be a
finite-type
$k_0$-scheme, put $X=X_0\times_{k_0}k$, and let
$\Phi:X\to X$ be the $q$-power scheme Frobenius of
[def-trf-scheme-frobenius]. For every $m\in\mathbf Z_{\geq1}$,

$$
\operatorname{Fix}(\Phi^m)\xrightarrow{\ \sim\ }
\coprod_{y\in X_0(\mathbf F_{q^m})}\Spec k,
$$

a canonical isomorphism of the
fixed scheme with the disjoint union of
one copy of $\Spec k$ for each $\mathbf F_{q^m}$-point of $X_0$.
In particular $\operatorname{Fix}(\Phi^m)$ is finite and etale over
$k$, so every fixed point is simple, and the
graph $\Gamma_{\Phi^m}$ and
the diagonal meet transversally with local multiplicity one: on the
smooth locus the differential $d\Phi^m=0$, so
$1-d\Phi^m$ is the identity.
