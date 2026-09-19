+++
id = "def-cohomology-weil-structure"
kind = "definition"
title = "Frobenius on a cohomology sheaf"
order = 78
uses = ["def-constructible-heart", "def-constructible-truncation-functors", "def-derived-weil-object", "def-weil-finite-coefficient-datum", "prop-constructible-t-structure"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, let $Y_0$ be of finite type
over $k_0$ with geometric fiber $Y$, and let
$\Lambda\in\{E,\Qlb\}$. For a derived Weil object
$(K,\theta_K)$ with $K\in D^b_c(Y,\Lambda)$, and every
$i\in\mathbf Z$,
define the Frobenius isomorphism
on its $i$-th cohomology sheaf by the composite in the constructible heart

$$
\theta_{\mathcal H^iK}:
Lg_Y^*\mathcal H^i(K)
\xrightarrow{c_i(K)}\mathcal H^i(Lg_Y^*K)
\xrightarrow{\mathcal H^i(\theta_K)}\mathcal H^i(K).
$$

Thus $\mathcal H^i(K)\in\Sh_c(Y,\Lambda)$ carries a specified
object-level Frobenius structure without passing to a derived category of
Frobenius sheaves.
