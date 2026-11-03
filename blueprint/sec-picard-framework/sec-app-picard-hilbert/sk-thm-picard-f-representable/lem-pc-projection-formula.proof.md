+++
kind  = "proof"
of    = "lem-pc-projection-formula"
+++
*The case $q=0$.* There is a canonical map
$f_*\mathcal{G}\otimes\mathcal{N}\to f_*(\mathcal{G}\otimes f^*\mathcal{N})$ for every
$\mathcal{O}_X$-module $\mathcal{G}$, natural in $\mathcal{G}$ (adjoint to
$f^*(f_*\mathcal{G}\otimes\mathcal{N})=f^*f_*\mathcal{G}\otimes f^*\mathcal{N}\to\mathcal{G}\otimes f^*\mathcal{N}$).
Whether it is an isomorphism is local on $Y$, and on an open $V\subseteq Y$
where $\mathcal{N}|_V\cong\mathcal{O}_V$ both sides become $f_*\mathcal{G}|_V$ and the
map the identity. So $f_*\circ(-\otimes f^*\mathcal{N})\cong(-\otimes\mathcal{N})\circ f_*$.

*The general case.* Since $\mathcal{N}$ is invertible, so is $f^*\mathcal{N}$, and
tensoring with an invertible module is an autoequivalence of the category of
modules (with inverse the tensor product with the dual). Hence
$-\otimes f^*\mathcal{N}$ is exact and sends injective $\mathcal{O}_X$-modules to
injective ones, so the right derived functors of
$f_*\circ(-\otimes f^*\mathcal{N})$ are $R^qf_*\circ(-\otimes f^*\mathcal{N})$
([def-pc-derived-direct-image]); and $-\otimes\mathcal{N}$ is exact, so the right
derived functors of $(-\otimes\mathcal{N})\circ f_*$ are
$(-\otimes\mathcal{N})\circ R^qf_*$. The isomorphism of functors of the case
$q=0$ therefore induces isomorphisms of their right derived functors, which
evaluated at $\mathcal{F}$ give the claim.
