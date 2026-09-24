+++
id = "lemma-weil-pbc-underived-exchange-naturality"
kind = "lemma"
title = "Sectionwise exchange is natural"
order = 1517
lean = ["AlgebraicGeometry.Etale.baseChangeMap_naturality"]
uses = ["def-weil-pbc-underived-exchange"]
+++
For every morphism $u:F\to G$ the square

$$
\begin{CD}
g^{-1}f_*F @>{\operatorname{Ex}_{\square,F}}>> f'_*g'^{-1}F\\
@V{g^{-1}f_*u}VV @VV{f'_*g'^{-1}u}V\\
g^{-1}f_*G @>{\operatorname{Ex}_{\square,G}}>> f'_*g'^{-1}G
\end{CD}
$$

commutes on every etale object of $Y'$.

## Proof

On a representative section $s_i$, both paths first apply $u$ and then
pull back along the same two maps. Since inverse image is a functor, the two
resulting sections of $g'^{-1}G$ are equal on each $V_i$ and therefore after
descent on $V$. Equality for all $V$ is equality of sheaf morphisms.
