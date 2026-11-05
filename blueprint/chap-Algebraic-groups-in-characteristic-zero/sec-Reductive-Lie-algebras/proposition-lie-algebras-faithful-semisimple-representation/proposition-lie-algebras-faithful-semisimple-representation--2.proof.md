+++
kind = "proof"
of = "proposition-lie-algebras-faithful-semisimple-representation--2"
order = 1740004
uses = ["lemma-killing"]
+++
Write $Q=\mathfrak l/Z(\mathfrak l)$ and let
$\pi\colon\mathfrak l\to Q$ be the quotient map. To show that $Q$
has zero radical, it suffices to show that it has no nonzero abelian
ideal. If $I$ is an abelian ideal of $Q$ and $J=\pi^{-1}(I)$, then
$[J,J]\subseteq Z(\mathfrak l)$, so $[[J,J],[J,J]]=0$. Thus $J$ is
solvable and

$$
J\subseteq\operatorname{rad}\mathfrak l=Z(\mathfrak l).
$$

Surjectivity of $\pi$ gives $I=0$. This proves
`LieAlgebra.hasTrivialRadical_quotient_center` over any field.

Now assume that $k$ has characteristic zero. The Killing form of $Q$
is nondegenerate, as in Lemma [lemma-killing]. Put $D=[Q,Q]$.
The Killing orthogonal $D^\perp$ is an ideal complementary to $D$
(`LieIdeal.isCompl_killingCompl`). For $z\in D^\perp$ and $x\in Q$,
the bracket $[x,z]$ lies in both $D$ and $D^\perp$, hence is zero.
Thus $D^\perp\subseteq Z(Q)\subseteq\operatorname{rad}Q=0$, and
$D=Q$.

The quotient map sends $[\mathfrak l,\mathfrak l]$ onto $[Q,Q]$.
Given $x\in\mathfrak l$, choose $y\in[\mathfrak l,\mathfrak l]$
with $\pi(y)=\pi(x)$. Then $x-y\in Z(\mathfrak l)$, giving the
required decomposition.
