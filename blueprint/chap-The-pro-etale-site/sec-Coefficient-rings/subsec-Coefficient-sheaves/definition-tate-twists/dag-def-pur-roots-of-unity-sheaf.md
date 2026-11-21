+++
id = "dag-def-pur-roots-of-unity-sheaf"
kind = "dag-definition"
title = "The pro-etale sheaf of roots of unity"
name_showing = false
order = 184507
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-roots-of-unity-sheaf"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.proEtaleUnitsPower", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnitySheaf", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnityInclusion", "AlgebraicGeometry.Scheme.existsUnique_proEtaleRootsOfUnitySections", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnitySections", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnity_nsmul", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnityCoefficientRing", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnityModule", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnityTransition_condition", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnityTransition", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnity_nsmul_of_dvd", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnityTransition_prime", "AlgebraicGeometry.Scheme.proEtaleRootsOfUnityTower"]
uses = ["dag-def-pur-abelian-sheaf-kernel", "dag-def-pur-proetale-structure-sheaf", "dag-def-pur-proetale-units-sheaf", "dag-def-weil-pbc-constant-sheaf", "dag-def-weil-pbc-proetale-site"]
+++
Let $S$ be a scheme and $N\in\mathbf Z_{\geq1}$. On the small pro-etale site
[dag-def-weil-pbc-proetale-site] $S_{\mathrm{proet}}$ let $\mathcal O_S$ be the structure
sheaf of rings [dag-def-pur-proetale-structure-sheaf], $\mathcal O_S(U)=\Gamma(U,\mathcal O_U)$,
and $\mathbf G_{m,S}=\mathcal O_S^\times$ the sheaf of abelian groups of its units
[dag-def-pur-proetale-units-sheaf], $\mathbf G_{m,S}(U)=\Gamma(U,\mathcal O_U)^\times$. The
*$N$-th power map* $[N]:\mathbf G_{m,S}\to\mathbf G_{m,S}$, $u\mapsto u^N$ on the
sections over every $U$, is a morphism of sheaves of abelian groups: on each $U$ it is a
group homomorphism because $\Gamma(U,\mathcal O_U)^\times$ is commutative, and it commutes
with restriction because the restriction maps are ring homomorphisms. The *sheaf of
$N$-th roots of unity* is its kernel [dag-def-pur-abelian-sheaf-kernel]

$$
 \mu_{N,S}=\ker\bigl([N]:\mathbf G_{m,S}\to\mathbf G_{m,S}\bigr),\qquad
 \mu_{N,S}(U)=\{u\in\Gamma(U,\mathcal O_U^\times):u^N=1\}
 \qquad(U\to S\text{ weakly etale}),
$$

a sheaf of abelian groups whose group of sections over $U$ is the group of $N$-th roots of
unity of the ring $\Gamma(U,\mathcal O_U)$, with the restriction maps of
$\mathcal O^\times$ along morphisms $V\to U$ over $S$. Every group $\mu_{N,S}(U)$ is killed
by $N$, so $\mu_{N,S}$ is a sheaf of modules `def-weil-sheaf-of-modules-category` over the
constant sheaf $(\mathbf Z/N\mathbf Z)_S$ [dag-def-weil-pbc-constant-sheaf], with the unique
module structure of [dag-lem-pur-torsion-sheaf-constant-module]. For $N\mid N'$, the
*transition map*

$$
 \mu_{N',S}\longrightarrow\mu_{N,S},\qquad u\longmapsto u^{N'/N},
$$

is well defined, since $(u^{N'/N})^N=u^{N'}=1$, and is a morphism of sheaves of abelian
groups for the same reasons as $[N]$; as both sheaves are killed by $N'$, it is a morphism
of sheaves of $(\mathbf Z/N'\mathbf Z)_S$-modules by
[dag-lem-pur-torsion-sheaf-constant-module] (2). For a prime $\ell$ and $N=\ell^r$,
$N'=\ell^{r+1}$ it is $u\mapsto u^\ell$, and $(\mu_{\ell^r,S})_{r\geq1}$ with these maps is
an inverse system of sheaves of abelian groups.

(SHEAF DAG node `def-pur-roots-of-unity-sheaf`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. DAG status: split. Lean names not on master: `AlgebraicGeometry.Scheme.proEtaleRootsOfUnityTransition_linear`, `AlgebraicGeometry.Scheme.proEtaleRootsOfUnityTransitionModule`. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `sk-def-pbc-conventions`.
