+++
kind = "proof"
of = "det-prop-sfb-module-pullback-exact-main"
uses = ["det-def-sfb-sheaf-tensor-closed", "lem-sfb-finite-upper-star-braided", "def-sfb-finite-upper-star-monoidal", "det-def-sfb-ring-object-transport", "def-sfb-modobj-restriction-equivalence"]
+++
**Setting.** The categories $\Sh(X_{\mathrm{proét}},\Ab)$ and $\Sh(Y_{\mathrm{proét}},\Ab)$ are abelian
and closed symmetric monoidal, with $\otimes$ additive and right exact in each variable
([det-def-sfb-sheaf-tensor-closed]); they have all limits and colimits. The pullback
$f^*_{\Ab}$ is additive, exact ([lem-sfb-finite-upper-star-exact]) and strong monoidal
([def-sfb-finite-upper-star-monoidal]) and braided ([lem-sfb-finite-upper-star-braided]). So
$f^*\Lambda_Y$ is a commutative ring object of $\Sh(X_{\mathrm{proét}},\Ab)$
([det-def-sfb-ring-object-transport]), and $\Lambda_Y\otimes-$, $f^*\Lambda_Y\otimes-$,
$\Lambda_X\otimes-$ are right exact.

**Transport.** $\operatorname{mapMod}(f^*_{\Ab})$ is the transport of module objects along the
lax (indeed strong) monoidal functor $f^*_{\Ab}$ ([def-sfb-modobj-transport]). Since $f^*_{\Ab}$
preserves finite limits and finite colimits, so does $\operatorname{mapMod}(f^*_{\Ab})$
([det-prop-sfb-module-pullback-exact-lifted] with $F=f^*_{\Ab}$ and $\mathcal R=\Lambda_Y$).

**Extension of scalars.** The coefficient morphism $\alpha_f\colon f^*\Lambda_Y\to\Lambda_X$ is an
isomorphism of ring objects ([lem-sfb-alpha-iso]). The hypotheses of
[def-sfb-modobj-extension-along-iso] hold for $\Sh(X_{\mathrm{proét}},\Ab)$ (braided, closed, with
equalizers and coequalizers, $\otimes$ preserving colimits in each variable, $f^*\Lambda_Y$
commutative), so $\operatorname{Ext}_{\alpha_f}\cong\operatorname{Res}_{\alpha_f^{-1}}$. Restriction of
scalars along an isomorphism of ring objects is an equivalence of categories, with inverse the
restriction of scalars along the inverse isomorphism ([def-sfb-modobj-restriction-equivalence]); an equivalence preserves all limits and
colimits, and so does a functor isomorphic to it. Hence $\operatorname{Ext}_{\alpha_f}$ preserves
finite limits and finite colimits.

**Conclusion.** $f^*$ is a composite of two functors between abelian categories that preserve
finite limits and finite colimits, so it preserves them, hence is exact. A functor between
preadditive categories with finite biproducts that preserves finite products is additive, so
$f^*$ is additive.
