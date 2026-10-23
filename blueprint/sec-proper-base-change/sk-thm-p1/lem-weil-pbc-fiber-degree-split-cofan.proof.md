+++
kind = "proof"
of = "lem-weil-pbc-fiber-degree-split-cofan"
uses = ["def-pc-finite-locally-free"]
+++
Put $K=\kappa(x)$ and let $q:\operatorname{Spec}K\to U$ be the canonical morphism. Each $p\circ i_j$ is an isomorphism, so with $s_j=(p\circ i_j)^{-1}\circ q:\operatorname{Spec}K\to D_j$ the square formed by $s_j$, $\mathrm{id}_{\operatorname{Spec}K}$, $p\circ i_j$ and $q$ is cartesian: the fibre of $D_j$ over $x$ is $\operatorname{Spec}K$. By the universal property of $Z_x=Z\times_U\operatorname{Spec}K$, the morphisms $i_j\circ s_j$ and $\mathrm{id}_{\operatorname{Spec}K}$ define $a_j:\operatorname{Spec}K\to Z_x$, whose composite with the fibre projection $Z_x\to\operatorname{Spec}K$ is the identity.

Finite coproducts of schemes are universal, i.e. stable under base change. Base-changing the coproduct decomposition $Z=\coprod_jD_j$ along $q$ and using the cartesian squares of the first step shows that the $a_j$ exhibit $Z_x$ as the coproduct $\coprod_{j\in J}\operatorname{Spec}K$.

A finite coproduct of copies of $\operatorname{Spec}K$ is $\operatorname{Spec}(\prod_{j\in J}K)$. Under the resulting isomorphism $Z_x\cong\operatorname{Spec}(\prod_JK)$ the fibre projection corresponds to $\operatorname{Spec}$ of the diagonal map $K\to\prod_JK$, as one checks on each summand, where both maps are the identity. Hence $\Gamma(Z_x,\mathcal O_{Z_x})\cong\prod_JK$ as $K$-algebras, and this finite product has $K$-dimension $|J|$. For $J$ empty it is the zero algebra, of dimension zero. ([def-pc-finite-locally-free]).
