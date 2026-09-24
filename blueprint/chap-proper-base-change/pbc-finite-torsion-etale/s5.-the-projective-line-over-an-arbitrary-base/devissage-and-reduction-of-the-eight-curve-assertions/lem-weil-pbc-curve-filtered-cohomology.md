+++
id = "lem-weil-pbc-curve-filtered-cohomology"
kind = "lemma"
title = "Filtered cohomology on a curve"
order = 1711
uses = ["def-weil-pbc-eight-curve-assertions-detailed", "def-weil-pbc-etale-sheaves", "lem-weil-pbc-cohomology-filtered-colimit"]
+++
For a quasi-compact quasi-separated curve $C$ and a filtered system of torsion
etale sheaves $(F_i)$,

$$
 \varinjlim_iH^q(C,F_i)\xrightarrow{\sim}
 H^q(C,\varinjlim_iF_i)
$$

for every $q$. This isomorphism commutes with extension of the ground field.

## Proof

Apply the filtered-colimit theorem for etale cohomology to the given
quasi-compact quasi-separated scheme $C$. For a ground-field extension,
pullback of the hypercovers, sections and cocycles in that proof gives the
maps $\rho^q_{k'/k}$ of [def-weil-pbc-eight-curve-assertions-detailed].
Pullback commutes with the sheaf colimit, and hence with the canonical
comparison maps. This proves the stated compatibility.
