+++
kind  = "proof"
of    = "sk-prop-sfb-module-derived-factorization"
uses = ["sk-prop-sfb-module-pullback-exact", "sk-def-sfb-finite-pushforward-pullback", "sk-prop-sfb-module-category"]
+++
(1) is [prop-sfb-module-right-derived-lower-star-iso]. (2) is
[lem-sfb-module-mapmod-pullback-kflat] together with
[prop-sfb-module-left-derived-upper-star-iso]. (3) is
[prop-sfb-module-left-derived-upper-star-levelwise], which uses the exactness of
$f^*$ ([sk-prop-sfb-module-pullback-exact]). (4) is
[prop-sfb-module-left-derived-upper-star-comp]. (5) is
[prop-sfb-module-derived-pushpull-adjunction-plus]. (6) is
[prop-sfb-module-derived-open-adjunction] and
[prop-sfb-module-derived-open-adjunction-plus].
