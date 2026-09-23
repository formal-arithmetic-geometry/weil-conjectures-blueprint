+++
id = "thm-weil-pbc-bounded-below"
kind = "theorem"
title = "Bounded-below derived proper base change"
order = 1742
uses = ["def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-exact-couple-abutment", "lem-weil-pbc-exact-couple-differential", "lem-weil-pbc-hypercohomology-convergence", "prop-weil-pbc-torsion-assembly"]
+++
For a cartesian square [def-weil-pbc-cartesian-square-detailed] with $f$ proper and
every $K\in\Dplus(X_{\Et})$ with torsion cohomology,

$$
 \Ex_{\square,K}:g^{-1}Rf_*K
 \xrightarrow{\sim}Rf'_*g'^{-1}K
$$

is an isomorphism in $\Dplus(Y'_{\Et})$.

## Proof

The exchange morphism of [def-weil-pbc-derived-exchange-detailed] induces the morphism
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
