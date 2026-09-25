+++
id = "sk-prop-av-symmetric-ample"
kind = "section"
title = "A symmetric ample module"
order = 480
uses = ["sk-def-av", "sk-def-av-ample-degree", "sk-prop-av-projective"]
+++
*Proposition (sketch).*

Let $A$ be an abelian variety over $k$ and let $\cL$ be an ample
invertible $\cO_A$-module. Then

$$
\cN:=\cL\otimes[-1]^*\cL
$$

is ample and *symmetric*: $[-1]^*\cN\cong\cN$.

## Proof

Choose $a,b\ge1$ with $\cL^{\otimes a}$, $\cL^{\otimes b}$ very ample;
then $(\cL\otimes\cL)^{\otimes ab}$ is very ample, being the pullback
of $\cO(1)\boxtimes\cO(1)$ along the Segre embedding, so
$\cL\otimes\cL$ is ample. As $[-1]$ is an automorphism of $A$,
$[-1]^*\cL$ is ample; and $[-1]^*[-1]^*\cL\cong\cL$, whence
$[-1]^*\cN\cong[-1]^*\cL\otimes\cL\cong\cN$.

Uses: [sk-def-av-ample-degree], [sk-def-av], [sk-prop-av-projective]
