+++
id = "def-sc-effective-cartier-divisor"
kind = "definition"
title = "Effective Cartier divisors"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.isInvertible_toModules", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.isFinite_subscheme\u03b9_comp"]
order = 713
uses = ["def-sc-curves"]
+++
Let $C$ be a curve. An *effective Cartier divisor* on $C$ is a closed
subscheme $D\subseteq C$ which is locally defined by a single
non-zero-divisor: every point of $D$ has an open neighbourhood
$U$ and a non-zero-divisor $f\in\mathcal O_C(U)$ with
$D\cap U=V(f)$.
