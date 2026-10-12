+++
id = "prop-weil-pbc-common-stage-calculus"
kind = "theorem"
title = "Common-stage additive and shift calculus"
order = 1368
uses = ["def-weil-pbc-finite-stage-pair-category", "prop-weil-pbc-scalar-extension"]
tags = ["latex:proposition"]
+++
The equivalence relation of [def-weil-pbc-finite-stage-pair-category] is
reflexive, symmetric, and transitive. Transport is additive and obeys
$(u_N)_P=u_P$ for $M\subset N\subset P$. The common-stage operations are
representative-independent and make $\mathcal P_T$ an additive category.
Every finite diagram of objects, morphisms, composites, and asserted
equalities in $\mathcal P_T$ is represented over one finite field, and an
asserted equality holds exactly when it holds after passage to a further
common stage.

Define
$$
 (E,K)[1]=(E,K[1])
$$
and, for $f=[M,u]:(E,K)\to(F,L)$, define
$$
 f[1]=\left[M,
 \sigma_{M/F,L}^{-1}\circ u[1]\circ\sigma_{M/E,K}\right].
$$
This gives a well-defined additive autoequivalence $[1]$ with inverse
$[-1]$, and every finite-stage inclusion
$j_E:\mathcal C_E(T)\to\mathcal P_T$ commutes with shifts through the
specified comparison.
