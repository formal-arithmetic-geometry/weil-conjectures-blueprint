+++
id = "def-kun-global-generated"
kind = "definition"
title = "Globally generated sheaves"
lean = ["AlgebraicGeometry.Etale.IsGloballyGenerated"]
order = 3123
uses = ["def-kun-constant-sheaf", "def-weil-pbc-etale-sheaves"]
+++
Let $T$ be a scheme and $F$ a sheaf of $\Lambda_T$-modules on
$T_{\Et}$. The *evaluation morphism* of $F$ is

$$
\bigoplus_{s\in\Gamma(T_{\Et},F)}\underline{\Lambda}\longrightarrow F,
\qquad 1_s\longmapsto s,
$$

and $F$ is *globally generated* if this morphism is an
epimorphism of sheaves. For abelian sheaves take
$\Lambda=\mathbf Z$.
