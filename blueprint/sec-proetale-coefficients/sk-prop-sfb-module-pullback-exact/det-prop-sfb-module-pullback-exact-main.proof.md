+++
kind = "proof"
of = "det-prop-sfb-module-pullback-exact-main"
uses = ["det-def-sfb-sheaf-tensor-closed", "lem-sfb-finite-upper-star-braided", "def-sfb-finite-upper-star-monoidal", "det-def-sfb-ring-object-transport"]
+++
**Setting.** The categories $\Sh(X_{\mathrm{proét}},\Ab)$ and $\Sh(Y_{\mathrm{proét}},\Ab)$ are abelian
and closed symmetric monoidal, with $\otimes$ additive and right exact in each variable
([det-def-sfb-sheaf-tensor-closed]); they have all limits and colimits. The pullback
$f^*_{\Ab}$ is additive, exact ([lem-sfb-finite-upper-star-exact]) and strong monoidal
([def-sfb-finite-upper-star-monoidal]) and braided ([lem-sfb-finite-upper-star-braided]). So
$f^*\Lambda_Y$ is a commutative ring object of $\Sh(X_{\mathrm{proét}},\Ab)$
([det-def-sfb-ring-object-transport]), and $\Lambda_Y\otimes-$, $f^*\Lambda_Y\otimes-$,
$\Lambda_X\otimes-$ are right exact.

**Transport.** $\operatorname{mapMod}(f^*_{\Ab})$ commutes with the forgetful functors
([def-sfb-modobj-transport]): $U\circ\operatorname{mapMod}(f^*_{\Ab})=f^*_{\Ab}\circ U$. By
[det-prop-sfb-module-pullback-exact-lifted] with $F=f^*_{\Ab}$, it is additive and exact.

**Extension of scalars.** The coefficient morphism $\alpha_f\colon f^*\Lambda_Y\to\Lambda_X$ is an
isomorphism of ring objects ([lem-sfb-alpha-iso]). The hypotheses of
[def-sfb-modobj-extension-along-iso] hold for $\Sh(X_{\mathrm{proét}},\Ab)$ (braided, closed, with
equalizers and coequalizers, $\otimes$ preserving colimits in each variable, $f^*\Lambda_Y$
commutative), so $\operatorname{Ext}_{\alpha_f}\cong\operatorname{Res}_{\alpha_f^{-1}}$. Restriction of
scalars is the identity on underlying objects and morphisms, so
$U\circ\operatorname{Res}_{\alpha_f^{-1}}=U$, and [det-prop-sfb-module-pullback-exact-lifted] with
$F=\mathrm{Id}$ shows that $\operatorname{Res}_{\alpha_f^{-1}}$ is additive and exact. A functor
isomorphic to an additive exact functor is additive and exact, so $\operatorname{Ext}_{\alpha_f}$ is.

**Conclusion.** $f^*$ is a composite of two additive exact functors between abelian categories,
hence additive and exact, and so it preserves finite limits and finite colimits.
