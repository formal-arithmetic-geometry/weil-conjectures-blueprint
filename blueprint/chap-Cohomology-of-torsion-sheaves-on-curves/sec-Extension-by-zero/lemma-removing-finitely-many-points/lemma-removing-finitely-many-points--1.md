+++
id = "lemma-removing-finitely-many-points--1"
kind = "lemma"
title = "Dense-open cohomology comparisons"
name_showing = false
order = 1605001
aliases = ["bp-r500-1"]
lean = ["AlgebraicGeometry.IsCurve.dense_open_high_cohomology", "AlgebraicGeometry.IsCurve.dense_open_primary_finiteness", "AlgebraicGeometry.IsCurve.dense_open_base_change"]
uses = ["theorem-cohomology-curves"]
+++
Let $k$ be algebraically closed, let $C$ be a separated scheme of finite
type over $k$ with $\dim C\leq1$, and let $j:U\hookrightarrow C$ be a
dense open. Let $\Lambda$ be a commutative ring, let $F$ be a sheaf of
$\Lambda$-modules on $C_{\acute{e}t}$, and put $G=j_!j^*F$. Cohomology
is taken on the small étale site with the underlying abelian sheaf.

1. The counit $\varepsilon:G\to F$ induces isomorphisms
   $$
   H^q(C,G)\xrightarrow{\sim}H^q(C,F)\qquad(q>1).
   $$
   For every open immersion $a:W\hookrightarrow C$, the map induced
   by $a^*\varepsilon$ is also an isomorphism
   $$
   H^2(W,a^*G)\xrightarrow{\sim}H^2(W,a^*F).
   $$
2. Suppose in addition that $C$ is reduced, $\Lambda$ is finite,
   $F$ is constructible, and $\ell F=0$ for a prime $\ell$.
   Interpret the assertions of [theorem-cohomology-curves] on the small
   étale site. Each of the conditional assertions $(C_3)$, $(C_4)$
   and $(C_5)$ holds for $F$ if and only if it holds for $G$.
3. Under the hypotheses of (2), each of the conditional assertions
   $(C_6)$ and $(C_7)$ holds for $F$ if and only if it holds for $G$.
