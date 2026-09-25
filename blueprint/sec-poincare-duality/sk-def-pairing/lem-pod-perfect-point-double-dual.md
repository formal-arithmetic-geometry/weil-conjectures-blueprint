+++
id = "lem-pod-perfect-point-double-dual"
kind = "lemma"
title = "Double dual of a perfect point complex"
order = 2588
uses = ["def-pod-conventions", "def-pod-perfect-point-complex"]
+++
In the Poincare duality conventions of
this chapter, let $C$ be a
perfect point complex over the
coefficient ring $\Lambda\in\{A,\mathcal O_E,E,\Qlb\}$, with derived
dual $C^\vee=R\operatorname{Hom}_\Lambda(C,\Lambda)$. Then the
canonical map $C\to C^{\vee\vee}$ of the tensor–internal-Hom
adjunction is an isomorphism.

## Proof

By [def-pod-perfect-point-complex] the object $C$ is
quasi-isomorphic to a bounded complex $P^\bullet$ of finite projective
$\Lambda$-modules, so it may be replaced by $P^\bullet$. For a
finite projective $\Lambda$-module $P$ the canonical map
$P\to P^{\vee\vee}$ is an isomorphism: for $P=\Lambda^r$ it is the
identity, and it is inherited by direct summands, because the duality
functor is additive and carries a retraction of $\Lambda^r$ onto $P$
to a retraction of $P^\vee$ onto $\Lambda^{r\vee}$. The terms
$P^i$ are flat, so
$R\operatorname{Hom}_\Lambda(P^\bullet,\Lambda)$ is computed termwise
and $P^{\bullet\vee\vee}\cong P^\bullet$; the canonical map
$P^\bullet\to P^{\bullet\vee\vee}$ is therefore an isomorphism, and
with it the canonical map $C\to C^{\vee\vee}$.
