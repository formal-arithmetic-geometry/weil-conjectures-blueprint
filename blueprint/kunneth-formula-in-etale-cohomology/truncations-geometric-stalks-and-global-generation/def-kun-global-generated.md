+++
id = "def-kun-global-generated"
kind = "definition"
title = "Globally generated sheaves"
order = 6033
lean = ["AlgebraicGeometry.Etale.IsGloballyGenerated"]
uses = ["def-kun-constant-sheaf"]
+++
Let $T$ be a scheme and $F$ a sheaf of $\Lambda_T$-modules on $T_{\Et}$. The
*evaluation morphism* of $F$ is
$$
\bigoplus_{s\in\Gamma(T_{\Et},F)}\underline{\Lambda}\longrightarrow F,\qquad1_s\longmapsto s,
$$
and $F$ is *globally generated* if this morphism is an epimorphism of
sheaves; the equivalent description by surjectivity of the evaluation
morphism on every geometric stalk is
[lem-kun-global-generated-stalkwise]. For abelian sheaves take
$\Lambda=\mathbf Z$.

Unresolved dependencies: def:weil-pbc-etale-sheaves
