+++
kind  = "proof"
of    = "prop-sfb-module-left-derived-upper-star-comp"
uses = ["prop-sfb-module-left-derived-upper-star-levelwise", "sk-prop-sfb-module-pullback-exact"]
+++
All pullbacks of module objects are exact ([sk-prop-sfb-module-pullback-exact]), so
each total left derived functor involved is the levelwise functor
([prop-sfb-module-left-derived-upper-star-levelwise]). An isomorphism of exact
functors $(g\circ f)^*\cong f^*\circ g^*$ ([def-sfb-module-upper-star-comp]) induces
an isomorphism $D((g\circ f)^*)\cong D(f^*\circ g^*)$ of levelwise functors, and
$D(f^*\circ g^*)=D(f^*)\circ D(g^*)$ for levelwise functors. Transporting along the
isomorphisms $L(-)\cong D(-)$ gives
$L(g\circ f)^*\cong L(f^*\circ g^*)\cong Lf^*\circ Lg^*$.
