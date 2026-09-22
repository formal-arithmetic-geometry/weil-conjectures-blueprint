+++
id = "prop-weil-pbc-property-iff-acyclicity"
kind = "theorem"
title = "Equivalence of proper base change and acyclicity"
order = 2123
lean = ["AlgebraicGeometry.Etale.isBaseChangeIso_iff_isInjectiveAcyclic"]
uses = ["def-weil-pbc-property-detailed", "def-weil-pbc-injective-acyclicity", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-leray-acyclicity", "lem-weil-pbc-underived-proper-exchange", "def-weil-pbc-derived-exchange-detailed", "lem-weil-pbc-prime-factor-devissage", "lem-weil-pbc-five-lemma-transfer", "lem-weil-pbc-torsion-filtered-union", "lem-weil-pbc-direct-image-filtered-colimit"]
+++
For a proper morphism [def-weil-pbc-scheme-conventions] $f$, the following
conditions are equivalent.

1. $\mathrm{PBC}(f)$ holds in the sense of
   [def-weil-pbc-property-detailed].
2. $\mathrm{IA}_r(f)$ holds for every prime $r$ in the sense of
   [def-weil-pbc-injective-acyclicity].

## Proof

Suppose $\mathrm{PBC}(f)$ holds. If $I$ is injective among $\mathbf
F_r$-module sheaves, then $Rf_*I=f_*I$ in that category; after arbitrary base
change, [def-weil-pbc-property-detailed] identifies $Rf'_*g'^{-1}I$ with the
degree-zero complex $g^{-1}f_*I$, so $R^qf'_*g'^{-1}I=0$ for $q>0$, which is
$\mathrm{IA}_r(f)$ by [def-weil-pbc-injective-acyclicity].

Conversely assume $\mathrm{IA}(f)$. For an $\mathbf F_r$-module sheaf $E$,
take an injective resolution $E\to I^\bullet$. Acyclicity and
[lem-weil-pbc-leray-acyclicity] make $f'_*g'^{-1}I^\bullet$ compute
$Rf'_*g'^{-1}E$, while $g^{-1}f_*I^\bullet$ computes $g^{-1}Rf_*E$; the
underived proper exchange of [lem-weil-pbc-underived-proper-exchange] is an
isomorphism in every degree, and by naturality these maps form an isomorphism
of complexes, which is the derived exchange morphism of
[def-weil-pbc-derived-exchange-detailed]. For a sheaf $F$ killed by $n$,
induction on the number of prime factors of $n$ using the exact sequence of
[lem-weil-pbc-prime-factor-devissage] and the five-lemma transfer of
[lem-weil-pbc-five-lemma-transfer] gives the assertion for $F[n]$. Finally
every torsion sheaf is the filtered union of the $F[n]$ by
[lem-weil-pbc-torsion-filtered-union], and
[lem-weil-pbc-direct-image-filtered-colimit] passes the isomorphism to the
colimit, since proper maps are quasi-compact and quasi-separated. This proves
$\mathrm{PBC}(f)$ by [def-weil-pbc-property-detailed].
