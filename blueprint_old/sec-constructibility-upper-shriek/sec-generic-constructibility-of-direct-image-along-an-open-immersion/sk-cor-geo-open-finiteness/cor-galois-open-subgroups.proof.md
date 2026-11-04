+++
kind  = "proof"
of    = "cor-galois-open-subgroups"
+++
Here $\pi_1=\pi_1(Y,\bar y)=\operatorname{Aut}(F_{\bar y})$ is the group
of [def-galois-fibre-functor] and the covers are the finite etale
covers of [def-galois-object]. Under [thm-galois-fundamental] connected finite etale covers of $Y$
correspond to transitive finite continuous $\pi_1$-sets — the
transitivity being that of [lem-galois-transitive] — i.e. to
$\pi_1/H$ with $H$ open. Stabilizers are open because the action on the
finite set $P_{\bar y}$ is continuous. If $x\in P_{\bar y}$ has
stabilizer $H$, the orbit map $gH\mapsto gx$ is an equivariant
bijection $\pi_1/H\to P_{\bar y}$ carrying the coset $H$ to $x$, so
$\#F_{\bar y}(P)=\#\pi_1/H=[\pi_1:H]$ is the degree. Conversely, for
$H$ open the finite continuous transitive $\pi_1$-set $\pi_1/H$ comes
from a connected cover, and the stabilizer of the coset $H$ is $H$; so
every open subgroup occurs. An equivariant bijection
$\pi_1/H\to\pi_1/H'$ sending $H$ to $H'$ exists exactly when $H=H'$;
since the fibre functor is fully faithful, pointed connected covers are
isomorphic exactly when their stabilizers agree. The stabilizer of
$gx$ is $gHg^{-1}$, and by transitivity these are all the stabilizers
of points of $P_{\bar y}$, so forgetting the point gives a conjugacy
class. An equivariant bijection $\pi_1/H\to\pi_1/H'$ exists exactly when
$H$ and $H'$ are conjugate (it sends $H$ to some $gH'$, whose
stabilizer $gH'g^{-1}$ must equal $H$), so unpointed connected covers
are isomorphic exactly when their stabilizers are conjugate. Together
with the existence statement, both assignments are bijective.
