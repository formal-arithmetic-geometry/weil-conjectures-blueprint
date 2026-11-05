+++
id = "theorem-picard-scheme-jacobian-over-separably--5"
kind = "theorem"
title = "Compatibility with base change"
name_showing = false
order = 1549005
aliases = ["bp-r483-5"]
lean = ["AlgebraicGeometry.nonempty_picardFunctor_iso_of_isPullback", "AlgebraicGeometry.picardFunctorDegreeIsoOfIsPullback"]
uses = ["definition-relative-picard-functor", "theorem-picard-scheme-jacobian-over-separably--1", "theorem-picard-scheme-jacobian-over-separably--3"]
+++
For a morphism $X\to S$ and a base change $S'\to S$, put
$X'=X\times_S S'$. Restricting $\operatorname{Pic}_{X/S}$ to schemes
over $S'$ gives a functor naturally isomorphic to
$\operatorname{Pic}_{X'/S'}$.

Let $k$ be any field, let $C/k$ be proper and locally of finite
presentation, and let $K/k$ be a field extension. For every
$d\in\mathbf Z$, the same identification restricts to the degree
parts:

$$
\left.\operatorname{Pic}^d_{C/k}\right|_{K\text{-schemes}}
\simeq\operatorname{Pic}^d_{C_K/K}.
$$

Consequently, whenever these functors are represented, their
representing schemes commute with extension of the ground field.
This applies to the Picard scheme and its degree components in
[theorem-picard-scheme-jacobian-over-separably--1], and, for $d=0$,
to the Jacobian in [theorem-picard-scheme-jacobian-over-separably--3].
