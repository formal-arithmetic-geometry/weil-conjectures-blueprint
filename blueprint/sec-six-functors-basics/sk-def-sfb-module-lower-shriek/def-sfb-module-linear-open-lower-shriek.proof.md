+++
kind  = "proof"
of    = "def-sfb-module-linear-open-lower-shriek"
uses = ["sk-def-sfb-finite-lower-shriek", "det-prop-sfb-module-category"]
+++
The pullback $j^*_{\Ab}$ is strong monoidal and the projection formula holds
([lem-sfb-open-projection-formula]), so the linearization of
[det-def-sfb-transport] applies to $P=j^{\Ab}_!$ and $S=j^*_{\Ab}$: it produces the
module structure displayed above (associativity and unitality of the action follow
from the coherence of the projection isomorphism), and it lifts the adjunction
$j^{\Ab}_!\dashv j^*_{\Ab}$ to $j^{\mathrm{lin}}_!\dashv
\operatorname{mapMod}(j^*_{\Ab})$. The extension by zero $j^{\Ab}_!$ is exact
([sk-def-sfb-finite-lower-shriek]), and finite limits and colimits of module objects
are computed on underlying sheaves ([det-prop-sfb-module-category]), so
$j^{\mathrm{lin}}_!$ is exact.
