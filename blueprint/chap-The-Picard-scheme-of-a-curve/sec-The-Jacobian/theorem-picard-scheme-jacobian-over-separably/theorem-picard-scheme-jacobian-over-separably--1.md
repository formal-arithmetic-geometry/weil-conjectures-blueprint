+++
id = "theorem-picard-scheme-jacobian-over-separably--1"
kind = "theorem"
title = "Representability, smoothness and degree decomposition"
name_showing = false
order = 1549001
aliases = ["bp-r483-1"]
lean = ["AlgebraicGeometry.isRepresentable_picardFunctor", "AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_picardFunctor", "AlgebraicGeometry.GrpObj.isSeparated_hom", "AlgebraicGeometry.exists_decomposition_picardFunctor_representableBy"]
uses = ["definition-relative-picard-functor"]
+++
Let $k$ be separably closed and let $C/k$ be a smooth proper
geometrically integral curve of genus $g$. The fppf Picard functor
is represented by a group scheme $P$ whose group law is induced by
tensor product of invertible sheaves. Every representing scheme is
smooth of dimension $g$, and the group scheme $P$ is separated;
in particular, it is locally of finite type over $k$.

The degree $\delta:P\to\mathbf Z$ of the universal Picard class is
locally constant. Its fibres give a decomposition

$$
P=\coprod_{d\in\mathbf Z}P^d
$$

into pairwise disjoint open and closed subschemes. Here $P^d$
represents $\operatorname{Pic}^d_{C/k}$, the fppf sheafification of
the subfunctor of invertible sheaves whose degree on every fibre is
$d$. The representations are compatible with the inclusions
$P^d\hookrightarrow P$: a class of fibrewise degree $d$ determines
the same point of $P$ through either representation.
