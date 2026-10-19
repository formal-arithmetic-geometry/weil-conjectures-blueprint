+++
id = "thm-pod-global-verdier-duality"
kind = "theorem"
title = "Global Verdier duality at the point"
order = 2592
uses = ["def-pod-conventions", "def-weil-finite-coefficient-point", "def-weil-ordinary-compact-cohomology", "def-weil-site-perfect-complex", "fix-cor-verdier-exchange", "lem-fix-operation-reduction", "lem-pod-point-dualizing-complex", "thm-pur-finite-reduction-of-purity", "thm-sf-global-duality"]
+++
Use the Poincare duality conventions of [def-pod-conventions] (so $X_0$
is smooth, separated of finite type and geometrically connected of pure
dimension $d$, not necessarily proper). The statement below also
holds verbatim for a smooth, proper, geometrically connected $k$-scheme
$X$ of pure dimension $d$ not assumed to descend to $k_0$ (see
[thm-sf-global-duality]). Let $K\in D^b_{ctf}(X,\Lambda)$. For the admissible structure
morphism $a_X:X\to s$ there is a canonical isomorphism

$$
R\Gamma_c(X,K)^\vee\xrightarrow{\sim}R\Gamma(X,\mathbb D_XK),
$$

with the cohomology functors
of the fixed coefficient ring. It is natural in $K$ and compatible
with shifts. For a site-perfect
$K$, it is also compatible with finite coefficient reduction and
scalar extension under the smooth orientation and its coefficient
comparisons. At $K=\Lambda_X$ it identifies
$R\Gamma_c(X,\Lambda_X)^\vee$ with $R\Gamma(X,\omega_{X,\Lambda})$.
