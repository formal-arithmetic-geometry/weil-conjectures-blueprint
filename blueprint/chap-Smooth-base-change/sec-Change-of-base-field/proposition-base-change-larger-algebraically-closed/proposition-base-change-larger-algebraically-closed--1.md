+++
id = "proposition-base-change-larger-algebraically-closed--1"
kind = "proposition"
title = "Killing degree-one classes on an étale covering"
name_showing = false
order = 687001
aliases = ["bp-r207-1"]
lean = ["AlgebraicGeometry.Etale.CurveTestDatum.exists_cover_cohomologyMap_eq_zero"]
uses = ["lemma-reduction-curve-over-normal-base"]
+++
Let $S=\operatorname{Spec}R$ for a normal domain $R$ with algebraically
closed fraction field $L$, and let $a:C\to S$ be affine and smooth
of relative dimension one. Let $\Omega/L$ be an extension of algebraically
closed fields, let $m$ be a positive integer invertible on $S$, and let
$h:C_\Omega\to C$ be the projection. For every positive divisor $e\mid m$,
every affine scheme $U$ with an étale map $u:U\to C$, and every class

$$
\xi\in H^1(C_\Omega\times_C U,\mathbf Z/e),
$$

there is a jointly surjective family of étale maps $v_i:V_i\to U$ such
that the pullback of $\xi$ to $C_\Omega\times_C V_i$ is zero for every
$i$. All cohomology in this statement is taken on the small étale site.
