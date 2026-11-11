+++
id = "lemma-fourier-transform-boundary-sequence"
kind = "lemma"
title = "Fourier transform of the boundary sequence"
order = 1276
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.hasWeightsAtMost", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.isLisse"]
uses = ["lemma-stability", "proposition-six-operations-change-coefficients", "lemma-artin-schreier-character-sheaf", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
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
