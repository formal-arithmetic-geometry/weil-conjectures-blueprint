+++
kind  = "proof"
of    = "sk-prop-av-ntorsion-etale"
uses = ["sk-cor-av-commutative", "sk-def-av-group-scheme", "sk-prop-av-prime-p-etale", "sk-prop-av-mult-surjective", "sk-thm-picard-main", "sk-cor-picard-degree"]
+++
We prove the statement for an abelian variety $A$ of dimension $g$ over
$k$ and $n$ invertible in $k$; the corollary is the case $A=J(C)$, which
is an abelian variety of dimension $g$ whose formation commutes with
extension of the ground field ([sk-thm-picard-main]).

*Étaleness and base extension.* By [sk-prop-av-isogeny], $A[n]$ is a
finite flat group scheme of order $n^{2g}$ over $k$; as $n$ is prime to
$\operatorname{char}k$, it is étale ([sk-prop-av-prime-p-etale]); so it
is finite étale of rank $n^{2g}$ (this is the proposition on
multiplication on an abelian variety). A finite étale scheme of rank $r$
over algebraically closed $k$ is a disjoint union of $r$ copies of
$\Spec k$. This description is stable under base extension, so the
natural map on $k$-points is a bijection
([sk-prop-av-finite-etale-points]). For $A=J(C)$, apply it to the kernel,
using the base-change compatibility of the Jacobian
($J(C)_K=J(C_K)$) and of $[n]$.

*Group structure.* $A(k)$ is commutative ([sk-cor-av-commutative]).
For a prime $q\mid n$ and $q^a\mid n$, the group $A[q^a](k)$ has order
$q^{2ga}$, is killed by $q^a$, and its subgroup killed by $q$, namely
$A[q](k)$, has order $q^{2g}$. The classification of finite abelian groups
therefore gives $2g$ cyclic factors, each of exponent at most $q^a$.
Their orders have product $q^{2ga}$, so every factor has order $q^a$
(this is also [sk-prop-av-divisible-structure]). Combining the
prime-power parts (Chinese remainder theorem: $A[n]=\prod_qA[q^{a_q}]$
for $n=\prod_q q^{a_q}$) gives
$A[n](k)=A(k)[n]\simeq(\Z/n\Z)^{2g}$. No basis is distinguished, so the
isomorphism is not canonical.

*Divisibility and $\operatorname{Pic}$.* Every fibre of the finite
surjective $[n]$ ([sk-prop-av-mult-surjective]) over a $k$-point is a
nonempty finite $k$-scheme, which has a $k$-point as $k$ is algebraically
closed; this proves divisibility of $A(k)$ ([sk-prop-av-divisible]). In
the degree sequence
$0\to J(C)(k)\to\operatorname{Pic}(C)\to\Z\to0$ of [sk-cor-picard-degree],
the group $\Z$ has no $n$-torsion and $J(C)(k)/n=0$. The snake lemma for
multiplication by $n$ gives
$0\to J(C)(k)[n]\to\operatorname{Pic}(C)[n]\to\Z[n]=0$ and
$0=J(C)(k)/n\to\operatorname{Pic}(C)/n\to\Z/n\to0$, which proves the two
assertions for $\operatorname{Pic}(C)$.
