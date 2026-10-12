+++
kind  = "proof"
of    = "sk-prop-sfb-module-pullback-exact"
uses = ["sk-def-sfb-finite-pushforward-pullback", "sk-prop-sfb-module-category", "sk-def-sfb-transport", "sk-def-sfb-change-of-scalars", "sk-prop-sfb-cartesian-coefficients"]
+++
Right exactness holds because $f^*$ is a left adjoint
([sk-def-sfb-module-pushforward-pullback]).

For left exactness write $f^*=\operatorname{Ext}_{\alpha_f}\circ
\operatorname{mapMod}(f^*_{\Ab})$. The pullback $f^*_{\Ab}$ of abelian sheaves is
exact ([sk-def-sfb-finite-pushforward-pullback]). The forgetful functors from module
objects to sheaves are exact and faithful, and finite limits and colimits of module
objects are computed on the underlying sheaves ([sk-prop-sfb-module-category]); since
the underlying sheaf of $\operatorname{mapMod}(f^*_{\Ab})M$ is $f^*_{\Ab}M$
([sk-def-sfb-transport]), the functor $\operatorname{mapMod}(f^*_{\Ab})$ is exact. The
coefficient morphism $\alpha_f$ is an isomorphism
([sk-prop-sfb-cartesian-coefficients]), so extension of scalars along it is
isomorphic to restriction of scalars along its inverse,
$\operatorname{Ext}_{\alpha_f}\cong\operatorname{Res}_{\alpha_f^{-1}}$
([sk-def-sfb-change-of-scalars]), which is exact. Hence $f^*$ is isomorphic to a
composite of exact functors and is exact.
