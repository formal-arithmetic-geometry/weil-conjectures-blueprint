+++
kind  = "proof"
of    = "sk-p-dl-a1-correction"
+++
By the stalk formula ([sk-thm-inversion]), the stalk of
$\operatorname{FT}_\psi(j_!M)$ at $y$ is
$R\Gamma_c(U,M\otimes\mathcal L_{\psi(yx)})[1]$. The group in
degree zero vanishes by [sk-l-dl-a1-endpoints], and the group in
degree two vanishes because a nonzero coinvariant would give $M$ a
geometric rank-one quotient of the form excluded by
Fourier-genericity. Thus the transform is a sheaf $G$.
After geometric base change, the punctual sheaf $B$ is a finite sum of
skyscrapers with coefficient modules, and the transform of each is a
linear character sheaf tensored with that module, shifted by one.
Hence $B'$ is lisse. Now apply the Fourier transform to the triangle
of $0\to j_!M\to j_*M\to B\to0$. The isomorphism of
[sk-p-dl-a1-middle] identifies the transform of the middle term with
$j'_*M'$, and the long exact sequence of ordinary cohomology sheaves
gives the stated exact sequence.

For the weights, boundary semicontinuity ([sk-p-real-semi]) bounds the
weights of the stalks of $B$ by $w$, and a character sheaf has weight
zero ([sk-lem-as-properties]). At a boundary point that is not
rational, Frobenius permutes the geometric summands, and on a cycle
its power is the original local Frobenius times a root of unity.
Taking this power raises the residue cardinality to the same exponent,
so the normalized bound is preserved.

To obtain the filtration, choose for each boundary point, over its
residue field, a Frobenius-stable flag of the coefficient module whose
successive quotients are one-dimensional eigenspaces. Tensoring with
the linear character sheaves and summing over the Frobenius orbit, we
obtain a finite Weil filtration of $B'$ whose quotients are pure of
the weights of the coefficient eigenvalues, and these weights are at
most $w$.
