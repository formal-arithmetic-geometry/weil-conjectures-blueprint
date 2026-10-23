+++
id = "sec-six-functors-basics"
kind = "section"
title = "Six Functors: Basic Constructions"
order = 2118
uses = ["sec-abelian-varieties", "sec-curve-estimates", "sec-nagata-compactification", "sec-picard-framework", "sec-proetale-coefficients", "sec-proper-base-change", "sec-smooth-base-change", "sk-def-exchange", "sk-def-pbc-conventions", "sk-lem-curve-normalization", "sk-lem-pbc-finite", "sk-prop-curve-affine-kummer", "sk-thm-br", "sk-thm-curveestimate"]
+++
**Content.** This section sets up the pro-étale derived categories and the six
functors on which the later six-functor sections rest, following
Bhatt–Scholze, *The pro-étale topology for schemes*, §6.8. Two layers
coexist ([rem-sfb-coefficient-layers]). In layer (A), sheaves on
$X_{\mathrm{proét}}$ take values in a fixed closed symmetric monoidal
Grothendieck abelian category $\mathcal A$, for instance $\mathcal A=\Mod_R$ for a
finite ring $R$. Layer (B) handles the non-finite coefficients
$\mathbb Z_\ell,\mathbb Q_\ell,\cO_E,E,\Qlb$. A commutative condensed ring
$\Lambda$ ([det-def-sfb-condensed-ring], [det-def-sfb-qlbar-condensed]) is pulled back from the point to a
ring object $\Lambda_X=p_X^*\Lambda$ of $\Sh(X_{\mathrm{proét}},\Ab)$
([det-def-sfb-pulled-back-coefficients]). Sheaves are module objects over
$\Lambda_X$ ([det-def-sfb-module-objects]). Since $f^*\Lambda_Y\cong\Lambda_X$
for every $f$ ([sk-prop-sfb-cartesian-coefficients]), the functors of layer (B)
come from those of layer (A) with $\mathcal A=\Ab$, by transporting module
structures and changing scalars ([det-def-sfb-transport],
[det-def-sfb-change-of-scalars]).

The route is as follows:
- sheaf tensor product and ring objects;
- condensed coefficient rings and their pullback from the point;
- module objects and change of scalars;
- derived categories, the comparison of $E$- with $\cO_E$-coefficients
  ([sk-thm-sfb-rationalization-comparison]), and constructibility
  ([det-def-sfb-bounded-constructible]);
- the six functors of layer (A), then of layer (B);
- change of coefficients, ending with
  $D_{\mathrm{cons}}(X,\Qlb)=2\text{-}\colim_E D_{\mathrm{cons}}(X,E)$
  ([sk-thm-sfb-qlbar-two-colimit]);
- the restrictions of the six functors to bounded constructible complexes over a field
  ([sk-def-sfb-dc-restricted-functors], [sk-def-sfb-dc-lower-shriek],
  [sk-def-sfb-dc-upper-shriek]);
- the base change theorems.

| Functor | Layer A: $\Sh(X_{\mathrm{proét}},\mathcal A)$ | Layer B: $\Mod_{\Lambda_X}$, $\Lambda_X=p_X^*\Lambda$ |
|---|---|---|
| coefficients | fixed $\mathcal A$ | condensed $\Lambda$ pulled back; $\alpha_f\colon f^*\Lambda_Y\cong\Lambda_X$ for all $f$ |
| $f_*$ | restriction along base change | $\operatorname{Res}_{\eta_f}\circ\operatorname{mapMod}(f_*)$ |
| $f^*$ | $\operatorname{sheafify}\circ\operatorname{Lan}$, exact, monoidal | $\operatorname{Ext}_{\alpha_f}\circ\operatorname{mapMod}(f^*)$, exact |
| $j_!$ ($j$ open) | $\operatorname{sheafify}\circ\operatorname{Lan}$ along localization | linearized $j_!$ (projection formula) $\circ\operatorname{Res}_{\alpha_j}$ |
| $f_!$ | $g_*\circ i_!$ for a chosen compactification | $g_*\circ i_!$ |
| $Rf_*$, $Lf^*$ | $R(f_*)$, $L(f^*)\cong D(f^*)$ | derived functors of the composites |
| $Rf_!$ | $R(g_*)\circ D(i_!)$ | the same; on $D_{\mathrm{cons}}$ assembled from the restricted $i_!$, $Rg_*$ |
| $Rf^!$ | $D(i^*)\circ Rg^!$ | only on $D_{\mathrm{cons}}$: $i^*\circ Rg^!$, given a right adjoint $Rg^!$ of $Rg_*$ (available for $\cO_E$, $E$, $\Qlb$) |
| $\otimes^{\mathrm L}$, $\RHom$ | K-flat derived $\otimes$, right adjoint | K-flat derived $\otimes_{\Lambda_X}$, right adjoint |
| base change | $\mathrm{BC}$, $\mathrm{Ex}^c_!$ (étale) | $\mathrm{BC}$, $\mathrm{Ex}^c_!$ on $D_{\mathrm{cons}}$ |

**Key theorems.**

- Prop [sk-prop-sfb-cartesian-coefficients] (Cartesian coefficient system):
  $\alpha_f\colon f^*\Lambda_Y\to\Lambda_X$ is an isomorphism for every
  morphism $f$ and every condensed ring $\Lambda$.
- Thm [sk-thm-sfb-proper-base-change] and Thm [sk-thm-sfb-shriek-base-change]
  (base change on $D_{\mathrm{cons}}$ for $\Lambda=\underline E,\underline{\Qlb}$).
- Thm [sk-thm-sfb-qlbar-two-colimit]
  ($D_{\mathrm{cons}}(X,\Qlb)$ is the filtered 2-colimit of the
  $D_{\mathrm{cons}}(X,E)$).

**References.**

- B. Bhatt, P. Scholze, *The pro-étale topology for schemes*, Astérisque 369
  (2015), §6.7–6.8.
