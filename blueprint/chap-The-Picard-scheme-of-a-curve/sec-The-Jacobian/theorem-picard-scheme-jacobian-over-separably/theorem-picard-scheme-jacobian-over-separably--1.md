+++
id = "theorem-picard-scheme-jacobian-over-separably--1"
kind = "theorem"
title = "Representability, smoothness and degree decomposition"
order = 1552001
aliases = ["bp-r483-1"]
lean = ["AlgebraicGeometry.GrpObj.isSeparated_hom", "AlgebraicGeometry.exists_decomposition_picardFunctor_representableBy", "AlgebraicGeometry.isRepresentable_picardFunctor", "AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_picardFunctor"]
+++
Let $k$ be separably closed and let $C/k$ be a smooth proper
geometrically integral curve of genus $g$. The fppf Picard functor
is represented by a group scheme $\mathbf{Pic}_{C/k}$ whose group law
is induced by tensor product of invertible sheaves. Every representing
scheme is smooth of dimension $g$, in particular locally of finite type
over $k$, and the group scheme $\mathbf{Pic}_{C/k}$ is separated.

The degree $\delta:\mathbf{Pic}_{C/k}\to\mathbf Z$ of the universal
Picard class is locally constant. Its fibres give a decomposition

$$
\mathbf{Pic}_{C/k}=\coprod_{d\in\mathbf Z}\mathbf{Pic}^d_{C/k}
$$

into pairwise disjoint open and closed subschemes. Here
$\mathbf{Pic}^d_{C/k}$ represents $\operatorname{Pic}^d_{C/k}$, the fppf
sheafification of the subfunctor of invertible sheaves whose degree on
every fibre is $d$. The representations are compatible with the
inclusions $\mathbf{Pic}^d_{C/k}\hookrightarrow\mathbf{Pic}_{C/k}$: a
class of fibrewise degree $d$ determines the same point of
$\mathbf{Pic}_{C/k}$ through either representation.
