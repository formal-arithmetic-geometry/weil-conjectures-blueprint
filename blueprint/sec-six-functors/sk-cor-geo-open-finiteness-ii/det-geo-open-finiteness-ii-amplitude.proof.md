+++
kind = "proof"
of = "det-geo-open-finiteness-ii-amplitude"
+++
*Finiteness of $d$.* The morphism $j$ is a morphism between schemes of finite
type over the field $k$, so $\operatorname{cd}(j)<\infty$ by
[lem-kun-0f10] (1).

*(1).* Every sheaf $F$ of $\Lambda$-modules is killed by $\ell^r$, hence is a
torsion abelian sheaf. The forgetful functor from $\Lambda$-modules to abelian
sheaves is exact and commutes with derived direct image (Stacks, Tag
[0D6J](https://stacks.math.columbia.edu/tag/0D6J)), so $R^qj_{\mathrm{ét},*}F$
computed with $\Lambda$-coefficients has the same underlying abelian sheaf as
$R^qj_*$ of the underlying torsion abelian sheaf. The latter vanishes for
$q>d$ by the definition [def-kun-cd] of $d=\operatorname{cd}(j)$.

*(2).* An open immersion of Noetherian schemes is quasi-compact and
quasi-separated, so the comparison direct image
[prop-weil-pbc-comparison-direct-image], applied to $F$ placed in degree $0$,
gives an isomorphism
$\nu_Y^*Rj_{\mathrm{ét},*}F\xrightarrow{\sim}Rj_{\mathrm{proét},*}\nu_X^*F$.
Since $\Lambda$ is finite, $\nu_Y^*$ is exact
([prop-weil-pbc-site-comparison-finite-level]), so it commutes with taking
cohomology sheaves:

$$
\mathcal H^q\bigl(Rj_{\mathrm{proét},*}\nu_X^*F\bigr)\cong
\nu_Y^*\bigl(R^qj_{\mathrm{ét},*}F\bigr),
$$

which vanishes for $q>d$ by (1).

*(3).* Induct on the number of nonzero cohomology sheaves of $M$. If there is
only one, $M\simeq\mathcal H^m(M)[-m]$ with $a\le m\le b$, and (2) together
with $\mathcal H^q=0$ for $q<0$ of the direct image of a sheaf gives
cohomology in $[m,m+d]\subset[a,b+d]$. Otherwise choose $a\le m<b$ splitting
the nonzero cohomology sheaves, and apply the exact functor
$Rj_{\mathrm{proét},*}\nu_X^*$ to the truncation triangle
$\tau^{\le m}M\to M\to\tau^{>m}M\to$; the outer terms have cohomology in
$[a,m+d]$ and $[m+1,b+d]$ by induction, and the long exact cohomology sequence
puts the middle term in $[a,b+d]$.
