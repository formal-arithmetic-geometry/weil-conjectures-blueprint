+++
kind = "proof"
of = "corollary-plancherel--2"
order = 1238004
uses = ["corollary-plancherel--1", "definition-growth-squared-traces"]
+++
Specialize [corollary-plancherel--1] to a one-element coordinate set.
This gives
`AlgebraicGeometry.WeilComplex.traceEnergy_fourierTransform`:
$S_n(\operatorname{FT}_\psi K)=q^nS_n(K)$ for $n\ge1$. Hence, for
each $\beta\in\mathbf R$,

$$
\frac{S_n(\operatorname{FT}_\psi K)}{q^{n(\beta+1)}}
=\frac{S_n(K)}{q^{n((\beta-1)+1)}}
\qquad(n\ge1).
$$

The two sequences have the same limsup, since they agree from $n=1$
onwards. Thus $\beta$ belongs to the set defining
$\nu(\operatorname{FT}_\psi K)$ if and only if $\beta-1$ belongs to
the set defining $\nu(K)$. For the first inequality, each such
$\beta$ is at most $\nu(K)+1$. Conversely, each $\gamma$ in the set
defining $\nu(K)$ gives $\gamma+1$ in the set defining the transform's
growth parameter. Taking suprema in both directions proves the
identity, also when either supremum is infinite.
