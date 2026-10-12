+++
kind  = "proof"
of    = "sk-i-real-galois"
+++
*Sheaves and covers.* The functor $P\mapsto\underline{\operatorname{Hom}}_Y(-,P)$
from finite etale covers to finite locally constant sheaves of sets is an
equivalence. A finite etale cover is trivial after an etale base change, so
its sheaf of sections is locally constant with finite fibers. It is fully
faithful because a morphism of covers is determined by its graph, a closed
subscheme and hence a subsheaf, and every map of sheaves descends from a map
of finite sets over a common trivializing cover. It is essentially surjective
because the glueing data of a locally constant sheaf transport to a descent
datum for a trivial cover, which is effective for finite etale morphisms.

*Covers and $\pi_1$-sets.* For connected $Y$ the Galois covers are
cofinal among connected covers and pro-represent $F_{\bar y}$, so
$\pi_1(Y,\bar y)$ is profinite and acts continuously on every fiber, with open
stabilizers; the action is transitive on a connected cover. Hence
$F_{\bar y}$ is an equivalence onto finite continuous $\pi_1(Y,\bar y)$-sets,
compatibly with finite limits and colimits.

*Linear structure.* A $\Lambda$-module structure on a locally constant
sheaf is a $\Lambda$-action on the corresponding object, carried by both
equivalences; composing them gives the geometric-stalk functor of the
statement.

*Exactness and tensor.* Two locally constant sheaves
become constant on a common etale covering, on which a map between them is a
map of constant sheaves; its kernel and cokernel are therefore again locally
constant, and are computed on stalks, so the equivalence is exact. The same
common covering computes $\otimes_\Lambda$ stalkwise, so the equivalence is
compatible with tensor products.

*Compatibility with the stalk.* By construction the functor is the composite
of the two equivalences above, and the fibre $F_{\bar y}(P)$ of the cover $P$
attached to a locally constant sheaf $\mathcal F$ is the set of sections of
$\mathcal F$ over $\bar y$, i.e. the stalk $\mathcal F_{\bar y}$, with the
$\Lambda$-module structure induced from $\mathcal F$. Hence the underlying
$\Lambda$-module of the representation attached to $\mathcal F$ is
$\mathcal F_{\bar y}$, naturally in $\mathcal F$.
