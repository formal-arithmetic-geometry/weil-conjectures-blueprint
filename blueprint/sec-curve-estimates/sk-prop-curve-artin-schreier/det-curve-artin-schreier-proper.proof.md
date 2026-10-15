+++
kind = "proof"
of = "det-curve-artin-schreier-proper"
+++
The sequence $0\to\mathbf F_p\to\mathbf G_a\xrightarrow{\wp}\mathbf G_a\to0$,
$\wp=F-1$, is exact on $C_{\mathrm{ét}}$ ([lem-sc-as-sequence]), and
$H^q(C_{\mathrm{ét}},\mathbf G_a)=H^q(C,\cO_C)$, which vanishes for $q\geq2$
([lem-sc-ga-cohomology]). Moreover $H^0(C,\cO_C)=k$
([lem-sc-global-functions]) and $E$ is finite-dimensional of dimension $g$.
The identification with Zariski cohomology is induced by the identity on
Čech complexes of an affine cover, so it carries the map induced by $\wp$ on
étale cohomology to $F-1$ on $E$. The long exact sequence is

$$
0\to H^0(\mathbf F_p)\to k\xrightarrow{\wp}k\to H^1(\mathbf F_p)\to
E\xrightarrow{F-1}E\to H^2(\mathbf F_p)\to0,
$$

and $H^q(\mathbf F_p)=0$ for $q\geq3$. On $k$, $\ker\wp=\mathbf F_p$ and
$\wp$ is surjective ([lem-sc-artin-schreier-k]). Hence
$H^0(C,\mathbf F_p)=\mathbf F_p$ and $H^1(C,\mathbf F_p)\to\ker(F-1)$ is an
isomorphism. On $E$, $F-1$ is surjective ([lem-sc-lang-steinberg]), so
$H^2(C,\mathbf F_p)=0$. The kernel $\ker(F-1)=E^F$ is a finite
$\mathbf F_p$-vector space of dimension at most $\dim_kE=g$
([lem-sc-fixed-points-finite]).

For $k\subseteq k'$, $C_{k'}$ is again smooth, proper and connected
([lem-sc-base-change-curve]). Pullback along $C_{k'}\to C$ maps the
Artin–Schreier sequence of $C$ to that of $C_{k'}$, so the pullback maps
commute with the long exact sequences. Flat base change
([lem-pc-flat-base-change-cohom]) identifies $E\otimes_kk'$ with
$H^1(C_{k'},\cO_{C_{k'}})$, and the absolute Frobenius corresponds to
$F\otimes\sigma_{k'}$, where $\sigma_{k'}$ is the $p$th power map of $k'$. On
$H^0$ the pullback map is the identity of $\mathbf F_p$. On $H^1$ it is the
map $E^F\to(E\otimes_kk')^{F\otimes\sigma_{k'}}$, $v\mapsto v\otimes1$, which
is an isomorphism ([lem-sc-frobenius-fixed-invariance]). In degrees $q\geq2$
both sides vanish. Hence every $\rho^q_{k'/k}(C,\mathbf F_p)$ is an
isomorphism.
