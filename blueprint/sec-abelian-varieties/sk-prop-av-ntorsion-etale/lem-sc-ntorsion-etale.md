+++
id = "lem-sc-ntorsion-etale"
kind = "lemma"
title = "The $n$-torsion of an abelian variety is etale"
lean = ["AlgebraicGeometry.etale_torsionSubgroupScheme", "AlgebraicGeometry.isFinite_torsionSubgroupScheme", "AlgebraicGeometry.bijective_toUnit_comp_torsionSubgroupScheme", "AlgebraicGeometry.nonempty_addEquiv_torsionBy", "AlgebraicGeometry.torsionByEquiv"]
order = 613
uses = ["def-sc-abelian-variety", "def-sc-group-scheme", "def-sc-mult-n", "lem-sc-av-commutative"]
+++
Let $A$ be an abelian variety
of dimension $g$ over a field $k$ and let
$n\geq1$ be prime to $\operatorname{char}k$. Then
$A[n]=\ker([n])$ ([def-sc-mult-n]) is a finite etale
group scheme over $k$. If moreover $k$ is algebraically closed, the
canonical base change map

$$
A[n](k)\xrightarrow{\ \sim\ }A[n](k')
$$

is a bijection for every extension $k\subseteq k'$ of
algebraically closed fields, and the $n$-torsion subgroup of $A(k)$
satisfies

$$
A[n](k)=A(k)[n]\cong(\mathbf Z/n\mathbf Z)^{2g}.
$$
