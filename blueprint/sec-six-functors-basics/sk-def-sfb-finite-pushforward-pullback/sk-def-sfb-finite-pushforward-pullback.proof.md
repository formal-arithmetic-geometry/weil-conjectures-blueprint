+++
kind  = "proof"
of    = "sk-def-sfb-finite-pushforward-pullback"
+++
Base change is continuous and $g_*G$ is a sheaf by [def-sfb-finite-lower-star]; the
Kan extension and the sheafification defining $g^*$ exist by
[def-sfb-finite-upper-star]. Base change exists for every morphism $g$, whereas the
localization functor $(W\to Z)\mapsto(W\to Z\to Y)$ is defined only when $g$ is weakly
étale. Defining both functors along base change is what makes them available for the
proper morphism of a compactification, which in general is not weakly étale.

1. is [def-sfb-finite-upper-lower-star-adjunction] and 2. is
[lem-sfb-finite-upper-star-exact]. In 3., $(\mathrm{id}_Y)_*G=G(-\times_YY)$, and the canonical isomorphisms
$V\times_YY\cong V$ give $(\mathrm{id}_Y)_*\cong\mathrm{id}$. The two composition
isomorphisms of 3. are [def-sfb-finite-lower-star-comp] and
[def-sfb-finite-upper-star-comp].

For 4., $g_*$ is lax symmetric monoidal by [def-sfb-finite-lower-star-lax-monoidal].
The mate of this structure is an oplax monoidal structure on $g^*$, whose structure maps
are isomorphisms by [lem-sfb-finite-upper-star-unit] and
[lem-sfb-finite-upper-star-tensor]. This gives the strong monoidal structure
[def-sfb-finite-upper-star-monoidal], which is symmetric by
[lem-sfb-finite-upper-star-braided]. The adjunction is monoidal by
[lem-sfb-finite-monoidal-adjunction].
