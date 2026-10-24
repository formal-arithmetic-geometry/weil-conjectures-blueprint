+++
id = "def-per-support-condition"
kind = "definition"
title = "Support and cosupport conditions"
order = 3968
uses = ["def-trf-dualizing-complex", "def-weil-derived-cohomology-sheaves", "det-def-sfb-bounded-constructible", "sk-lem-coefficient-heart", "def-weil-pbc-scheme-conventions"]
+++
Let $X$ be a
separated scheme of finite
type over a field $k$, and work in
$D^b_c(X,\overline{\mathbf Q}_\ell)\subset D(X_{\mathrm{proét}},\overline{\mathbf Q}_\ell)$,
the bounded complexes of $\overline{\mathbf Q}_{\ell,X}$-modules with constructible
cohomology sheaves ([det-def-sfb-bounded-constructible]), with the cohomology sheaves
$\mathcal H^i$ of [def-weil-derived-cohomology-sheaves]. Each $\mathcal H^i(K)$ lies in
$\Cons(X,\Qlb)$, so it is lisse on the strata of a finite stratification
([sk-lem-coefficient-heart]) and its support (the closure of the set of points with nonzero
geometric stalk) is a closed subset of $X$. For
$K\in D^b_c(X,\overline{\mathbf Q}_\ell)$ write

$$
\operatorname{SuppCon}(K)\quad\Longleftrightarrow\quad
\dim\operatorname{Supp}\mathcal H^{-i}(K)\le i\qquad(i\in\mathbf Z),
$$

with the convention that the empty support has dimension $-\infty$, and

$$
\operatorname{CosuppCon}(K)\quad\Longleftrightarrow\quad
\operatorname{SuppCon}\bigl(D_XK\bigr),
$$

where $D_X$ is the Verdier dual of [def-trf-dualizing-complex].
