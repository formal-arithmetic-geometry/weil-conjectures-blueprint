+++
id = "sk-p-dl-a1-correction"
kind = "proposition"
title = "The zero-extension comparison"
order = 3105
uses = ["sk-p-dl-a1-middle", "sk-p-dl-a1-perverse", "sk-p-real-semi"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.FourierCorrection", "AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.nonempty_fourierCorrection", "AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.FourierCorrection.isLisse", "AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.FourierCorrection.hasWeightsAtMost"]
tags = ["sketch"]
+++
Let $\psi$ be nontrivial. For an irreducible lisse $M$ (nonzero, with no
lisse subsheaves other than $0$ and $M$) which is
nonexceptional and punctually $\iota$-pure of weight $w$, put
$B=j_*M/j_!M$. There are ordinary sheaves $G$ and $B'$ such that

$$
\begin{gathered}
\DLAFT_\psi(j_!M[1])\simeq G[1],\qquad
\DLAFT_\psi(B)\simeq B'[1],\\
0\longrightarrow B'\longrightarrow G\longrightarrow j'_*M'
\longrightarrow0.
\end{gathered}
$$

The correction $B'$ is lisse on the entire dual line, with weights at
most $w$.
