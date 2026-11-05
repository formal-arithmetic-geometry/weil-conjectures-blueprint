+++
kind = "proof"
of = "lemma-simple-objects--2"
order = 1255002
uses = ["definition-constructible-sheaves", "lemma-largest-punctual-subsheaf", "lemma-boundary-stalk", "theorem-purity-real-sheaves-curves"]
+++
Choose a smaller dense open $k:V_0\hookrightarrow U_0$ on which
$A$ is lisse and $C$ vanishes. Restriction to a dense open preserves
irreducibility of lisse Weil sheaves
(`AlgebraicGeometry.WeilSheaf.IsIrreducibleLisse.upperStar_of_isDominant`),
as in the proof of [theorem-purity-real-sheaves-curves]. Hence the
lisse subsheaf $A|_{V_0}\subset N|_{V_0}$ is zero or all of
$N|_{V_0}$.

If $A|_{V_0}=0$, then $A$ is a punctual subsheaf of $j_*N$, so
$A=0$ by [lemma-largest-punctual-subsheaf]. Thus $s$ is injective
and becomes an isomorphism on $V_0$. The unit
$\theta:B\to j_*k_*(B|_{V_0})$ has punctual kernel, which vanishes
by the hypothesis on $B$. Moreover, $\theta\circ s$ is an isomorphism:
on $V_0$ the map $s$ is an isomorphism, and
$N\to k_*k^*N$ is an isomorphism by [lemma-boundary-stalk].
It follows that $\theta$ and $s$ are isomorphisms, and exactness
gives $C=0$.

If $A|_{V_0}=N|_{V_0}$, then exactness and $C|_{V_0}=0$ give
$B|_{V_0}=0$. Thus $B$ is punctual and the hypothesis on its
punctual subsheaves gives $B=0$.
