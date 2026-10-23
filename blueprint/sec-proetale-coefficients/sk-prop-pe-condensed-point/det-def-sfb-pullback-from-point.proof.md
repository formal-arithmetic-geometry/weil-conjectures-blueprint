+++
kind  = "proof"
of = "det-def-sfb-pullback-from-point"
uses = ["lem-sfb-lc-weakly-etale", "def-sfb-profinite-to-proetale", "lem-sfb-profinite-to-proetale-finite-limits", "lem-sfb-profinite-to-proetale-cover-preserving", "lem-sfb-profinite-to-proetale-continuous", "def-sfb-profinite-test-objects", "def-sfb-point-lower-star", "lem-sfb-point-lan-exists", "def-sfb-point-upper-star", "def-sfb-point-adjunction", "lem-sfb-point-upper-star-unit", "lem-sfb-point-upper-star-tensor", "lem-sfb-point-upper-star-braided", "def-sfb-upper-star-from-point", "lem-sfb-upper-star-from-point-left-adjoint", "def-sfb-finite-lower-star"]
+++
For part 1, [lem-sfb-lc-weakly-etale] shows that
$\Spec LC(S,\Z)\to\Spec\Z$ is weakly étale. [def-sfb-profinite-to-proetale]
constructs the functor $u$. [lem-sfb-profinite-to-proetale-finite-limits] and
[lem-sfb-profinite-to-proetale-cover-preserving] give the exactness and
covering properties, and continuity follows by
[lem-sfb-profinite-to-proetale-continuous].

Part 2 is [def-sfb-profinite-test-objects].

For part 3, $p_*$ is [def-sfb-point-lower-star]. The left Kan extension exists
by [lem-sfb-point-lan-exists], so $p^*$ is defined
([def-sfb-point-upper-star]), and the adjunction is [def-sfb-point-adjunction].
Since $p_*$ is lax monoidal, $p^*$ is oplax monoidal. Its oplax structure maps
are invertible by [lem-sfb-point-upper-star-unit] and
[lem-sfb-point-upper-star-tensor], so $p^*$ is strong monoidal. It is braided
by [lem-sfb-point-upper-star-braided].

For part 4, the functor $p_X^*=\pi_X^*\circ p^*$ and its strong monoidal
braided structure are [def-sfb-upper-star-from-point]. It is a left adjoint,
with right adjoint $p_*\circ\pi_{X*}$, by
[lem-sfb-upper-star-from-point-left-adjoint]. On sections over $S$,
$$
(p_*\pi_{X*}G)(S)=(\pi_{X*}G)(\Spec LC(S,\Z))
=G\bigl(\Spec LC(S,\Z)\times_{\Spec\Z}X\bigr)=G(X[S]),
$$
because $\pi_{X*}$ is restriction along base change
([def-sfb-finite-lower-star]).
