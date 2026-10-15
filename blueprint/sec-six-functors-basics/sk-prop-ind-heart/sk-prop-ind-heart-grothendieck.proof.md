+++
kind = "proof"
of = "det-ind-heart-grothendieck"
+++
By [det-ind-heart-kernels-cokernels], $\IndCons(X,\Lambda)$ is a full additive subcategory of the abelian
category $\Mod(X_{\mathrm{proét}},\Lambda)$ closed under kernels and cokernels (finite direct sums by
[det-ind-heart-filtered-colimits]); hence it is abelian and the inclusion is exact. Every colimit is a
cokernel of a map between direct sums; direct sums and cokernels are computed in
$\Mod(X_{\mathrm{proét}},\Lambda)$ by [det-ind-heart-filtered-colimits] and
[det-ind-heart-kernels-cokernels], so all colimits exist and are computed there. Filtered colimits are
exact in $\Mod(X_{\mathrm{proét}},\Lambda)$, hence in $\IndCons(X,\Lambda)$.

*Generator.* Let $G=\bigoplus_{C}C$ over a set of representatives of $\Cons(X,\Lambda)$ (part (2) of
[sk-lem-coefficient-heart]). If $g\colon B\to B'$ is nonzero, then by
[det-ind-heart-canonical-presentation] some $c\colon C\to B$ with $C$ constructible has $gc\neq0$, so
$\Hom(G,-)$ detects nonzero maps. Thus $G$ is a generator, and the category is Grothendieck.
(Closure under extensions, [det-ind-heart-extensions], is part of the proposition and is used in the
derived statement [sk-cor-ambient-ind-derived].)
