+++
id = "dag-def-pur-proetale-structure-sheaf"
kind = "dag-definition"
title = "The structure sheaf of rings on the small pro-etale site"
name_showing = false
order = 184505
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-proetale-structure-sheaf"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.proEtaleStructurePresheaf", "AlgebraicGeometry.Scheme.proEtaleStructurePresheaf_isSheaf", "AlgebraicGeometry.Scheme.proEtaleStructureSheaf"]
uses = ["dag-def-weil-pbc-small-proetale-site"]
+++
Let $S$ be a scheme `def-pc-scheme` and $S_{\mathrm{proet}}$ its small pro-etale site
[dag-def-weil-pbc-small-proetale-site]. The *structure sheaf* $\mathcal O_S$ on
$S_{\mathrm{proet}}$ is the presheaf of commutative rings

$$
 \mathcal O_S(U)=\Gamma(U,\mathcal O_U)\qquad(U\to S\text{ weakly etale}),
$$

whose restriction map along a morphism $h:V\to U$ over $S$ is the ring map
$h^\sharp:\Gamma(U,\mathcal O_U)\to\Gamma(V,\mathcal O_V)$ on global sections. Here $\Gamma(U,\mathcal O_U)=\mathcal O_U(U)$ is the ring of sections over the whole scheme $U$, and $h^\sharp$ is the component over $U$ of the morphism of structure sheaves of $h$. It is a
sheaf of rings on $S_{\mathrm{proet}}$: as a presheaf of sets it is isomorphic to
$U\mapsto\operatorname{Mor}(U,\operatorname{Spec}\mathbf Z[t])$ (a morphism to
$\operatorname{Spec}\mathbf Z[t]$ is a ring map $\mathbf Z[t]\to\Gamma(U,\mathcal O_U)$,
i.e. a global section), where $\operatorname{Spec}$ is the spectrum construction `def-weil-affine-spectrum`; hence it is representable on schemes and satisfies the sheaf
condition for fpqc coverings; the coverings of $S_{\mathrm{proet}}$ are fpqc coverings,
and the sheaf condition for a presheaf of rings is that of its underlying presheaf of
sets.

(SHEAF DAG node `def-pur-proetale-structure-sheaf`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pc-scheme`, `def-weil-affine-spectrum`.
