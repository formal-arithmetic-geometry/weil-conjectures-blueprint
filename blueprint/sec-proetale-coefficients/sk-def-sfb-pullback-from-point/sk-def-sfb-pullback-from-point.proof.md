+++
kind  = "proof"
of    = "sk-def-sfb-pullback-from-point"
+++
Part 1 combines four children. [lem-sfb-lc-weakly-etale] shows that
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

Part 4 is [def-sfb-upper-star-from-point] together with
[lem-sfb-upper-star-from-point-left-adjoint]. It remains to identify the right
adjoint. The right adjoint of $p_X^*=\pi_X^*\circ p^*$ is $p_*\circ\pi_{X*}$.
On sections over $S$,
$$
(p_*\pi_{X*}G)(S)=(\pi_{X*}G)(\Spec LC(S,\Z))
=G\bigl(\Spec LC(S,\Z)\times_{\Spec\Z}X\bigr)=G(X[S]),
$$
because $\pi_{X*}$ is restriction along base change
([sk-def-sfb-finite-pushforward-pullback]).
