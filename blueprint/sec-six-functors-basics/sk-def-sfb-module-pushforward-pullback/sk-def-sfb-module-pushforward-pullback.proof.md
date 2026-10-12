+++
kind  = "proof"
of    = "sk-def-sfb-module-pushforward-pullback"
uses = ["sk-def-sfb-sheaf-tensor", "sk-prop-sfb-cartesian-coefficients", "sk-prop-sfb-module-category"]
+++
The pushforward and its left exactness are [def-sfb-module-lower-star], the
pullback is [def-sfb-module-upper-star], and the adjunction $f^*\dashv f_*$ is
[def-sfb-module-upper-lower-adjunction]. The composition isomorphism of
pushforwards is [def-sfb-module-lower-star-comp]; it needs that the composition
isomorphism of pushforwards of abelian sheaves is monoidal
([lem-sfb-pushforward-comp-monoidal]) and that $\eta$ is compatible with
composition ([sk-prop-sfb-cartesian-coefficients]). The composition isomorphism of
pullbacks is [def-sfb-module-upper-star-comp].
