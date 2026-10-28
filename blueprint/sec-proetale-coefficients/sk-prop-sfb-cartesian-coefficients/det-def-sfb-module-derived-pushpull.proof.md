+++
kind  = "proof"
of    = "det-def-sfb-module-derived-pushpull"
uses = ["sk-prop-sf-open-closed-triangle"]
+++
The category $\Mod_{\Lambda_X}$ is a closed symmetric monoidal Grothendieck abelian
category with functorial flat resolutions ([det-prop-sfb-module-category]), so it has
K-injective resolutions, enough injectives and K-flat resolutions, and the right
derived functors $R(f_*)$, $R^+(f_*)$ of the additive functor $f_*$ exist
([det-def-sfb-derived-categories]). The K-flat left derived functor $L(f^*)$ exists
because $f^*$ sends quasi-isomorphisms between K-flat complexes to
quasi-isomorphisms ([lem-sfb-module-upper-star-kflat-quasi-iso], which uses
[det-prop-sfb-module-pullback-exact-main]). The derived adjunction is
[def-sfb-module-derived-pushpull-adjunction].
