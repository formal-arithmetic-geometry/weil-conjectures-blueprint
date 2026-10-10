+++
id = "lem-sc-support-dimension-union"
kind = "lemma"
title = "A sheaf supported in low dimension is a filtered union"
order = 1550
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $B$ be a finite-type
scheme over a field $K$. Suppose a torsion
etale sheaf $N$ has zero
geometric stalk at every point $y$ with
$\operatorname{trdeg}_K\kappa(y)>a$, where $a\geq0$.
For each closed $Z\subset B$ of dimension at most $a$, let
$j_Z:B\setminus Z\to B$ and set
$N_Z=\ker(N\to j_{Z*}j_Z^*N)$.
Then the canonical map $\varinjlim_Z N_Z\to N$ is an isomorphism.
