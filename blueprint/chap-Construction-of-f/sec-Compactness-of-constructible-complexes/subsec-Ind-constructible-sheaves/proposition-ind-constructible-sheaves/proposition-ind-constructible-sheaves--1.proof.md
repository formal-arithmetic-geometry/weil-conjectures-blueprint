+++
kind = "proof"
of = "proposition-ind-constructible-sheaves--1"
order = 453003
uses = ["lemma-continuity-ext-out-constructible-complex", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--4", "lemma-constructible-sheaves--6", "lemma-continuity-ext-out-constructible-complex--1"]
+++
*Finite presentation.* Constructible sheaves are finitely
presented in $\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$. Indeed,
Lemma [lemma-continuity-ext-out-constructible-complex] in degree zero
shows that $\Hom(C,-)$ commutes with filtered colimits for $C$ constructible.
By Lemma [lemma-constructible-sheaves](1),(2), the
category $\Cons(X,\Lambda)$ is essentially small, abelian, and closed
under extensions. We fix a small skeleton. Part (1) follows from finite
presentation.

*Full faithfulness.* For filtered diagrams $(C_\alpha)$ and
$(D_\beta)$ of constructible sheaves, finite presentation implies

$$
\Hom(\varinjlim_\alpha C_\alpha,\varinjlim_\beta D_\beta)
=\varprojlim_\alpha\varinjlim_\beta\Hom_{\Cons(X,\Lambda)}(C_\alpha,D_\beta),
$$

which is the Hom set in the ind-category.

*Source:* the proof of Proposition [proposition-ind-constructible-sheaves].
