+++
kind = "proof"
of = "det-ind-heart-filtered-colimits"
+++
Let $\mathcal K$ be the category of pairs $(\lambda,c\colon C\to B_\lambda)$ with $C$ constructible; a
morphism $(\lambda,c)\to(\mu,c')$ is an arrow $\lambda\to\mu$ in $I$ and a map $C\to C'$ with
$c'\circ(C\to C')=(B_\lambda\to B_\mu)\circ c$.

*$\mathcal K$ is filtered.* Given finitely many objects and arrows, first move all indices to a common
upper bound $\mu\in I$ (possible since $I$ is filtered), composing the maps $c$ with the transition maps
into $B_\mu$; then the finitely many objects lie in $J(B_\mu)$, which is filtered
([det-ind-heart-canonical-presentation]), so they admit a cocone there (direct sums and cokernels in
$\Cons(X,\Lambda)$). If two parallel arrows in $\mathcal K$ differ in the $I$-component, equalize those
first in $I$.

*Colimit.* Computing the colimit of $(\lambda,c)\mapsto C$ first over $c$ for fixed $\lambda$ and then
over $\lambda$ gives

$$
\varinjlim_{\mathcal K}C=\varinjlim_\lambda\varinjlim_{J(B_\lambda)}C=\varinjlim_\lambda B_\lambda=B,
$$

using [det-ind-heart-canonical-presentation]. So $B$ is a filtered colimit of constructible sheaves.

*Direct sums.* $\bigoplus_{s\in S}B_s$ is the filtered colimit over finite subsets $T\subset S$ of
$\bigoplus_{s\in T}B_s$. A finite direct sum of filtered colimits $\varinjlim_{\alpha}C^{(s)}_{\alpha}$ is
the filtered colimit over the product of the index categories of the finite direct sums
$\bigoplus_{s\in T}C^{(s)}_{\alpha_s}$, which are constructible. So finite sums lie in
$\IndCons(X,\Lambda)$, and arbitrary ones by the first part.
