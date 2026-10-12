+++
kind  = "proof"
of    = "prop-sfb-module-derived-pushpull-adjunction-plus"
uses = ["def-sfb-module-derived-pushpull-adjunction", "prop-sfb-module-left-derived-upper-star-levelwise"]
+++
Start from the unbounded adjunction $Lf^*\dashv Rf_*$
([def-sfb-module-derived-pushpull-adjunction]) and replace $Lf^*$ by the isomorphic
levelwise functor $D(f^*)$ ([prop-sfb-module-left-derived-upper-star-levelwise]). The
inclusions $D^+\subseteq D$ are fully faithful; $D(f^*)$ restricted to $D^+$ is
$D^+(f^*)$ (an exact functor preserves bounded below complexes), and $Rf_*$
restricted to $D^+$ is $R^+f_*$ (on a bounded below complex both are computed on a
bounded below injective resolution, [sk-def-sfb-derived-categories]). An adjunction
between functors that restrict to full subcategories restricts to an adjunction
between the restrictions.
