+++
kind = "proof"
of = "det-ind-heart-full-faithfulness"
+++
(1) A filtered colimit of sheaves in degree $0$ is a filtered diagram of complexes vanishing below
degree $0$. Part (1) of [sk-lem-constructible-ext-continuity] with $q=0$ gives
$\varinjlim_i\Hom(C,K_i)\cong\Hom(C,\varinjlim_iK_i)$; for sheaves concentrated in degree $0$ these are
Homs in $\Mod(X_{\mathrm{proét}},\Lambda)$.

(2) In $\operatorname{Ind}(\Cons(X,\Lambda))$, by definition,

$$
\Hom\bigl(\text{“}\varinjlim\text{”}_\alpha C_\alpha,\text{“}\varinjlim\text{”}_\beta D_\beta\bigr)
=\varprojlim_\alpha\varinjlim_\beta\Hom_{\Cons}(C_\alpha,D_\beta).
$$

On the other side, a colimit in the first variable turns into a limit, and by (1)

$$
\Hom_\Lambda(\varinjlim_\alpha C_\alpha,\varinjlim_\beta D_\beta)
=\varprojlim_\alpha\Hom_\Lambda(C_\alpha,\varinjlim_\beta D_\beta)
=\varprojlim_\alpha\varinjlim_\beta\Hom_\Lambda(C_\alpha,D_\beta).
$$

Since $\Cons(X,\Lambda)$ is a full subcategory, $\Hom_\Lambda(C_\alpha,D_\beta)=\Hom_{\Cons}(C_\alpha,D_\beta)$,
and the map induced by $\Phi$ is the identity of these limits-of-colimits. Hence $\Phi$ is fully
faithful.
