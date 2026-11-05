+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism"
order = 563
uses = ["lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-adjunction-projective-line", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
The maps
$\mu_N$ and $\beta_N$ are defined globally as adjoint
transposes. Since being an isomorphism is local on $X$, respectively on $X'$, we show that on a chart both maps become identifications of inverse images
under the explicit identification (6.14). For this we follow
the counits through the factorization $U\to\mathbf A^d_V\to V$.

We write
$\varepsilon_N:Rf_!f^!N\to N$ for the counit of
$Rf_!\dashv f^!$ (for $f=p$ this is (6.8)). The map $\mu_N$ is the
transpose of the morphism

$$
Rf_!(f^*N\otimes^{\mathbf L}\omega_f)
\xrightarrow{\ \sim\ }
N\otimes^{\mathbf L}Rf_!\omega_f
\xrightarrow{1\otimes\varepsilon_{A_S}}N ,
$$

where the first arrow is the projection formula. The map $\beta_N$ is the
transpose, for $f'$, of the morphism (6.2)
(Definition [definition-exceptional-base-change-finite]).

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
u^*\omega_f=A_U(d)[2d].
\tag{6.14}
$$

In particular, $\omega_f$ has a single nonzero cohomology sheaf, in
degree $-2d$, which is locally free of rank one. This proves (1), because
the counit on $U$ is the composite of the étale counit for $e$ and the
counit for $p_d$. The first of these is the sum over the fibres.

*$\mu_N$ is an isomorphism.* On each such $U$, under
(6.14), the source and the target of $\mu_N$
are both $e^*p_d^*v^*N(d)[2d]$. We claim that the map is the
identification obtained by reassociating tensor product and twist. It
suffices to compare the transposes. Both are the projection formula
followed by the counit for $v$, the $d$ counits for the affine lines, and
the étale counit for $e$. They agree by the formula for the counit of a
composite in Lemma [lemma-affine-space-etale-localization]. Hence
$\mu_N$ is an isomorphism on $X$.

*$\beta_N$ is an isomorphism.* For each type of chart,
under the explicit description of $f^!$ as a
twisted inverse image, $\beta_N$ is the evident identification of
inverse images. For the projective line, the transpose of
(6.2) is the usual identification
$g'^*p^*N(1)[2]=p'^*g^*N(1)[2]$ of pullbacks. This holds because the unit
(6.7) and counit (6.8) commute with base change.
By restriction to the affine line and composition, the same holds for
affine space. For a separated étale map $u$, the transpose is again the
usual identification of inverse images. Indeed, the stalk of $u_!M$ at a
geometric point is the direct sum of the stalks of $M$ at the geometric
points over it. This description is compatible with base change, and under
it the counit $u_!u^*N\to N$ is the sum of the identity maps of the stalks
of $N$.

The cases combine, because base change for $Rf_!$ is compatible with
composition (Proposition [proposition-composition-base-change-rf-shriek](2)) and the counit of a composite is the composite of
the counits. The open immersions $u$ and $v$ are étale, so the étale case covers them as well. Substituting these facts into (6.2), we see that the restriction of
$\beta_N$ to $U\times_XX'$ is the composite of the étale and
affine-space cases just treated. Hence $\beta_N$ is an
isomorphism on a cover of $X'$, and therefore it is an isomorphism.

*Compatibilities.* Taking $N=A_S$, we see that
$\beta_N$ identifies $g'^*\omega_f$ with $\omega_{f'}$, because
$g^*A_S=A_{S'}$. The compatibility of $\mu_N$ with
$\beta_N$ says that two maps $g'^*(f^*N\otimes^{\mathbf L}\omega_f)\to f'^!g^*N$ agree. Here the first is
$\mu_N$ followed by $\beta_N$, and the second is the identification
$g'^*(f^*N\otimes^{\mathbf L}\omega_f)=f'^*g^*N\otimes^{\mathbf L}\omega_{f'}$,
coming from $g'^*f^*=f'^*g^*$ and the case $N=A_S$, followed by
$\mu_N$ for $f'$. Their transposes are maps
$Rf'_!g'^*(f^*N\otimes^{\mathbf L}\omega_f)\to g^*N$. Both are given by the
projection formula followed by the counit, once before and once after
the base change isomorphism for $Rf_!$. They agree for two reasons. First, the projection formula isomorphism is compatible with the base change
isomorphism for $Rf_!$. Second, by the definition (6.2) of
$\beta_N$, the counit for $f'$ composed with $Rf'_!$ of
$\beta_N$ is $g^*$ of the counit for $f$ under that
isomorphism.
