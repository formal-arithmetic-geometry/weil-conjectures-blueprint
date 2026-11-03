+++
kind = "proof"
of = "sk-prop-cohsm"
uses = ["sk-prop-geo-p1-adjunction", "sk-lem-geo-affine-local"]
+++
The maps
(7.11) and (7.12) are defined globally as adjoint transposes, and being an
isomorphism is local on $X$, respectively on $X'$. Hence it suffices to
identify their restrictions to a chart with the explicit identification
(7.14).

We write
$\varepsilon_N:Rf_!f^!N\to N$ for the counit of
$Rf_!\dashv f^!$ (for $f=p$ this is (7.7)). The map (7.11) is the
transpose of the morphism

$$
Rf_!(f^*N\otimes^{\mathbf L}\omega_f)
\xrightarrow{\ \sim\ }
N\otimes^{\mathbf L}Rf_!\omega_f
\xrightarrow{1\otimes\varepsilon_{\Lambda_S}}N ,
$$

where the first arrow is the projection formula. The map (7.12) is the
transpose, for $f'$, of the morphism

$$
Rf'_!g'^*f^!N
\xrightarrow{\ \sim\ }g^*Rf_!f^!N
\xrightarrow{g^*\varepsilon_N}g^*N,
\tag{7.13}
$$

where the first arrow is the inverse of the base change isomorphism
for $Rf_!$ [Stacks, Tag 0F7L](https://stacks.math.columbia.edu/tag/0F7L).

*Local charts.* Zariski locally on $X$ and $S$, a smooth morphism
is an étale map to affine space followed by the projection
[Stacks, Tag 054L](https://stacks.math.columbia.edu/tag/054L). Hence every point of $X$
has an affine open neighbourhood $u:U\hookrightarrow X$ mapping into
an affine open $v:V\hookrightarrow S$, together with a separated
étale map $e:U\to\mathbf A^d_V$ such that $fu=vp_de$, where
$p_d:\mathbf A^d_V\to V$ is the projection. By
Lemma [sk-lem-geo-affine-local] and uniqueness of right adjoints,
we have

$$
u^*f^!N=e^*p_d^*v^*N(d)[2d],\qquad
u^*\omega_f=\Lambda_U(d)[2d].
\tag{7.14}
$$

In particular, $\omega_f$ has a single nonzero cohomology sheaf, in
degree $-2d$, which is locally free of rank one. This proves (1): the
counit on $U$ is the composite of the étale counit for $e$, which is the sum
over the fibres, and the counit for $p_d$.

*(7.11) is an isomorphism.* Under (7.14), the source and the target of (7.11)
are both $e^*p_d^*v^*N(d)[2d]$, and we have to check that the map is the
identification obtained by reassociating tensor product and twist. We
compare transposes. Both are the projection formula followed by the
counit for $v$, the $d$ counits for the affine lines, and the étale counit
for $e$, and they agree by the formula for the counit of a composite in
Lemma [sk-lem-geo-affine-local]. Hence (7.11) is an isomorphism on each
such $U$, and therefore on $X$.

*(7.12) is an isomorphism.* We first consider each type of chart
separately. For the projective line, the unit (7.6) and counit (7.7)
commute with base change, so that the transpose of (7.13) is the usual
identification $g'^*p^*N(1)[2]=p'^*g^*N(1)[2]$ of pullbacks. By restriction
to the affine line and composition, the same holds for affine space. For
a separated étale map $u$, the stalk of $u_!M$ at a geometric point
is the direct sum of the stalks of $M$ at the geometric points over it.
This description is compatible with base change, and under it the counit
$u_!u^*N\to N$ is the sum of the identity maps of the stalks of $N$.
Thus, here too, the transpose of (7.13) is the
usual identification of inverse images. To combine these cases, recall that base
change for $Rf_!$ is compatible with composition [Stacks, Tag 0F7L](https://stacks.math.columbia.edu/tag/0F7L) and
that the counit of a composite is the composite of the counits.
Substituting this into (7.13), we see that the restriction of (7.12) to
$U\times_XX'$ is the composite of the étale and affine-space cases
just treated (the open immersions $u$ and $v$ are étale). Hence (7.12) is an isomorphism on a
cover of $X'$, and therefore it is an isomorphism.

Taking $N=\Lambda_S$, we see that (7.12) identifies $g'^*\omega_f$ with
$\omega_{f'}$. The compatibility of (7.11) with (7.12) says that two maps
$g'^*(f^*N\otimes^{\mathbf L}\omega_f)\to f'^!g^*N$ agree: (7.11)
followed by (7.12), and the identification
$g'^*(f^*N\otimes^{\mathbf L}\omega_f)=f'^*g^*N\otimes^{\mathbf L}\omega_{f'}$
(from $g'^*f^*=f'^*g^*$ and the case $N=\Lambda_S$) followed by (7.11) for
$f'$. Their transposes are maps
$Rf'_!g'^*(f^*N\otimes^{\mathbf L}\omega_f)\to g^*N$, both given by the
projection formula followed by the counit, once before and once after
the base change isomorphism for $Rf_!$. They agree because the
projection formula isomorphism is compatible with the base change
isomorphism for $Rf_!$, and because, by the definition (7.13) of (7.12),
the counit for $f'$ composed with $Rf'_!$ of (7.12) is $g^*$ of the
counit for $f$ under that isomorphism.
