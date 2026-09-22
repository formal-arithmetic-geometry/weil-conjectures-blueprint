+++
id = "thm-weil-pbc-bounded-below"
kind = "theorem"
title = "Bounded-below derived proper base change"
order = 1187
lean = ["AlgebraicGeometry.Etale.isIso_derivedBaseChangeMapPlus_of_isProper"]
uses = ["prop-weil-pbc-torsion-assembly", "lem-weil-pbc-exact-couple-differential", "lem-weil-pbc-hypercohomology-convergence", "lem-weil-pbc-exact-couple-abutment", "def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange"]
+++
For a cartesian square [def-weil-pbc-cartesian-square] with $f$ proper and
every $K\in\Dplus(X_{\Et})$ with torsion cohomology,

$$
 \Ex_{\square,K}:g^{-1}Rf_*K
 \xrightarrow{\sim}Rf'_*g'^{-1}K
$$

is an isomorphism in $\Dplus(Y'_{\Et})$.

## Proof

The exchange morphism of [def-weil-pbc-derived-exchange] induces the morphism
of hypercohomology spectral sequences whose $E_2$ map is the exchange map for
the torsion cohomology sheaf $\mathcal H^q(K)$, an isomorphism by
[prop-weil-pbc-torsion-assembly]; the differential compatibility is
[lem-weil-pbc-exact-couple-differential]. If $\mathcal H^q(K)=0$ for $q<a$,
then in fixed total degree $n$ only $a\leq q\leq n$ occurs by
[lem-weil-pbc-hypercohomology-convergence], so both filtrations are finite,
exhaustive, and separated. Page induction gives an isomorphism on $E_\infty$,
and induction on the finite filtration gives an isomorphism on each abutment;
the abutment identification [lem-weil-pbc-exact-couple-abutment] identifies
that abutment map with the cohomology map of the named mate, which is
therefore an isomorphism.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-derived-categories
