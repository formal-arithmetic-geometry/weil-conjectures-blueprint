+++
id = "lem-pbc-m2-dense-open-base-change-boundary"
kind = "lemma"
title = "Finite closed separably closed boundary after extension of an algebraically closed field"
uses = ["def-pc-separably-closed", "def-weil-pbc-curve-setting", "def-sc-field-extension"]
lean = ["AlgebraicGeometry.IsCurve.dense_open_baseChange_boundary"]
order = 1779
+++
Let $k,k'$ be algebraically closed fields, $f:X\to\operatorname{Spec}k$ a curve [def-weil-pbc-curve-setting], and let $a:X'\to X$ be the top arrow of a cartesian field-extension square [def-sc-field-extension] with bottom arrow $\operatorname{Spec}k'\to\operatorname{Spec}k$. For every dense open $U\subseteq X$, put $V=a^{-1}(U)$. Then $X'\setminus V$ is finite, every $y\in X'\setminus V$ is a closed point, and its residue field $\kappa(y)$ is separably closed [def-pc-separably-closed]. There are no irreducibility, reducedness or nonemptiness assumptions.
