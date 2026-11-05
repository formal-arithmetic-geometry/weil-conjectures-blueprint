+++
id = "proposition-cohomology-smooth-affine-curve--1"
kind = "proposition"
title = "Cohomology of a smooth affine curve (1)"
name_showing = false
order = 1579001
aliases = ["bp-r493-1"]
lean = []
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-compactification-refinement"]
+++
This residue sequence is bypassed by the Lean proof, which uses the Kummer
sequence and a cardinality calculation.

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
