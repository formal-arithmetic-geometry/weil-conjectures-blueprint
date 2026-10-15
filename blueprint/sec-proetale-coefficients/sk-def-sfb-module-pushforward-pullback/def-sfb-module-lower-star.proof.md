+++
kind  = "proof"
of    = "def-sfb-module-lower-star"
uses = ["sk-prop-sfb-module-category"]
+++
Both factors are additive. The pushforward $f^{\Ab}_*$ is left exact, being a right
adjoint ([sk-def-sfb-finite-pushforward-pullback]). Finite limits of module objects
are computed on the underlying sheaves ([sk-prop-sfb-module-category]), so
$\operatorname{mapMod}(f^{\Ab}_*)$ is left exact, and restriction of scalars is exact
([sk-def-sfb-change-of-scalars]). Hence $f_*$ is left exact.
