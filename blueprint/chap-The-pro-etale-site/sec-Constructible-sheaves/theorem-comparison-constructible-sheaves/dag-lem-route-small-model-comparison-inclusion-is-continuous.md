+++
id = "dag-lem-route-small-model-comparison-inclusion-is-continuous"
kind = "dag-lemma"
title = "The transported inclusion is continuous, retaining the original covers."
name_showing = false
order = 149536
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-route-small-model-comparison-inclusion-is-continuous"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.smallModelComparisonInclusion_isContinuous"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Let $X$ be any scheme and use the small etale and pro-etale sites $C=X_{\mathrm{Et}}$ and $D=X_{\mathrm{proet}}$, with their original Grothendieck topologies $J$ and $K$ [def-weil-pbc-etale-site, def-weil-pbc-proetale-site]. Write $i:C\to D$ for the inclusion `def-weil-pbc-site-comparison-morphism`. For arbitrary universe parameters $u,v$ with $X:\mathrm{Scheme}_u$, put $w=\max(v,u+1)$ and take the canonical equivalent copies $C^s=\operatorname{AsSmall}_w(C)$ and $D^s=\operatorname{AsSmall}_w(D)$, in the size convention `def-weil-size-convention`. Denote the canonical equivalences and their quasi-inverses by $d_C:C^s\to C$, $a_C:C\to C^s$, $d_D:D^s\to D$ and $a_D:D\to D^s$ (the named functors AsSmall.down and AsSmall.up).

Equip $C^s$ and $D^s$ with the topologies $J^s=d_C.\operatorname{inducedTopology}(J)$ and $K^s=d_D.\operatorname{inducedTopology}(K)$: a sieve is covering exactly when its image under the corresponding down equivalence generates a covering sieve on the original site `lem-weil-pbc-site-equivalence-sheaf-transport`. Thus these are the original topologies transported along the equivalences, with every original object retained in an equivalent copy. Then
$$i^s=a_D\circ i\circ d_C:(C^s,J^s)\longrightarrow(D^s,K^s)$$
is continuous: for every sheaf of sets $G$ on $(D^s,K^s)$, the presheaf $(i^s)^{\mathrm{op}}\mathbin{\cdot}G$ on $C^s$, taking $U$ to $G(i^s(U))$ and $f$ to $G(i^s(f))$, is a $J^s$-sheaf. Here $i^s$, $J^s$ and $K^s$ are precisely smallModelComparisonInclusion, smallModelComparisonEtaleTopology and coefficientProEtaleModelTopology.

(SHEAF DAG node `lem-route-small-model-comparison-inclusion-is-continuous`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: statement. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-etale-site`, `def-weil-size-convention`, `lem-weil-pbc-site-equivalence-sheaf-transport`.
