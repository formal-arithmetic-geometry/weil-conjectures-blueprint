+++
id = "def-sc-group-scheme-subgroup"
kind = "definition"
title = "Subgroup schemes"
order = 3903
lean = ["AlgebraicGeometry.GroupScheme.IsClosedSubgroupScheme", "AlgebraicGeometry.GroupScheme.SubgroupScheme"]
uses = ["def-sc-group-scheme"]
+++
Let $G$ be a group scheme [def-sc-group-scheme] over a field $k$. A
*closed subgroup scheme* of $G$ is a closed subscheme $Z\subseteq G$ such
that for every $k$-algebra $R$ the subset $Z(R)\subseteq G(R)$ is a
subgroup of the group $G(R)$. A *subgroup scheme* of $G$ is a $k$-group
scheme $Z$ together with a homomorphism [def-sc-group-scheme] $i:Z\to G$
whose induced maps $i(R):Z(R)\to G(R)$ are injective for every
$k$-algebra $R$. The subgroup scheme is *normal* if $i(R)(Z(R))$ is a
normal subgroup of $G(R)$ for every $R$.
