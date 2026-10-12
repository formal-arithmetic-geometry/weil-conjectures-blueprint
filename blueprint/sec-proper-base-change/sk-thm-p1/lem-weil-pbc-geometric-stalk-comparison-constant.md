+++
id = "lem-weil-pbc-geometric-stalk-comparison-constant"
kind = "lemma"
title = "Comparison of geometric module stalks normalized on constant sheaves"
uses = ["def-constructible-constant", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.exists_geometricStalkComparison_constant"]
source = "Stacks Project, Tag 04FN (stalk functors and pointed neighbourhoods), combined with Tag 09BH (3), generic submodule paragraph; agent-written separably closed module-valued formulation"
+++
Let $X$ be a scheme [def-weil-pbc-scheme-conventions] and $\Lambda$ a commutative ring. Let $s:\operatorname{Spec}\Omega\to X$ and $t:\operatorname{Spec}\Omega\prime\to X$ have the same image point, where $\Omega,\Omega\prime$ are separably closed fields. On the category of $\Lambda$-module sheaves on the small etale site [def-weil-pbc-etale-site], there exists a natural isomorphism $\beta:(-)_{s}\simeq(-)_{t}$ between the stalk functors [def-weil-pbc-geometric-stalks]. For every $\Lambda$-module $M$, the component $\beta_{M_X}$ is identity on $M$ under the canonical identifications of the stalks of the constant sheaf $M_X$ [def-constructible-constant] with $M$. No monomorphism, subsheaf, genericity or finiteness is assumed.
