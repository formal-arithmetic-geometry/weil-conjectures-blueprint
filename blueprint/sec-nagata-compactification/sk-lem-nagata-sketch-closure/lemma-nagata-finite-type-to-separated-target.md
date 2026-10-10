+++
id = "lemma-nagata-finite-type-to-separated-target"
kind = "lemma"
title = "Finite type over a separated target"
order = 78
lean = ["AlgebraicGeometry.locallyOfFiniteType_of_comp"]
+++
In a commutative triangle $T\to Y\to B$, if $T\to B$ is locally of
finite type, then $T\to Y$ is locally of finite type.

## Proof

Being locally of finite type is local on the source and on the target, so
it suffices to check it on affine opens. Let $t\in T$, let
$\operatorname{Spec}(A)\subseteq B$ be an affine open containing the image of
$t$, let $\operatorname{Spec}(R)\subseteq Y$ be an affine open containing the
image of $t$ and mapping into $\operatorname{Spec}(A)$, and let
$\operatorname{Spec}(C)\subseteq T$ be an affine open neighbourhood of $t$
mapping into $\operatorname{Spec}(R)$. Since $T\to B$ is locally of finite
type, $C$ is a finitely generated $A$-algebra (Stacks Project, Tag 01T2).
The structure map $A\to C$ factors as $A\to R\to C$, so any finite set of
$A$-algebra generators of $C$ also generates $C$ as an $R$-algebra. Hence
$C$ is a finitely generated $R$-algebra, and such affine opens
$\operatorname{Spec}(C)$ cover $T$. Thus $T\to Y$ is locally of finite type.
