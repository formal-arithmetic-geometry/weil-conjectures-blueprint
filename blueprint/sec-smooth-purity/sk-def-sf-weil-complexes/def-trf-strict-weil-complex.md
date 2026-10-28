+++
id = "def-trf-strict-weil-complex"
kind = "definition"
title = "Strict Weil complex at finite coefficients"
lean = ["AlgebraicGeometry.ProEtale.StrictWeilComplex", "AlgebraicGeometry.ProEtale.StrictWeilComplex.Hom", "AlgebraicGeometry.ProEtale.StrictWeilComplex.hom_ext", "AlgebraicGeometry.ProEtale.StrictWeilComplex.forget", "AlgebraicGeometry.ProEtale.GeometricFiberStrictWeilComplex", "AlgebraicGeometry.ProEtale.StrictWeilComplex.map_hom_eq_zero_of_iso_unit", "AlgebraicGeometry.ProEtale.GeometricFiberStrictWeilComplex.map_hom_eq_zero_of_iso_unit"]
order = 3017
uses = ["def-trf-coefficient-conventions", "def-trf-scheme-frobenius", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-field-fiber", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "sk-def-sf-weil-complexes"]
+++
Fix the global finite-field datum
and the coefficient
conventions of this trace-formula blueprint: $A=A_{E,n}$, $X_0$
separated finite type over $k_0$, $X=X_0\times_{k_0}k$, on the
small pro-etale site. A
*strict Weil complex at $A$* is a pair $(K,\varphi)$ with
$K\in D^b_{ctf}(X,A)$ and an isomorphism formed using the
derived pullback

$$
\varphi:Lg_\gamma^*K\xrightarrow{\ \sim\ }K,
$$

where $g_\gamma=g_X$ is the
geometric-Frobenius
automorphism of [def-trf-scheme-frobenius]; morphisms are morphisms
of $K$ commuting with $\varphi$. Write
$D^b_{ctf,\mathrm W}(X,A)$ for the resulting category, the finite
admissible coefficient ring of the
Weil-complex category of
the trace-formula chapter, with its forgetful functor $\operatorname{For}$.
This is the case $\Lambda=A$ of the Weil complexes of
[sk-def-sf-weil-complexes]: a category of pairs over $D^b_{ctf}(X,A)$, not a
triangulated (derived) category of Weil sheaves.

Its Hom-groups are not Ext groups of Weil sheaves: a nonsplit Frobenius
extension of $A$ by $A$ (a Jordan block) gives no nonzero map $A\to A[1]$ of
pairs.
