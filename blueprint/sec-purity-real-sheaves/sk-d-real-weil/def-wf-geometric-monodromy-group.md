+++
id = "def-wf-geometric-monodromy-group"
kind = "definition"
title = "Monodromy groups of a lisse Weil sheaf"
lean = ["AlgebraicGeometry.WeilGroup.toLinearAut"]
order = 3790
uses = ["d-central", "d-monodromy", "def-sc-general-linear-group", "def-wf-fundamental-representation", "def-wf-geometric-semisimplicity", "def-wf-monodromy-data", "def-wf-weil-group", "lem-wf-weil-fundamental-representation", "lem-wf-weil-group-exact-sequence"]
+++
Let $\mathcal F_0$ be a lisse Weil sheaf as in
[def-wf-fundamental-representation], with Weil fundamental representation
$\rho:W(X_0)\to\operatorname{GL}(V)$ (a homomorphism by
[lem-wf-weil-fundamental-representation]), let
$\Pi=\pi_1(X,\bar x)$ be the geometric subgroup of the Weil group, and
choose $s\in W(X_0)$ of degree one for the degree map of
[def-wf-weil-group]. By [lem-wf-weil-group-exact-sequence],
$(W(X_0),\deg,s)$ is a degree datum with $P=\Pi$, and $\rho$, written in
a basis of $V$, makes it a represented degree datum ([d-monodromy]).

The *geometric monodromy group* of $\mathcal F_0$ is the group $H$ of
this datum, the closed linear algebraic subgroup

$$
H_{\mathrm{geom}}=\overline{\rho(\Pi)}^{\,\mathrm{Zar}}
\subseteq\operatorname{GL}(V).
$$

The closure is taken in the Zariski topology of the affine algebraic
group
$\operatorname{GL}(V)=\operatorname{Spec} \overline{\mathbf Q}_\ell[x_{ij},\det(x)^{-1}]$ of [def-sc-general-linear-group], not in the ambient
affine space of all matrices. Equivalently it is the common zero locus
in $\operatorname{GL}(V)$ of the regular functions vanishing on
$\rho(\Pi)$. To avoid a clash with the arithmetic monodromy extension
$G_{\mathrm{arith}}(\rho)$, the closure $G$ of $\rho(W(X_0))$ is
written $G_{\mathrm{Zar}}$.

The *monodromy data* of $\mathcal F_0$ are those of this datum
([def-wf-monodromy-data]). The sheaf $\mathcal F_0$ is *semisimple*,
resp. *geometrically semisimple*, when the datum is semisimple
([d-monodromy]), resp. geometrically semisimple
([def-wf-geometric-semisimplicity]).
Its *positive central Frobenius representatives* $(N,z)$ are the positive central pairs
([d-central]) of this datum.
