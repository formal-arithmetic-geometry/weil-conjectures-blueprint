+++
kind = "proof"
of = "det-pe-classical-sheaves-image"
+++
*(1)$\Rightarrow$(2).* Classicality is invariant under isomorphism, so let
$G=\nu_X^*F$. Let $U=\varprojlim_iU_i$ be a pro-étale affine presentation. By
the affine evaluation formula of [sk-prop-pe-comparison-morphism] (proved in
detail in [lem-weil-pbc-comparison-sections]) we have
$(\nu_X^*F)(U)=\varinjlim_iF(U_i)$, and $(\nu_X^*F)(U_i)=F(U_i)$ for the étale
objects $U_i$. The identification is induced by the restriction maps of
$\nu_X^*F$ along $U\to U_i$, so it is precisely the continuity map
$c_{G,U}$, which is therefore bijective.

*(2)$\Rightarrow$(3).* Let $U=\varprojlim_iU_i$ be a pro-étale affine
presentation. By the section formula,
$(\nu_X^*\nu_{X,*}G)(U)=\varinjlim_i(\nu_{X,*}G)(U_i)=\varinjlim_iG(U_i)$. The
counit is adjoint to the identity of $\nu_{X,*}G$; in the explicit adjunction of
[lem-weil-pbc-comparison-sections] it sends the class of $s\in G(U_i)$ to its
restriction $s|_U\in G(U)$. Thus $\varepsilon_G(U)=c_{G,U}$, a bijection by
assumption. The affine ind-étale objects form a basis of $X_{\Proet}$: every
object, and every fibre product of two of them over a third, has a covering by
affine ind-étale objects ([lem-weil-pbc-ind-etale-basis]). A morphism of sheaves
which is bijective on every object of such a basis is an isomorphism (injectivity
and gluing are both tested on basis coverings), so $\varepsilon_G$ is an
isomorphism.

*(3)$\Rightarrow$(1).* Take $F=\nu_{X,*}G$.
