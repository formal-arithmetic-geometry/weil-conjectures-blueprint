+++
id = "proposition-cohomology-smooth-affine-curve--1"
kind = "proposition"
title = "Cohomology of a smooth affine curve (1)"
name_showing = false
order = 1584001
aliases = ["bp-r493-1"]
lean = ["AlgebraicGeometry.Scheme.residueSequence_exact", "AlgebraicGeometry.Scheme.gysinH2_eq_zero_iff"]
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--1", "proposition-comparison-morphism-inverse-image--1", "definition-compactification-refinement--1", "definition-relative-picard-functor--2", "lemma-cohomology-multiplicative-group--3", "lemma-cohomology-multiplicative-group--5"]
+++
Let $\overline C$ be a smooth proper connected curve of genus $g$
over an algebraically closed field $k$.  Let
$U=\overline C\setminus D$, where $D$ is a finite nonempty set of
closed points, and let $n$ be invertible in $k$.  There is a natural exact sequence

$$
0\longrightarrow H^1(\overline C,\mu_n)
\longrightarrow H^1(U,\mu_n)
\xrightarrow{\partial}(\mathbf Z/n)^D
\xrightarrow{\sum}\mathbf Z/n\longrightarrow0.
\tag{D.1}
$$
