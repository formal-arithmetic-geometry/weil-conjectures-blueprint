+++
kind = "proof"
of = "sk-prop-deg0"
+++
By [Stacks, Tag 0EY5](https://stacks.math.columbia.edu/tag/0EY5), locally on an étale object $U\to Y'$ there is a
factorization $U\to V\to Y$ in which $V\to Y$ is étale and $U\to V$
is flat and qcqs with geometrically connected fibres. Pullback along
such a map does not change the sections of the pullback of an étale sheaf
[Stacks, Tag 0A3H](https://stacks.math.columbia.edu/tag/0A3H), [Stacks, Tag 0EZX](https://stacks.math.columbia.edu/tag/0EZX). We apply this twice: to $U\to V$, which computes the
left side from $(f_*F_{\acute{e}t})(V)$, and to its base change
$U\times_YX\to V\times_YX$, which again has geometrically connected fibres
and computes the right side. Hence on these objects

$$
(g^{-1}f_*F_{\acute{e}t})(U)
=F_{\acute{e}t}(V\times_Y X)
=(f'_*g'^{-1}F_{\acute{e}t})(U).
$$

Since these equalities are induced by the base change map, the lemma follows
by descent (this is the argument in degree zero of [Stacks, Tag 0EYS](https://stacks.math.columbia.edu/tag/0EYS)).
