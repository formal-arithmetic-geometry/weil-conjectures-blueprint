+++
id = "lem-pc-ample-positive-degree"
kind = "lemma"
title = "Positive degree is equivalent to ampleness"
lean = ["AlgebraicGeometry.Scheme.isAmple_iff_degree_pos", "AlgebraicGeometry.Scheme.isAmple_of_degree_pos"]
order = 750
uses = ["def-pc-base-change", "def-pc-dimension", "def-pc-zero-scheme", "def-sc-ample", "def-nagata-invertible-ideal", "lem-pc-degree-base-change", "lem-pc-dim-base-change", "lem-pc-genus-base-change", "lem-pc-proper-base-change", "lem-pc-very-ample-descends", "lem-pc-flat-base-change-cohom", "lem-sc-positive-degree-ample", "lem-sc-smooth-regular", "lem-sc-regular-dim1-dvr", "lem-sc-point-cartier"]
+++
Let $k$ be a field, $X$ a scheme which is smooth of relative
dimension $1$ and proper over $k$ with $H^0(X,\mathcal{O}_X)=k$, and
$\mathcal{L}$ an invertible $\mathcal{O}_X$-module. Then $\mathcal{L}$ is ample if and
only if $\deg(\mathcal{L})>0$.
