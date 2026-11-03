+++
kind  = "proof"
of = "det-def-sfb-module-pushforward-pullback"
uses = ["def-sfb-module-lower-star", "def-sfb-module-upper-star", "def-sfb-module-upper-lower-adjunction", "def-sfb-module-lower-star-comp", "lem-sfb-pushforward-comp-monoidal", "lem-sfb-eta-comp", "def-sfb-module-upper-star-comp"]
+++
The pushforward and its left exactness are [def-sfb-module-lower-star], the
pullback is [def-sfb-module-upper-star], and the adjunction $f^*\dashv f_*$ is
[def-sfb-module-upper-lower-adjunction]. The composition isomorphism of
pushforwards is [def-sfb-module-lower-star-comp]; it needs that the composition
isomorphism of pushforwards of abelian sheaves is monoidal
([lem-sfb-pushforward-comp-monoidal]) and that $\eta$ is compatible with
composition ([lem-sfb-eta-comp]). The composition isomorphism of
pullbacks is [def-sfb-module-upper-star-comp].
