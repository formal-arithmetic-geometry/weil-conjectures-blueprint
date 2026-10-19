+++
id = "def-weil-pbc-finite-torsors"
kind = "definition"
title = "Finite torsors"
order = 588
lean = ["CategoryTheory.Sheaf.Torsor", "CategoryTheory.Sheaf.Torsor.Iso", "CategoryTheory.Sheaf.Torsor.setoid", "CategoryTheory.Sheaf.Torsor.trivial", "AlgebraicGeometry.Scheme.EtaleTorsor.isFiniteLocallyConstantSheafOfTypes_sheaf"]
uses = ["def-weil-pbc-etale-sheaves"]
+++
Let $M$ be a finite abelian group and let $\underline M$ be the constant
sheaf on $Y_{\Et}$. Following Cohomology on Sites, Definition 21.4.1
(Tag [03AH](https://stacks.math.columbia.edu/tag/03AH)), an $M$-torsor on
$Y_{\Et}$ is a sheaf of sets $P$ on $Y_{\Et}$ with an action
$\underline M\times P\to P$ such that

1. for every $U$ in $Y_{\Et}$ with $P(U)\neq\emptyset$, the action of
   $\underline M(U)$ on $P(U)$ is simply transitive (free and transitive);
1. for every $U$ in $Y_{\Et}$ there is a covering $\{U_i\to U\}$ with
   $P(U_i)\neq\emptyset$ for all $i$.

Condition (1) says that $\underline M\times P\to P\times_YP$,
$(m,p)\mapsto(m+p,p)$, is an isomorphism; a sheaf with an $M$-action
satisfying (1) alone is a pseudo-torsor in the sense of loc. cit., and the
empty sheaf is one, so (2) is not implied by (1). Together, (1) and (2) say
that $P$ is locally for the etale topology isomorphic to $\underline M$ with
its translation action; in particular an $M$-torsor is a finite locally
constant sheaf of sets. Morphisms of $M$-torsors are the $M$-equivariant
morphisms of sheaves. Write

$$
 \operatorname{Tor}^1(Y,M)
$$

for the pointed set of isomorphism classes of $M$-torsors on $Y_{\Et}$,
pointed by the trivial torsor $\underline M$.
