+++
id = "def-local-frobenius-trace"
kind = "definition"
title = "Local Frobenius and local alternating trace"
order = 95
uses = ["def-cohomology-weil-structure", "def-derived-weil-object", "def-weil-base-field", "def-weil-finite-coefficient-datum", "def-weil-frobenius"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum]. Let $Y_0/\Fq$ be
of finite type, let $Y=Y_0\times_{\Fq}k$, let
$\Lambda\in\{E,\Qlb\}$, and let $(K,\theta_K)$ be a derived Weil
object in $D^b_c(Y,\Lambda)$. Let $y\in|Y_0|$ be a closed point of degree
$r=[\kappa(y):\Fq]$. Choose an embedding
$\kappa(y)\hookrightarrow k$ and the associated geometric point
$\bar y\to Y$. Compose the Weil isomorphism with its Frobenius pullbacks
$r$ times. The resulting return map at $\bar y$ defines the geometric
Frobenius operator
$F_y$ on every stalk
$\mathcal H^j(K)_{\bar y}$, for $j\in\mathbf Z$; its conjugacy class is
independent of the chosen embedding.

More generally, for every $n\geq1$ and
$x\in Y_0(\mathbf F_{q^n})$, the $n$-fold iterate
at the associated geometric point defines $F_x^{(n)}$. Put

$$
\Tr(F_x^{(n)}\mid K_{\bar x})=
\sum_{j\in\mathbf Z}(-1)^j
\Tr\bigl(F_x^{(n)}\mid
\mathcal H^j(K)_{\bar x}\bigr).
$$
