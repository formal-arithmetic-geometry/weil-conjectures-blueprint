+++
id = "rem-sfb-coefficient-layers"
kind = "remark"
title = "Two layers of coefficients"
order = 1451
+++
The construction follows Bhatt–Scholze, *The pro-étale topology for schemes*,
§6.8, for $\ell$-adic coefficients. Throughout, $X_{\mathrm{proét}}$ is the small
pro-étale site of a scheme $X$ ([def-weil-pbc-proetale-site]): its coverings are the
jointly surjective fpqc families of weakly étale maps, so, unlike on the étale site,
joint surjectivity alone does not make a family a covering. Two layers of coefficients
coexist, used for different coefficient rings.

- **(A) Finite coefficients: a fixed coefficient category.** Sheaves on
  $X_{\mathrm{proét}}$ take values in a fixed closed symmetric monoidal Grothendieck
  abelian category $\mathcal A$, typically $\mathcal A=\Mod_R$ for a finite ring $R$
  such as $\mathbf Z/\ell^n$ ([sk-def-sfb-sheaf-tensor],
  [sk-def-sfb-finite-pushforward-pullback]).
- **(B) Non-finite coefficients: module objects over a pulled-back condensed ring.**
  A commutative condensed ring $\Lambda$, i.e. a commutative ring object of abelian
  sheaves on the pro-étale site of a point, is fixed once and for all, e.g.
  $\Lambda=\underline{\mathbf Z}_\ell,\underline{\mathbf Q}_\ell,\underline{\cO}_E,
  \underline E,\underline{\Qlb}$ ([sk-def-sfb-condensed-ring],
  [sk-def-sfb-qlbar-condensed]). It is pulled back to $\Lambda_X:=p_X^*\Lambda$ on every
  $X_{\mathrm{proét}}$ ([sk-def-sfb-pulled-back-coefficients]). Sheaves are module
  objects over the ring object $\Lambda_X$ of $\Sh(X_{\mathrm{proét}},\Ab)$
  ([sk-def-sfb-module-objects]), and the six functors are obtained from those of layer
  (A) with $\mathcal A=\Ab$ by transporting module structures and changing scalars
  ([sk-def-sfb-transport], [sk-def-sfb-change-of-scalars]). One construction serves all
  these coefficient rings: there is no separate development for $\underline T=C(-,T)$
  and for $\underline{\Qlb}$.

The module-object setup is used only for the coefficients
$\mathbf Z_\ell,\mathbf Q_\ell,E,\cO_E,\Qlb$; finite coefficients stay in layer (A).

The reason for the split is the following. For a discrete ring $R$, the sheaf
$C(-,R)$ is the constant sheaf $\underline R$, a sheaf of $\underline R$-modules is the
same as a $\Mod_R$-valued sheaf, and $f^*\underline R_Y=\underline R_X$; so the fixed
coefficient formalism suffices. For a non-discrete topological ring $T$ this breaks
down: an $\ell$-adic sheaf is a module over $\underline{\mathbf Z}_{\ell,X}$, which is
*not* the constant sheaf with value $\mathbf Z_\ell$ (the two differ on w-contractible
objects), and it is not a sheaf with values in a fixed category of modules. So the
coefficients cannot be absorbed into a fixed $\mathcal A$: they form a ring object that
varies with $X$, and they are made coherent in $X$ by pulling them back from the point.
Defining them on the point has a further advantage: on the point, the presheaf of
continuous maps with values in a finite subextension of $\Qlb/\mathbf Q_\ell$ is
already a sheaf ([sk-def-sfb-qlbar-condensed]), whereas the analogous presheaf on a
general $X_{\mathrm{proét}}$ is not.
