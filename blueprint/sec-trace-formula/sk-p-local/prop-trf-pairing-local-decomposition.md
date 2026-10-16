+++
id = "prop-trf-pairing-local-decomposition"
kind = "theorem"
title = "Decomposition of the pairing into local terms"
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.integral_supportedPairing_eq_sum_localTermPair"]
order = 2693
tags = ["latex:proposition"]
uses = ["def-trf-correspondence-between-pairs", "def-trf-dualizing-complex", "def-trf-integration", "def-trf-local-term", "def-trf-local-term-pair", "def-trf-supported-pairing", "lem-trf-integration-component-sum", "lem-trf-trace-class-diagonal-pairing", "prop-trf-pairing-point-normalization"]
+++
Let $(C,c,u)$, $(D,d,v)$ be an opposite pair of cohomological
correspondences as in [def-trf-supported-pairing], with intersection
support $E=E(C,D)$ (the fiber product of the two supports of
[def-trf-correspondence-between-pairs]) and Borel–Moore section
$\langle u,v\rangle_{\mathrm{LV}}:A_E\to\omega_{E,A}$. Suppose that
$E$ is a finite disjoint union

$$
E=\coprod_{\beta\in B}\beta
$$

of open-and-closed subschemes $j_\beta:\beta\hookrightarrow E$, each
proper over $s$. For $\beta\in B$ let
$\langle u,v\rangle_{\mathrm{LV}}|_\beta:=j_\beta^*\langle u,v\rangle_{\mathrm{LV}}:A_\beta\to\omega_{\beta,A}$
be the restricted pairing and

$$
\LT_\beta(u,v)=\int_\beta\bigl(\langle u,v\rangle_{\mathrm{LV}}|_\beta\bigr)\in A
$$

the local term of the pair on $\beta$, both as in
[def-trf-local-term-pair]; the restricted pairing is the restriction
of [lem-trf-integration-component-sum] (both are the composite
$A_\beta\simeq Lj_\beta^*A_E\to Lj_\beta^*\omega_{E,A}\cong\omega_{\beta,A}$),
and for $v=1_K$ and $\beta\subseteq\Fix(c)$ the local term is
$\LT_\beta(u)$ of [def-trf-local-term]. Then $E$ is proper over $s$ and

$$
\int_E\langle u,v\rangle_{\mathrm{LV}}
=\sum_{\beta\in B}\LT_\beta(u,v).
$$

If $E=\emptyset$ both sides are $0$. Moreover, for a perfect
$A$-complex $P$ on $s$ and an endomorphism $w:P\to P$, regarded as an
endocorrespondence with support $s$ (whose sole component is $s$),

$$
\LT_s(w)=\LT_s(w,1_P)=\tr_A(w\mid P).
$$
