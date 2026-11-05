+++
id = "lemma-scheme-frobenius-geometric-frobenius--4"
kind = "lemma"
title = "The operator of a graph with an arbitrary coefficient morphism"
name_showing = false
order = 953004
aliases = ["bp-r290-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.globalOperator_ofGraph"]
uses = ["definition-action-correspondence"]
+++
The comparison for an arbitrary morphism $(\operatorname{Fr}_X^m)^*K\to K$
is bypassed by Lean; its route uses the following graph formula.

Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be prime, and let
$X/k$ be separated and of finite type. Let $h:X\to X$ be a proper
$k$-endomorphism, let $K\in\Dbc(X,\Qbarl)$ in the condensed coefficient
model, and let $v:h^*K\to K$ be any morphism. For the graph
$c=(\operatorname{id}_X,h)$, regard $v$ as a cohomological correspondence
using $K\simeq(\operatorname{id}_X)^!K$. Then

$$
T_c(v)=\RGammac(X,v)\circ h^\sharp,
$$

where $h^\sharp:\RGammac(X,K)\to\RGammac(X,h^*K)$ is induced by the unit
$K\to Rh_*h^*K$, the properness identification $Rh_*\simeq Rh_!$, and
composition for the lower shriek. No invertibility of $v$ is assumed.
