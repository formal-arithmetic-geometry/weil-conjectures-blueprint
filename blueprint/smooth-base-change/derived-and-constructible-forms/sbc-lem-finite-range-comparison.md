+++
id = "sbc-lem-finite-range-comparison"
kind = "lemma"
title = "Finite-range comparison"
order = 2802
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-hypercohomology-filtrations-detailed"]
+++
If $H^q(K)=0$ outside $[a,b]$ and the comparison of the two
hypercohomology spectral sequences of
[def-weil-pbc-hypercohomology-filtrations-detailed] is an isomorphism on
every $E_2^{p,q}$, then it is an isomorphism on every abutment
$H^n\cong H^n$, and hence
${\operatorname{BC}}_{f,g}(K)$ is an isomorphism.

## Proof

For a fixed total degree $n$, the abutment $H^n$ of
[def-weil-pbc-hypercohomology-filtrations-detailed] has a finite filtration
with associated graded pieces the $E_\infty^{p,q}$ with $p+q=n$, of
which only those with $q\in[a,b]$ are nontrivial; if the comparison is
an isomorphism on every $E_2^{p,q}$ it is an isomorphism on every
$E_\infty^{p,q}$, hence by induction along the finite filtration on
$H^n$.
