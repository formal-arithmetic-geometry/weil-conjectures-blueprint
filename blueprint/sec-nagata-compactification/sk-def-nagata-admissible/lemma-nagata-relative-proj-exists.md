+++
id = "lemma-nagata-relative-proj-exists"
kind = "lemma"
title = "Existence and affine compatibility of relative Proj"
lean = ["AlgebraicGeometry.Scheme.GradedAlgebraData.existsUnique_relProjIso", "AlgebraicGeometry.Scheme.GradedAlgebraData.isColimitRestrict", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProj\u03b9_relProjHom", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjHom_preimage", "AlgebraicGeometry.Scheme.GradedAlgebraData.isPullback_relProj\u03b9", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjFunctor_map_relProj\u03b9", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjRestrictIso", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjRestrictIso_hom_naturality"]
order = 156
uses = ["def-nagata-affine-proj", "def-nagata-relative-proj", "lemma-nagata-proj-chart-ring-cocycle"]
+++
Let $\mathcal A$ be a quasi-coherent graded $\mathcal O_X$-algebra. The
relative Proj $\pi\colon\operatorname{Proj}_X(\mathcal A)\to X$ of
[def-nagata-relative-proj] exists, and:

1. for every affine open $V\subseteq X$, the chart $\iota_V$ is an open
   immersion, $\pi\circ\iota_V$ is the structure morphism
   $\operatorname{Proj}(\mathcal A(V))\to V$ followed by $V\subseteq X$,
   and $\pi^{-1}(V)$ is the image of $\iota_V$;
1. the square formed by $\iota_V$, $\pi$, the structure morphism
   $\operatorname{Proj}(\mathcal A(V))\to V$ and $V\subseteq X$ is
   cartesian, giving a restriction isomorphism
   $\operatorname{Proj}(\mathcal A(V))\cong V\times_X\operatorname{Proj}_X(\mathcal A)$;
1. for affine opens $U\subseteq V$, $\iota_U$ is the transition morphism
   $\operatorname{Proj}(\mathcal A(U))\to\operatorname{Proj}(\mathcal A(V))$
   followed by $\iota_V$, and under the restriction isomorphisms this
   transition morphism is the inclusion
   $U\times_X\operatorname{Proj}_X(\mathcal A)\to V\times_X\operatorname{Proj}_X(\mathcal A)$;
1. (uniqueness) if $p\colon P\to X$ is a scheme over $X$ with morphisms
   $j_V\colon\operatorname{Proj}(\mathcal A(V))\to P$ for all affine opens
   $V$, such that each $j_V$ exhibits $\operatorname{Proj}(\mathcal A(V))$ as
   $V\times_XP$ over the structure morphism and such that $j_U$ is the
   transition morphism followed by $j_V$ for $U\subseteq V$, then there is a
   unique isomorphism $e\colon\operatorname{Proj}_X(\mathcal A)\to P$ with
   $e\circ\iota_V=j_V$ for all $V$, and $p\circ e=\pi$;
1. (independence of the cover) if $(V_i)_{i\in I}$ is a family of affine
   opens indexed by a preordered set, monotone in $i$, covering $X$, and such
   that for all $i,i'$ and $x\in V_i\cap V_{i'}$ there is $k\le i,i'$ with
   $x\in V_k$, then $\operatorname{Proj}_X(\mathcal A)$ with the charts
   $\iota_{V_i}$ is also the colimit of the diagram
   $i\mapsto\operatorname{Proj}(\mathcal A(V_i))$.
