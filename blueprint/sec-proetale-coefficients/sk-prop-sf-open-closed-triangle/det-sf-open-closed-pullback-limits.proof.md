+++
kind = "proof"
of = "det-sf-open-closed-pullback-limits"
uses = ["def-exc-closed-site-lift", "lem-exc-closed-site-adjunction", "lem-exc-closed-inverse-image-formula", "lem-exc-closed-localization"]
+++
*Reduction to abelian sheaves and to affine $X$.* The $i^*B$-module
structure of $i^*F$ is induced from the $B$-module structure of $F$, and
limits and colimits of module sheaves are computed on underlying abelian
sheaves, so it suffices to treat abelian sheaves. Cover $X$ by finitely many
affine opens $X_k$. Restriction to $X_k$ and to $Z_k=Z\cap X_k$ commutes
with limits, colimits and with $i^*$ ([lem-exc-closed-localization]), and
the family of restrictions to the $Z_k$ is jointly conservative; so we may
assume $X=\operatorname{Spec}A$ and $Z=\operatorname{Spec}A/I$.

*(1) Evaluation on weakly contractible objects.* By
[lem-exc-closed-inverse-image-formula], $i^*F$ is the sheafification of the
presheaf $P_F(V)=F(v(V))$ on the basis $\mathcal B_Z$. Let $V$ be weakly
contractible. Every pro-étale covering family of $V$ can be refined to a
single weakly étale surjection $V'\to V$ (take a finite subfamily and its
disjoint union, $V$ being quasi-compact), and such a map has a section
because $V$ is weakly contractible. For a covering with a section the
augmented Čech complex of any presheaf is contractible (the section provides
an extra degeneracy), so $\check H^0(\{V'\to V\},P)=P(V)$ for every presheaf
$P$. Hence $P^+(V)=P(V)$ and $P^{++}(V)=P^+(V)=P(V)$ for $P=P_F$, i.e.
$(i^*F)(V)=F(v(V))$, the map being the canonical one into the
sheafification.

*(2) Limits.* Let $(F_\alpha)$ be a small diagram of sheaves on $X$ with limit
$F=\lim_\alpha F_\alpha$; limits of sheaves are computed sectionwise. For
weakly contractible $V$ as in (1),

$$
(i^*F)(V)=F(v(V))=\lim_\alpha F_\alpha(v(V))=\lim_\alpha(i^*F_\alpha)(V)
=\bigl(\lim_\alpha i^*F_\alpha\bigr)(V),
$$

and the composite is the value at $V$ of the canonical comparison
$i^*\lim_\alpha F_\alpha\to\lim_\alpha i^*F_\alpha$ by naturality of (1). The
weakly contractible affines form a basis of $Z_{\mathrm{proét}}$
(Bhatt–Scholze, Proposition 4.2.8), and a morphism of sheaves that is
bijective on the objects of a basis is an isomorphism. So $i^*$ preserves
limits.

*(3) Colimits and exactness.* The functor $i^*$ is left adjoint to $i_*$
([lem-exc-closed-site-adjunction] gives the adjunction on bases), so it
preserves all small colimits. Preserving finite limits and finite colimits,
it is exact.
