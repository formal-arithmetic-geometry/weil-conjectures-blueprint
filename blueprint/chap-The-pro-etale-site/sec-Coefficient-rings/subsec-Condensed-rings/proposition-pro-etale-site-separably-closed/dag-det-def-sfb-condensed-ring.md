+++
id = "dag-det-def-sfb-condensed-ring"
kind = "dag-definition"
title = "Condensed coefficient rings $\\underline T$"
name_showing = false
order = 173505
tags = ["sheaf-dag"]
split_from = "proposition-pro-etale-site-separably-closed--3"
dag_id = "det-def-sfb-condensed-ring"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["Profinite.CondensedRing", "CategoryTheory.Sheaf.monObj_sheafCompose_obj", "CategoryTheory.Sheaf.isCommMonObj_sheafCompose_obj", "Profinite.continuousMapRingPresheaf", "Profinite.isSheaf_continuousMapRingPresheaf", "Profinite.continuousMapRingSheaf", "Profinite.continuousMapRingObj", "Profinite.isCommMonObj_continuousMapRingObj", "Profinite.continuousMapRingSheafMap", "Profinite.continuousMapRingSheafMap_id", "Profinite.continuousMapRingSheafMap_comp", "Profinite.padicIntCondensedRing", "Profinite.padicCondensedRing", "Profinite.padicSubfieldCondensedRing", "Profinite.padicIntegersCondensedRing", "Profinite.padicIntegersRingObj", "Profinite.isCommMonObj_padicIntegersRingObj", "Profinite.padicIntCondensedRingToPadicCondensedRing", "Profinite.padicCondensedRingToPadicSubfieldCondensedRing", "Profinite.padicIntegersCondensedRingToPadicSubfieldCondensedRing", "Profinite.padicIntCondensedRingToPadicIntegersCondensedRing", "Profinite.continuousMapRingPresheafOfUniverse", "Profinite.isSheaf_continuousMapRingPresheafOfUniverse", "Profinite.continuousMapRingSheafOfUniverse", "Profinite.continuousMapRingObjOfUniverse", "Profinite.continuousMapRingObjOfUniverseMonObj", "Profinite.isCommMonObj_continuousMapRingObjOfUniverse", "Profinite.continuousMapRingSheafMapOfUniverse", "Profinite.isMonHom_continuousMapRingObjMapOfUniverse"]
uses = ["dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
The *pro-étale site of a point*, $*_{\mathrm{proét}}$, is the category of profinite sets
with the coherent topology. In it, a finite family $\{S_i\to S\}$ covers $S$ exactly when
$\coprod_iS_i\to S$ is surjective, and a sieve covers when it contains such a family. A
*condensed ring* is a sheaf of rings on $*_{\mathrm{proét}}$. By `det-def-sfb-ring-object`,
its underlying condensed abelian group is a ring object of $\Sh(*_{\mathrm{proét}},\Ab)$.

For a topological ring $T$, the condensed ring $\underline T$ is defined by its sections,

$$
\underline T(S):=C(S,T),
$$

with restriction by precomposition and pointwise ring operations. It is a sheaf, and its
underlying ring object of $\Sh(*_{\mathrm{proét}},\Ab)$ is commutative when $T$ is. A
continuous ring homomorphism $\varphi\colon T\to T'$ induces a morphism of condensed rings
$\varphi_*\colon\underline T\to\underline{T'}$ by postcomposition, and this is functorial in
$\varphi$.

Fix a prime $\ell$ and an algebraic closure $\Qlb$ of $\mathbf Q_\ell$, with the absolute
value extending that of $\mathbf Q_\ell$. This gives the following commutative condensed
rings:

- $\underline{\mathbf Z}_\ell$ and $\underline{\mathbf Q}_\ell$, for the $\ell$-adic topologies;
- for a subfield $E$ of $\Qlb$ (a field with an embedding $E\hookrightarrow\Qlb$), the
  condensed rings $\underline E$ and $\underline{\cO}_E$. Here $E$ has the topology
  restricted from $\Qlb$, and $\cO_E=\{x\in E:|x|\le1\}$ is its ring of integers.

Postcomposition with continuous inclusions gives the morphisms of condensed rings
$\underline{\cO}_E\to\underline E$, and, when $E$ contains $\mathbf Q_\ell$ compatibly with
the embedding, $\underline{\mathbf Z}_\ell\to\underline{\mathbf Q}_\ell\to\underline E$ and
$\underline{\mathbf Z}_\ell\to\underline{\cO}_E\to\underline E$.

(SHEAF DAG node `det-def-sfb-condensed-ring`; machine-alignment layer.) Split from [proposition-pro-etale-site-separably-closed--3]. DAG kind: definition. DAG status: split. Lean names not on master: `CategoryTheory.coherentTopology`, `CategoryTheory.coherentTopology.mem_sieves_iff_hasEffectiveEpiFamily`, `Profinite.effectiveEpiFamily_tfae`, `Profinite.continuousMapRingSheafMapOfUniverse_app_apply`, `Profinite.continuousMapRingSheafMapOfUniverse_id`, `Profinite.continuousMapRingSheafMapOfUniverse_comp`. Statement dependencies not drawn: `def-sfb-continuous-map-condensed-ring-map`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-structure`, `lem-coef-grothendieck-locally-presentable`, `lem-weil-pbc-sheaf-tensor-closed`, `sk-def-sfb-sheaf-tensor`.
