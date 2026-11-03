+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism"
order = 556
+++
The maps
(6.11) and (6.12) are defined globally as adjoint
transposes. Being an isomorphism is local on $X$, respectively on $X'$.
We show that on a chart both maps become identifications of inverse images
under the explicit identification (6.14). For this we follow
the counits through the factorization $U\to\mathbf A^d_V\to V$.

We write
$\varepsilon_N:Rf_!f^!N\to N$ for the counit of
$Rf_!\dashv f^!$ (for $f=p$ this is (6.6)). The map (6.11) is the
transpose of the morphism

$$
Rf_!(f^*N\otimes^{\mathbf L}\omega_f)
\xrightarrow{\ \sim\ }
N\otimes^{\mathbf L}Rf_!\omega_f
\xrightarrow{1\otimes\varepsilon_{\Lambda_S}}N ,
$$

where the first arrow is the projection formula. The map (6.12) is the
transpose, for $f'$, of the morphism

$$
Rf'_!g'^*f^!N
\xrightarrow{\ \sim\ }g^*Rf_!f^!N
\xrightarrow{g^*\varepsilon_N}g^*N,
\tag{6.13}
$$

where the first arrow is the inverse of the base change isomorphism
for $Rf_!$ [Stacks, [0F7L](https://stacks.math.columbia.edu/tag/0F7L)].

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
\tag{6.14}
$$

In particular, $\omega_f$ has a single nonzero cohomology sheaf, in
degree $-2d$, which is locally free of rank one. This proves (1), because
the counit on $U$ is the composite of the étale counit for $e$ and the
counit for $p_d$. The first of these is the sum over the fibres.

*(6.11) is an isomorphism.* On each such $U$, under
(6.14), the source and the target of (6.11)
are both $e^*p_d^*v^*N(d)[2d]$. We claim that the map is the
identification obtained by reassociating tensor product and twist. It
suffices to compare the transposes. Both are the projection formula
followed by the counit for $v$, the $d$ counits for the affine lines, and
the étale counit for $e$. They agree by the formula for the counit of a
composite in Lemma [lemma-affine-space-etale-localization]. Hence
(6.11) is an isomorphism on $X$.

*(6.12) is an isomorphism.* For each type of chart,
under the explicit description of $f^!$ as a
twisted inverse image, (6.12) is the evident identification of
inverse images. For the projective line, the transpose of
(6.13) is the usual identification
$g'^*p^*N(1)[2]=p'^*g^*N(1)[2]$ of pullbacks. This holds because the unit
(6.5) and counit (6.6) commute with base change.
By restriction to the affine line and composition, the same holds for
affine space. For a separated étale map $u$, the transpose is again the
usual identification of inverse images. Indeed, the stalk of $u_!M$ at a
geometric point is the direct sum of the stalks of $M$ at the geometric
points over it. This description is compatible with base change, and under
it the counit $u_!u^*N\to N$ is the sum of the identity maps of the stalks
of $N$.

The cases combine, because base change for $Rf_!$ is compatible with
composition [Stacks, [0F7L](https://stacks.math.columbia.edu/tag/0F7L)] and the counit of a composite is the composite of
the counits. The open immersions $u$ and $v$ are étale. Substituting
these facts into (6.13), we see that the restriction of
(6.12) to $U\times_XX'$ is the composite of the étale and
affine-space cases just treated. Hence (6.12) is an
isomorphism on a cover of $X'$, and therefore it is an isomorphism.

*Compatibilities.* Taking $N=\Lambda_S$, we see that
(6.12) identifies $g'^*\omega_f$ with $\omega_{f'}$, because
$g^*\Lambda_S=\Lambda_{S'}$. The compatibility of (6.11) with
(6.12) says that two maps
$g'^*(f^*N\otimes^{\mathbf L}\omega_f)\to f'^!g^*N$ agree. The first is
(6.11) followed by (6.12). The second is the
identification
$g'^*(f^*N\otimes^{\mathbf L}\omega_f)=f'^*g^*N\otimes^{\mathbf L}\omega_{f'}$,
coming from $g'^*f^*=f'^*g^*$ and the case $N=\Lambda_S$, followed by
(6.11) for $f'$. Their transposes are maps
$Rf'_!g'^*(f^*N\otimes^{\mathbf L}\omega_f)\to g^*N$. Both are given by the
projection formula followed by the counit, once before and once after
the base change isomorphism for $Rf_!$. They agree for two reasons. The
projection formula isomorphism is compatible with the base change
isomorphism for $Rf_!$. And by the definition (6.13) of
(6.12), the counit for $f'$ composed with $Rf'_!$ of
(6.12) is $g^*$ of the counit for $f$ under that
isomorphism.
