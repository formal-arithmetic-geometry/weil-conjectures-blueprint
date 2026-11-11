+++
kind = "proof"
of = "lemma-degree-zero-calculation"
order = 668
uses = ["definition-small-pro-etale-site", "lemma-finite-direct-images"]
+++
Both sides are sheaves on $Y'_{\acute{e}t}$, so it is enough to compare their
sections on a family of étale objects $U\to Y'$ that cover $Y'$. We
choose these objects so that both sections can be computed from sections of
$F_{\acute{e}t}$ over a single scheme $V\times_YX$.

Such objects exist locally on every étale $U\to Y'$: by
[Stacks, [0EY5](https://stacks.math.columbia.edu/tag/0EY5)], locally on $U$ there is a factorization $U\to V\to Y$ in
which $V\to Y$ is étale and $U\to V$ is flat and qcqs with geometrically
connected fibres. Pullback along such a map does not change the sections
of the pullback of an étale sheaf [Stacks, [0A3H](https://stacks.math.columbia.edu/tag/0A3H), [0EZX](https://stacks.math.columbia.edu/tag/0EZX)], and we use this
twice. Applying it to
$U\to V$, we compute the left side from $(f_*F_{\acute{e}t})(V)$; applying it to
the base change $U\times_YX\to V\times_YX$, which again has geometrically
connected fibres, we compute the right side. On these objects we
therefore have

$$
(g^{-1}f_*F_{\acute{e}t})(U)
=F_{\acute{e}t}(V\times_Y X)
=(f'_*g'^{-1}F_{\acute{e}t})(U),
$$

and the base change map is bijective on sections over every such $U$,
because these equalities are induced by it. As these $U$ cover $Y'$, the
lemma follows by descent, as in the argument in degree zero of
[Stacks, [0EYS](https://stacks.math.columbia.edu/tag/0EYS)].
