+++
id = "lem-zl-bertini-finite-cover-curve"
kind = "lemma"
title = "Curves through prescribed points preserving a finite cover"
order = 4050
lean = ["AlgebraicGeometry.Scheme.Hom.exists_isClosedImmersion_connectedSpace_pullback"]
uses = ["def-weil-pbc-scheme-conventions", "def-weil-scheme-morphism-properties"]
+++
Let $X_0$ be a smooth, geometrically connected, affine scheme of
relative dimension $d\geq2$ over a finite field $k_0=\mathbf F_q$, let
$k=\overline{\mathbf F}_q$ and $X=X_0\times_{k_0}k$, let $T\to X$ be a
finite etale morphism with $T$ connected, and let $S\subset X(k)$ be a
nonempty finite set. There are a smooth connected affine curve $C$ over
$k$ and a closed immersion $i:C\hookrightarrow X$ whose image contains
$S$, such that $T\times_X C$ is connected and $C$ is defined over a
finite extension $\mathbf F_{q^m}$, $m\ge1$: there is an automorphism
$\varphi$ of $C$ with $i\circ\varphi=(\mathrm{id}_{X_0}\times\sigma)^m\circ i$,
where $\mathrm{id}_{X_0}\times\sigma$ is the geometric Galois Frobenius
of $X$.
