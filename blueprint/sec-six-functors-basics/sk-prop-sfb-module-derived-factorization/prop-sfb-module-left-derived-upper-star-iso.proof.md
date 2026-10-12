+++
kind  = "proof"
of    = "prop-sfb-module-left-derived-upper-star-iso"
uses = ["sk-def-sfb-derived-categories", "sk-def-sfb-finite-pushforward-pullback", "sk-prop-sfb-module-category"]
+++
By definition $f^*=\operatorname{Ext}_{\alpha_f}\circ\operatorname{mapMod}(f^*_{\Ab})$
([def-sfb-module-upper-star]). The functor $F=\operatorname{mapMod}(f^*_{\Ab})$ is
exact, since $f^*_{\Ab}$ is ([sk-def-sfb-finite-pushforward-pullback]) and finite limits and
colimits of module objects are computed on underlying sheaves
([sk-prop-sfb-module-category]), and it sends K-flat complexes to K-flat
complexes ([lem-sfb-module-mapmod-pullback-kflat]). Let $G=\operatorname{Ext}_{\alpha_f}$,
which preserves quasi-isomorphisms between K-flat complexes
([sk-def-sfb-derived-extension-of-scalars]). Then $LG\circ D(F)$, with the counit
assembled from the counit of $LG$, is a left derived functor of $G\circ F$: by the
K-flat left derivability structure ([sk-def-sfb-derived-categories]) it suffices that
its counit is an isomorphism on every K-flat complex $P$, and indeed $D(F)$ is
computed levelwise and the counit of $LG$ is an isomorphism on the K-flat complex
$F(P)$. Uniqueness of left derived functors gives
$L(G\circ F)\cong LG\circ D(F)$.
