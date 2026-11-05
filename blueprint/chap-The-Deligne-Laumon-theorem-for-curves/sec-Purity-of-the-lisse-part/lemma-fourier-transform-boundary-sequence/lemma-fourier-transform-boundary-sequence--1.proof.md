+++
kind = "proof"
of = "lemma-fourier-transform-boundary-sequence--1"
order = 1273003
uses = ["lemma-fourier-transform-boundary-sequence--2", "proposition-extension-zero-restriction-closed-subscheme", "prose-16-06"]
+++
The map $j_!M\to j_*M$ is a monomorphism and $B$ is its cokernel.
Rotate the associated distinguished triangle twice to obtain

$$
B\longrightarrow j_!M[1]\longrightarrow j_*M[1]\longrightarrow B[1].
$$

Its middle arrow is the negative of the shifted canonical map.
Apply the triangulated functor $\operatorname{FT}_\psi$ and use
[lemma-fourier-transform-boundary-sequence--2] and the chosen Fourier
partner isomorphism. The resulting triangle has the form

$$
B'[1]\longrightarrow K\longrightarrow(j'_*M')[1]\longrightarrow B'[2],
\qquad K=\operatorname{FT}_\psi(j_!M[1]).
$$

Both outer terms are concentrated in degree $-1$, so exactness of
cohomology sheaves gives $\mathcal H^a(K)=0$ for $a\ne-1$.
Put $G=\mathcal H^{-1}(K)$; then $K\simeq G[1]$.
In the long exact sequence, $\mathcal H^{-2}((j'_*M')[1])$ and
$\mathcal H^0(B'[1])$ vanish. Thus its degree $-1$ part is the required
short exact sequence, after changing the sign of the last map to
recover the canonical map.

In Lean, `AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.fourierCorrectionOfIso`
packages this construction, using
`AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.shortExact_correctionSeq`.
The epimorphism is defined by transporting the Fourier transform of
$j_!M[1]\to j_*M[1]$, which gives the stated compatibility.
Finally, the Fourier transform commutes with shifts, so cancelling
$[1]$ gives $\operatorname{FT}_\psi(j_!M)\simeq G$.
