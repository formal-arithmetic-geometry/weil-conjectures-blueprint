+++
kind  = "proof"
of    = "lem-sfb-module-mapmod-pullback-kflat"
+++
The functor $\operatorname{mapMod}(f^*_{\Ab})$ is the pullback of modules along the
morphism of ringed topoi $(X_{\mathrm{proét}},f^*\Lambda_Y)\to
(Y_{\mathrm{proét}},\Lambda_Y)$ whose inverse image is $f^*_{\Ab}$. Since $f^*_{\Ab}$
is exact, strong monoidal and commutes with colimits
([sk-def-sfb-finite-pushforward-pullback]), it commutes with the relative tensor
product of complexes of module objects (a coequalizer of tensor products, followed by
totalization, [det-prop-sfb-module-category]) and preserves acyclicity. That the
pullback of a K-flat complex along a morphism of ringed topoi is K-flat is then the
general statement of the Stacks Project (Cohomology on Sites, section on K-flat
complexes): one tests $f^*P\otimes_{f^*\Lambda_Y}N$ against an arbitrary acyclic
complex $N$ of $f^*\Lambda_Y$-modules on $X$, not only against pulled-back ones, by
reducing to the K-flat complexes built from the functorial flat resolutions
$\Lambda_Y\otimes Q$ of [det-prop-sfb-module-category], whose pullbacks
$f^*\Lambda_Y\otimes f^*_{\Ab}Q$ are again of this form with $f^*_{\Ab}Q$ flat.
