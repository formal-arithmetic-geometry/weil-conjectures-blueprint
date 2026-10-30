+++
id = "det-pd-dual-stratum-extension"
kind = "lemma"
title = "Verdier dual of an extension by zero from a smooth stratum"
order = 3425
uses = ["cor-pur-dualizing-object-purity", "det-pd-dualizing-complex-ctf", "det-sf-flat-model-generation", "det-thm-sf-ctf-stability-direct-images", "lem-pod-coefficient-dual-perfect", "lem-sf-tensor-hom"]
+++
Let $\Lambda=A$ be a finite admissible coefficient ring and let $X$ be
separated of finite type over $k$.

**(1)** Let $t\colon T\hookrightarrow X$ be a locally closed immersion with $T$
smooth of pure dimension $r$, and let $P$ be a locally constant perfect
complex of $A_T$-modules, with dual $P^\vee=\cHom_{A_T}(P,A_T)$. Then there
are isomorphisms

$$
\mathbb D_X(t_!P)\simeq Rt_*\mathbb D_TP\simeq Rt_*\bigl(P^\vee(r)[2r]\bigr),
$$

and $\mathbb D_X(t_!P)$ lies in $\Dctf(X,A)$.

**(2)** Every $K\in\Dctf(X,A)$ is obtained by finitely many shifts and cones
from objects $t_!P$ as in (1). Consequently $\mathbb D_XK\in\Dctf(X,A)$.
