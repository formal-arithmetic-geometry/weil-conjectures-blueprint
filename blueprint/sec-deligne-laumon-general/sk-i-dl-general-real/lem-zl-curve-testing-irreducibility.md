+++
id = "lem-zl-curve-testing-irreducibility"
kind = "lemma"
title = "Curve testing for geometric irreducibility"
order = 2832
lean = ["AlgebraicGeometry.LAdicWeilSheaf.exists_isClosedImmersion_isIrreducibleLocalSystem_upperStar"]
uses = ["def-weil-pbc-qbar-category", "def-wf-fundamental-representation", "lem-zl-bertini-finite-cover-curve", "lem-zl-finite-matrix-irreducibility"]
+++
Let $X_0$ be a smooth, geometrically connected, affine scheme of
relative dimension $d\geq1$ over a finite field $k_0=\mathbf F_q$, with
$X=X_0\times_{k_0}\overline{\mathbf F}_q$, and let
$\mathcal S_1,\ldots,\mathcal S_r$ be $\Qlb$-Weil sheaves on $X_0$ whose
geometric restrictions to $X$ are irreducible local systems. Let $S$ be
a nonempty finite set of $\overline{\mathbf F}_q$-points of $X$. There
are a smooth connected affine curve $C$ over $\overline{\mathbf F}_q$
and a closed immersion $i:C\hookrightarrow X$ whose image contains $S$,
such that every $i^*\mathcal S_j$ is an irreducible local system on $C$,
and $C$ is defined over a finite extension $\mathbf F_{q^m}$, $m\ge1$:
there is an automorphism $\varphi$ of $C$ with
$i\circ\varphi=(\mathrm{id}_{X_0}\times\sigma)^m\circ i$, where
$\mathrm{id}_{X_0}\times\sigma$ is the geometric Galois Frobenius of
$X$.
