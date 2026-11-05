+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--1"
order = 562003
+++
*Local charts.* The computation of $f^!$ on a chart also
proves (1). Zariski locally on $X$ and $S$, a smooth morphism
is an étale map to affine space followed by the projection
[Stacks, [054L](https://stacks.math.columbia.edu/tag/054L)]. Thus every point of $X$
has an affine open neighbourhood $u:U\hookrightarrow X$ mapping into
an affine open $v:V\hookrightarrow S$, together with a separated
étale map $e:U\to\mathbf A^d_V$ such that $fu=vp_de$, where
$p_d:\mathbf A^d_V\to V$ is the projection. By
Lemma [lemma-affine-space-etale-localization] and uniqueness of right adjoints,
we have

$$
u^*f^!N=e^*p_d^*v^*N(d)[2d],\qquad
u^*\omega_f=\Lambda_U(d)[2d].
$$

In particular, $\omega_f$ has a single nonzero cohomology sheaf, in
degree $-2d$, which is locally free of rank one. This proves (1), because
the counit on $U$ is the composite of the étale counit for $e$ and the
counit for $p_d$. The first of these is the sum over the fibres.

*Source:* the proof of Proposition [proposition-exceptional-inverse-image-smooth-morphism].
