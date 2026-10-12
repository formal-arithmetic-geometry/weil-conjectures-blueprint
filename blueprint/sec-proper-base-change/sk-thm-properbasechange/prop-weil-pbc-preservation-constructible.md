+++
id = "prop-weil-pbc-preservation-constructible"
kind = "theorem"
title = "Preservation before constructible restriction"
order = 1395
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-complete", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-cartesian-square", "def-weil-pbc-finite-level-amplification", "def-weil-pbc-scheme-conventions", "def-weil-pbc-tower-preservation", "def-weil-pbc-witness-compatibility", "lem-weil-pbc-reconstruction-uniform-tower", "prop-weil-pbc-direct-image-limits", "thm-weil-pbc-amplification-proper"]
tags = ["latex:proposition"]
+++
Let $\square$ be the cartesian square [def-weil-pbc-cartesian-square] with
$X,Y,X',Y'$ noetherian of finite dimension, $f$ and $f'$ proper, and suppose
there is a positive integer $N$ annihilating $A/I$ which is invertible on
all four schemes. Assume that the geometric fibers of $f$ have dimension at
most $e\in\mathbf Z_{\geq0}$; put $c=2e$.

Then, for every $K\in\Dbc(X_{\Proet},A)$ whose reductions have a common
cohomological interval $[a,b]$, one has
$$
 \begin{aligned}
  Rf_*K&\in\Dbc(Y_{\Proet},A),&
  Lg^*_{\mathrm{comp}}Rf_*K&\in\Dbc(Y'_{\Proet},A),\\
  Lg'^*_{\mathrm{comp}}K&\in\Dbc(X'_{\Proet},A),&
  Rf'_*Lg'^*_{\mathrm{comp}}K&\in\Dbc(Y'_{\Proet},A).
 \end{aligned}
$$
The two pullbacks have reduction amplitude $[a,b]$ and the two direct images
have reduction amplitude contained in $[a,b+c]$.
