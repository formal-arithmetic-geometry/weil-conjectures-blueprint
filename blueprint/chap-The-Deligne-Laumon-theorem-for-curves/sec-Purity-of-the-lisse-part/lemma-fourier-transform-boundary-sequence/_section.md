+++
id = "lemma-fourier-transform-boundary-sequence"
kind = "lemma"
title = "Fourier transform of the boundary sequence"
order = 1273
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.nonempty_fourierCorrection", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.fourierTransformExtensionByZeroIso", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.exists_isLisse_iso_fourierTransform_boundarySheaf"]
uses = ["definition-weil-structure", "definition-lisse-sheaves", "definition-weights", "prose-16-06", "proposition-fourier-transform-middle-extension"]
+++
Put $B=j_*M/j_!M$. There are sheaves $G$ and $B'$ on the dual line such
that $\operatorname{FT}_\psi(j_!M)=G$, $\operatorname{FT}_\psi(B)=B'[1]$,
and the sequence

$$
0\longrightarrow B'\longrightarrow G
\longrightarrow j'_*M'\longrightarrow0
$$

is exact. The sheaf $B'$ is lisse on the entire dual line and has weights at
most $w$.
