+++
id = "theorem-gabber-affine-proper-base-change--1"
kind = "remark"
title = "Effacement over a henselian pair"
order = 355001
lean = ["AlgebraicGeometry.Etale.exists_mono_map_eq_zero_of_henselianRing"]
uses = ["definition-torsion-sheaves"]
aliases = ["bp-r108-1"]
+++
Let $(B,J)$ be a henselian pair, put $X=\operatorname{Spec}B$ and
$X_0=\operatorname{Spec}(B/J)$, and let $i:X_0\hookrightarrow X$.
Let $\Lambda$ be a commutative ring and let $F$ be a torsion sheaf of
$\Lambda$-modules on $X_{\acute{e}t}$. For every $q>0$ and every class
$c\in H^q(X_0,i^*F)$, there is a monomorphism $a:F\hookrightarrow F'$
into a torsion sheaf of $\Lambda$-modules such that

$$
H^q(i^*a)(c)=0.
$$

Here cohomology is taken on the underlying abelian sheaves.

*Proof.* By [definition-torsion-sheaves--3], $F$ is a filtered colimit of sheaves
killed by positive integers. Inverse image and passage to underlying
abelian sheaves preserve these colimits. Since $X_0$ is affine,
continuity of étale cohomology
[lemma-finiteness-small-etale-topoi--2] gives a sheaf $C$, a map
$b:C\to F$, an integer $n>0$ with $nC=0$, and a class
$z\in H^q(X_0,i^*C)$ mapping to $c$.

For abelian sheaves killed by $n$, henselian restriction is surjective
in every degree. This is proved separately with $\Z/n$ coefficients:
represent a class by a constructible sheaf, embed that sheaf in a finite
sum of finite pushforwards of finite constant sheaves, and kill the
resulting classes by finite surjective covers. Finite base change
[lemma-finite-morphisms] and pushouts give effacement within
$\Z/n$-module sheaves. Starting with
[theorem-comparison-over-henselian-pair-degree], induction on the long
exact cohomology sequences gives comparison for these coefficients.
In particular, $z$ lifts to a class $x\in H^q(X,C)$.

Embed $C$ in an injective sheaf $I$ of $\Lambda$-modules and put
$E=\ker(n:I\to I)$. Since $nC=0$, the embedding factors through a
monomorphism $C\hookrightarrow E$. The sheaf $E$ is killed by $n$.
Viewed as a sheaf of $\Lambda/(n)$-modules, it is injective: taking this
kernel is right adjoint to the exact restriction of scalars from
$\Lambda/(n)$ to $\Lambda$. Thus its underlying abelian sheaf is
acyclic by [lemma-cohomology-modules-underlying-abelian]. The image of
$x$ in $H^q(X,E)$ is zero, so naturality of restriction shows that the
image of $z$ in $H^q(X_0,i^*E)$ is zero.

Form the pushout $F'=E\amalg_C F$. The map $F\to F'$ is a monomorphism,
and $F'$ is torsion, being a quotient of $E\oplus F$. The pushout
identity shows that the image of $c$ in $H^q(X_0,i^*F')$ is zero.
