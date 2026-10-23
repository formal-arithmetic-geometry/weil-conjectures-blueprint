+++
kind = "proof"
of = "det-curve-artin-schreier-proper"
uses = ["lem-sc-as-sequence", "lem-sc-ga-cohomology", "lem-sc-global-functions", "lem-sc-artin-schreier-k", "lem-sc-artin-schreier-dimension", "lem-sc-fixed-points-finite", "lem-sc-frobenius-fixed-invariance", "lem-pc-flat-base-change-cohom", "lem-sc-base-change-curve"]
+++
Take $V=H^1(C,\cO_C)$, finite-dimensional since $C$ is proper, and $F$ the
$p$-linear map induced by $a\mapsto a^p$ on $\cO_C$. The sequence
$0\to\mathbf F_p\to\mathbf G_a\xrightarrow{\wp}\mathbf G_a\to0$, $\wp=F-1$,
is exact on $C_{\mathrm{ét}}$ ([lem-sc-as-sequence]), and
$H^q(C_{\mathrm{ét}},\mathbf G_a)=H^q(C,\cO_C)$ ([lem-sc-ga-cohomology]); the
identification is induced by the identity on Čech complexes of an affine
cover, so it carries the map induced by $\wp$ to $F-1$. Moreover
$H^0(C,\cO_C)=k$ ([lem-sc-global-functions]). The long exact sequence begins

$$
0\to H^0(\mathbf F_p)\to k\xrightarrow{\wp}k\to H^1(\mathbf F_p)\to
V\xrightarrow{F-1}V.
$$

On $k$, $\ker\wp=\mathbf F_p$ and $\wp$ is surjective
([lem-sc-artin-schreier-k]); hence $H^0(C,\mathbf F_p)=\mathbf F_p$ (as $C$
is connected) and $H^1(C,\mathbf F_p)\to V^F$ is an isomorphism. The vanishing
for $q\geq2$ is [lem-sc-artin-schreier-dimension]. The fixed points $V^F$ form
a finite $\mathbf F_p$-vector space of dimension at most $\dim_kV$
([lem-sc-fixed-points-finite]).

For $k\subseteq k'$, $C_{k'}$ is again smooth, proper and connected
([lem-sc-base-change-curve]). Pullback along $C_{k'}\to C$ maps the
Artin–Schreier sequence of $C$ to that of $C_{k'}$, so the pullback maps
commute with the long exact sequences. Flat base change
([lem-pc-flat-base-change-cohom]) identifies $k'\otimes_kV$ with
$H^1(C_{k'},\cO_{C_{k'}})$, the class $v$ going to $1\otimes v$, and the
absolute Frobenius of $C_{k'}$ induces the $p$-linear map $F'$ with
$F'(1\otimes v)=1\otimes F(v)$. Applying the first part over $k'$ gives the
identification of $H^1(C_{k'},\mathbf F_p)$ with $(k'\otimes_kV)^{F'}$, and
naturality of the boundary maps shows that the pullback map is
$v\mapsto1\otimes v$. This map of fixed points is an isomorphism
([lem-sc-frobenius-fixed-invariance]). On $H^0$ the pullback map is the
identity of $\mathbf F_p$, and in degrees $q\geq2$ both sides vanish. Hence
every $\rho^q_{k'/k}(C,\mathbf F_p)$ is an isomorphism.
