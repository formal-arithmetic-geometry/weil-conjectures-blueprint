+++
id = "theorem-comparison-over-henselian-pair-degree--1"
kind = "theorem"
title = "Henselian comparison for abelian sheaves and module sheaves"
name_showing = false
order = 328001
aliases = ["bp-r098-1"]
lean = ["AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_addCommGrpCat_of_henselianRing", "AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_of_henselianRing", "AlgebraicGeometry.Etale.globalSectionsUpperStarMap_naturality"]
uses = []
+++
Let $(R,J)$ be a henselian pair, let $Z\to\operatorname{Spec}R$ be
proper, and let $i:Z_0=Z\times_R\operatorname{Spec}(R/J)\hookrightarrow Z$.
For every abelian sheaf $F$ on $Z_{\acute{e}t}$, restriction is an isomorphism

$$
\Gamma(Z,F)\xrightarrow{\sim}\Gamma(Z_0,i^*F).
$$

The same holds for sheaves of $\Lambda$-modules, where $\Lambda$ is any
commutative ring; in that case the comparison is $\Lambda$-linear. No
torsion hypothesis is required.

Writing $r_F$ for restriction, the comparison is natural in $F$: for every
morphism $a:F\to F'$ of abelian sheaves, or of $\Lambda$-module sheaves,

$$
\Gamma(Z_0,i^*a)\circ r_F=r_{F'}\circ\Gamma(Z,a).
$$
