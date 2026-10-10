+++
id = "def-sc-genus"
kind = "definition"
title = "The genus of a curve"
lean = ["AlgebraicGeometry.Scheme.Hom.genus"]
order = 419
uses = ["def-sc-curves"]
+++
Let $C$ be a proper smooth connected curve over
a field $k$. The *genus* of $C$ is

$$
g(C):=\dim_kH^0(C,\Omega^1_{C/k}),
$$

the $k$-dimension of the space of global sections of the sheaf of
relative differentials. Equivalently, by Serre duality,
$g(C)=\dim_kH^1(C,\mathcal O_C)$.

For a smooth separated, not necessarily proper, connected curve $C$ the
genus of $C$ is the genus of a compactification $\overline C$ of $C$, i.e.
of a proper smooth connected curve containing $C$ as an open subscheme
with finite complement.

## Proof

The genus is finite because coherent cohomology of a proper scheme over a
field is finite-dimensional: coherent higher direct images under a proper
morphism are coherent (Stacks Project, Cohomology of Schemes, Proposition
30.19.1, [Tag 02O5](https://stacks.math.columbia.edu/tag/02O5)). The
equality $\dim_kH^0(C,\Omega^1_{C/k})=\dim_kH^1(C,\mathcal O_C)$ is
duality on the proper smooth curve $C$ (Stacks Project, Algebraic Curves,
Lemma 53.4.1, [Tag 0BS2](https://stacks.math.columbia.edu/tag/0BS2),
parts (5) and (6)).
