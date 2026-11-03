+++
id = "def-sc-group-scheme-subgroup"
kind = "definition"
title = "Subgroup schemes"
lean = ["AlgebraicGeometry.IsSubgroupScheme", "AlgebraicGeometry.IsNormalSubgroupScheme", "AlgebraicGeometry.IsClosedSubgroupScheme"]
order = 478
uses = ["def-sc-group-scheme"]
+++
Let $G$ be a group scheme over a
field $k$. A
*subgroup scheme* of $G$ is a $k$-group scheme $Z$ together
with a homomorphism $i:Z\to G$ whose
induced maps $i(R):Z(R)\to G(R)$ are injective for every $k$-algebra
$R$. The subgroup scheme is *normal* if $i(R)(Z(R))$ is a
normal subgroup of $G(R)$ for every $R$, and *closed* if $i$ is a
closed immersion. Equivalently, a *closed subgroup scheme* of $G$ is a
closed subscheme $Z\subseteq G$ such that for every $k$-algebra $R$ the
subset $Z(R)\subseteq G(R)$ is a subgroup of the group $G(R)$, with the
group structure on $Z$ through which the operations of $G$ factor.
