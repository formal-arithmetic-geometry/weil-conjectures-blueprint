+++
id = "lem-wf-dense-identity-component"
kind = "lemma"
title = "A dense subgroup is dense in the identity component"
order = 2660
uses = ["def-wf-algebraic-components", "lem-wf-algebraic-component-cosets"]
+++
Let $\Gamma$ be a Zariski-dense subgroup of a linear algebraic group
$H$, and put $\Gamma^\circ=\Gamma\cap H^\circ$. Then
$\Gamma^\circ$ is Zariski dense in $H^\circ$.

## Proof

By [lem-wf-algebraic-component-cosets], the components are the
finitely many disjoint open-and-closed cosets of $H^\circ$, and
$H/H^\circ$ is finite. The identity-component notation is that of
[def-wf-algebraic-components].

Density forces
$\Gamma$ to meet every component: a component missed by $\Gamma$
would be a nonempty open-and-closed subset disjoint from its closure.
Choose representatives
$\gamma_1=1,\gamma_2,\ldots,\gamma_r\in\Gamma$, one in each
component, and let
$K$ be the Zariski closure of $\Gamma^\circ$ in $H^\circ$. Then

$$
\Gamma\subseteq\bigcup_{i=1}^r\gamma_iK,
\qquad\text{hence}\qquad
H=\bigcup_{i=1}^r\gamma_iK
$$

after taking closures. Intersect this equality with $H^\circ$.
The cosets $\gamma_iH^\circ$ are disjoint, and only
$\gamma_1H^\circ=H^\circ$ meets $H^\circ$; since
$K\subseteq H^\circ$, the intersection says $H^\circ=K$.
This is exactly the asserted density.
