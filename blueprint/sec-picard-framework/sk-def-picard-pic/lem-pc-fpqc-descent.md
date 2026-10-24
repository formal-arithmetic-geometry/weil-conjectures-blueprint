+++
id = "lem-pc-fpqc-descent"
kind = "lemma"
title = "FPQC descent for quasi-coherent modules"
order = 624
uses = ["def-sc-invertible-module"]
lean = ["AlgebraicGeometry.bijective_toDescentData_map", "AlgebraicGeometry.exists_isQuasicoherent_toDescentData_iso", "AlgebraicGeometry.isFinitePresentation_of_toDescentData_iso", "AlgebraicGeometry.isLocallyFree_of_toDescentData_iso", "AlgebraicGeometry.isFiniteLocallyFreeOfRank_of_toDescentData_iso", "AlgebraicGeometry.isInvertible_of_toDescentData_iso"]
+++
Let $\{f_i:S_i\to S\}_{i\in I}$ be an fpqc covering of
schemes.

1. The functor $\mathcal{M}\mapsto(f_i^*\mathcal{M},\mathrm{can})_{i\in I}$
from quasi-coherent $\mathcal{O}_S$-modules to descent data of
quasi-coherent modules for this covering (quasi-coherent
$\mathcal{O}_{S_i}$-modules $\mathcal{M}_i$ with isomorphisms
$\varphi_{ii'}:\mathrm{pr}_1^*\mathcal{M}_i\to\mathrm{pr}_2^*\mathcal{M}_{i'}$
on $S_i\times_SS_{i'}$ satisfying the cocycle condition on the triple
products) is an equivalence of categories: every descent datum is
effective.
2. The equivalence preserves and reflects finite presentation and
finite local freeness (of a given rank $r$): a quasi-coherent
$\mathcal{M}$ has one of these properties if and only if every
$f_i^*\mathcal{M}$ has it.
3. In particular (*descent of invertible modules*, [def-sc-invertible-module]):
invertible $\mathcal{O}_{S_i}$-modules with gluing isomorphisms
satisfying the cocycle condition glue to an invertible
$\mathcal{O}_S$-module $\mathcal{L}$ with $f_i^*\mathcal{L}\cong\mathcal{L}_i$
compatibly with the gluing data; and if an invertible
$\mathcal{O}_S$-module $\mathcal{L}$ admits trivializations
$f_i^*\mathcal{L}\cong\mathcal{O}_{S_i}$ whose two pullbacks to every
$S_i\times_SS_{i'}$ agree (i.e. compatible with the canonical gluing
isomorphisms), then $\mathcal{L}\cong\mathcal{O}_S$. (Without the
compatibility this fails already for Zariski coverings.)

In particular, applied to the fpqc covering $\{X_{T_i}\to X_T\}$ obtained by base change
from an fpqc covering $\{T_i\to T\}$ and a morphism $X\to T$: cartesian families
$\mathcal{L}_i$ on $X_{T_i}$ satisfying the cocycle condition glue to an
invertible $\mathcal{L}$ on $X_T$ with $\mathcal{L}|_{X_{T_i}}\cong\mathcal{L}_i$.
