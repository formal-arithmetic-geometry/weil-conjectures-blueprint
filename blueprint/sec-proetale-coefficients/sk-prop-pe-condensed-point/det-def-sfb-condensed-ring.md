+++
id = "det-def-sfb-condensed-ring"
kind = "definition"
title = "Condensed coefficient rings $\\underline T$"
order = 1068
uses = ["det-def-sfb-ring-object"]
lean = ["Profinite.continuousMapRingSheaf", "Profinite.continuousMapRingObj", "Profinite.continuousMapRingSheafMap", "Profinite.padicIntCondensedRing", "Profinite.padicCondensedRing", "Profinite.padicSubfieldCondensedRing", "Profinite.padicIntegersCondensedRing", "Profinite.isCommMonObj_continuousMapRingObj", "Profinite.padicIntCondensedRingToPadicCondensedRing", "Profinite.padicCondensedRingToPadicSubfieldCondensedRing", "Profinite.padicIntegersCondensedRingToPadicSubfieldCondensedRing", "Profinite.padicIntCondensedRingToPadicIntegersCondensedRing"]
+++
The *pro-étale site of a point*, $*_{\mathrm{proét}}$, is the category of profinite sets
with the coherent topology. In it, a finite family $\{S_i\to S\}$ covers $S$ exactly when
$\coprod_iS_i\to S$ is surjective, and a sieve covers when it contains such a family. A
*condensed ring* is a sheaf of rings on $*_{\mathrm{proét}}$. By [det-def-sfb-ring-object],
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
