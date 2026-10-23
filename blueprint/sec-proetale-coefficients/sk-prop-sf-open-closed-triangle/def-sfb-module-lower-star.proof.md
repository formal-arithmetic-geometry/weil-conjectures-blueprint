+++
kind  = "proof"
of    = "def-sfb-module-lower-star"
uses = ["det-prop-sfb-module-category", "def-sfb-finite-upper-lower-star-adjunction"]
+++
Both factors are additive. The pushforward $f^{\Ab}_*$ is left exact, being a right
adjoint ([def-sfb-finite-upper-lower-star-adjunction]). Finite limits of module objects
are computed on the underlying sheaves ([det-prop-sfb-module-category]), so
$\operatorname{mapMod}(f^{\Ab}_*)$ is left exact, and restriction of scalars is exact
([det-def-sfb-change-of-scalars]). Hence $f_*$ is left exact.
