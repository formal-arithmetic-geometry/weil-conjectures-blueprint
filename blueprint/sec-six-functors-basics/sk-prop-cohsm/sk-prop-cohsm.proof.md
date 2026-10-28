+++
kind = "proof"
of = "sk-prop-cohsm"
uses = ["sk-prop-geo-p1-adjunction", "sk-lem-geo-affine-local"]
+++
The maps (G11) and (G12) are defined globally as adjoint transposes, and being
an isomorphism is local on $X$, respectively on $X'$. Hence it suffices to
identify their restrictions to a chart with the explicit identification (G15).

We write $\varepsilon_N:Rf_!f^!N\to N$ for the counit of $Rf_!\dashv f^!$ (for
$f=p$ this is (G7) of [sk-prop-geo-p1-adjunction]). The map (G11) is the
transpose of the morphism

$$
Rf_!(f^*N\otimes^{\mathbf L}\omega_f)\xrightarrow{\ \sim\ }N\otimes^{\mathbf L}Rf_!\omega_f
\xrightarrow{\ 1\otimes\varepsilon_{\Lambda_S}\ }N,
$$

where the first arrow is the projection formula. The map (G12) is the
transpose, for $f'$, of the morphism

$$
Rf'_!g'^*f^!N\xrightarrow{\ \sim\ }g^*Rf_!f^!N\xrightarrow{\ g^*\varepsilon_N\ }g^*N,\qquad\text{(G14)}
$$

where the first arrow is the inverse of the base change isomorphism for
$Rf_!$ [Stacks, Tag 0F7L](https://stacks.math.columbia.edu/tag/0F7L).

*Local charts.* Zariski locally on $X$ and $S$, a smooth morphism is an étale
map to affine space followed by the projection
[Stacks, Tag 054L](https://stacks.math.columbia.edu/tag/054L). Hence every
point of $X$ has an affine open neighbourhood $u:U\hookrightarrow X$ mapping
into an affine open $v:V\hookrightarrow S$, together with a separated étale map
$e:U\to\mathbf A^d_V$ such that $fu=vp_de$, where $p_d:\mathbf A^d_V\to V$ is
the projection. By [sk-lem-geo-affine-local] and uniqueness of right adjoints,
we have

$$
u^*f^!N=e^*p_d^*v^*N(d)[2d],\qquad u^*\omega_f=\Lambda_U(d)[2d].\qquad\text{(G15)}
$$

In particular, $\omega_f$ has a single nonzero cohomology sheaf, in degree
$-2d$, which is locally free of rank one. This proves (1): the counit on $U$ is
the composite of the étale counit for $e$, which is the sum over the fibres,
and the counit for $p_d$.

*(G11) is an isomorphism.* Under (G15), the source and the target of (G11) are
both $e^*p_d^*v^*N(d)[2d]$, and we have to check that the map is the
identification obtained by reassociating tensor product and twist. We compare
transposes. Both are the projection formula followed by the counit for $v$, the
$d$ counits for the affine lines, and the étale counit for $e$, and they agree
by the formula for the counit of a composite in [sk-lem-geo-affine-local].
Hence (G11) is an isomorphism on each such $U$, and therefore on $X$.

*(G12) is an isomorphism.* We first consider each type of chart separately.
For the projective line, the unit (G6) and counit (G7) of
[sk-prop-geo-p1-adjunction] commute with base change, so that the transpose of
(G14) is the usual identification $g'^*p^*N(1)[2]=p'^*g^*N(1)[2]$ of
pullbacks. By restriction to the affine line and composition, the same holds
for affine space. For a separated étale map $u$, the stalk of $u_!M$ at a
geometric point is the direct sum of the stalks of $M$ at the geometric points
over it. This description is compatible with base change, and under it the
counit $u_!u^*N\to N$ is the sum of the identity maps of the stalks of $N$.
Thus, here too, the transpose of (G14) is the usual identification of inverse
images. To combine these cases, recall that base change for $Rf_!$ is
compatible with composition
[Stacks, Tag 0F7L](https://stacks.math.columbia.edu/tag/0F7L) and that the
counit of a composite is the composite of the counits. Substituting this into
(G14), we see that the restriction of (G12) to $U\times_XX'$ is the composite
of the étale and affine-space cases just treated (the open immersions $u$ and
$v$ are étale). Hence (G12) is an isomorphism on a cover of $X'$, and therefore
it is an isomorphism.

Taking $N=\Lambda_S$, we see that (G12) identifies $g'^*\omega_f$ with
$\omega_{f'}$. The compatibility of (G11) with (G12) says that two maps
$g'^*(f^*N\otimes^{\mathbf L}\omega_f)\to f'^!g^*N$ agree: (G11) followed by
(G12), and the identification
$g'^*(f^*N\otimes^{\mathbf L}\omega_f)=f'^*g^*N\otimes^{\mathbf L}\omega_{f'}$
(from $g'^*f^*=f'^*g^*$ and the case $N=\Lambda_S$) followed by (G11) for $f'$.
Their transposes are maps
$Rf'_!g'^*(f^*N\otimes^{\mathbf L}\omega_f)\to g^*N$, both given by the
projection formula followed by the counit, once before and once after the base
change isomorphism for $Rf_!$. They agree because the projection formula
isomorphism is compatible with the base change isomorphism for $Rf_!$, and
because, by the definition (G14) of (G12), the counit for $f'$ composed with
$Rf'_!$ of (G12) is $g^*$ of the counit for $f$ under that isomorphism.
