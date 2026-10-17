+++
kind  = "proof"
of    = "cor-trf-point-counting"
+++
Apply [det-thm-tf-uniform-formula-weil] to the Weil sheaf
$K=\Lambda_X$, $\Lambda\in\{E,\Qlb\}$, with its canonical Weil structure.
For every $y\in X_0(\mathbf F_{q^m})$ the stalk $K_{\bar y}$ is $\Lambda$ in
degree zero, and the local operator $F_{y,m}$ is its identity: the iterated
structure is the composite of the canonical identifications of inverse
images of $\Lambda_X$, which are the identity on the constant stalk. This is
the unit stalk trace of [cor-trf-constant-stalk-trace], read over the field
$\Lambda$. Hence

$$
\sum_{j}(-1)^j\operatorname{Tr}\bigl(F_{y,m}\mid H^j(K_{\bar y})\bigr)=1
$$

for every rational point $y$, and the right-hand side of the identity (2)
of [det-thm-tf-uniform-formula-weil] is the cardinality of
$X_0(\mathbf F_{q^m})$, which is finite because $X_0$ is of finite type.
This is the first identity; the second is the identification
$H_c^i\simeq H^i$ for proper $X_0$ of
[def-weil-ordinary-compact-cohomology].
