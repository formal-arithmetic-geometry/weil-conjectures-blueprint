+++
kind  = "proof"
of    = "sk-prop-sf-rf-shriek-preservation"
+++
*(i) Open immersions and finite étale morphisms.* For such $f$ the
ambient right adjoint is the exact functor $Lf^*$. Pulling back a finite
constructible stratification gives one again, and
$\mathcal H^q(Lf^*K)\cong f^*\mathcal H^q(K)$, so the constructible interval
is unchanged. Inverse image preserves flatness, so a bounded flat model in
degrees $[a,b]$ pulls back to one, giving the same Tor amplitude; applying
the exact tensor functor $f^*$ to a flat resolution also gives the
finite-level comparison
$(Rf_A^{\times}K)\otimes^{\mathrm L}_AB\cong Rf_B^{\times}(K\otimes^{\mathrm L}_AB)$, with bounds independent of $n$.

*(ii) Closed immersions.* Let $i:Z\hookrightarrow T$ be closed with
quasi-compact open complement $j:V\hookrightarrow T$ and $\dim T\le d$. The
pair $(V,T)$ satisfies the open-complement bound with $c=2d$: the
strict-henselization stalk formula writes $(R^qj_*M)_{\bar t}$ as a filtered
colimit of $H^q(V\times_TU,M)$ over pointed étale neighbourhoods $U$ of
$\bar t$, each an open of a finite-type $k$-scheme of dimension $\le d$, and
over the separably closed $k$ these vanish for $q>2d$
([sk-prop-sf-finiteness]); geometric stalks are conservative, so
$R^qj_*M=0$ there. The localization triangle
[sk-prop-sf-localization] then bounds $Ri^!$ in terms of $Rj_*$, which
produces the shift $2d+1$ on the constructible interval and, by the
residue-field test for Tor amplitude, on the amplitude as well. The bound
cannot be replaced by one depending only on the codimension of $Z$: for
$T=\operatorname{Spec}k[x,y]/(xy)$, $Z=V(y)$ (a component of $T$, so of
codimension $0$), $V=D(y)\cong\mathbf G_m$, which lies in the other component
$V(x)\cong\mathbf A^1$, and $M=\Lambda_T$ with $\Lambda=\mathbf F_\ell$, the
stalk $(R^1j_*\Lambda_V)_{\bar o}$ at the crossing point $o$ is $H^1$ of the
fraction field of the strictly henselian local ring of $\mathbf A^1$ at $0$
([03Q7](https://stacks.math.columbia.edu/tag/03Q7)), which is nonzero (the
Kummer class of $y$, [03PK](https://stacks.math.columbia.edu/tag/03PK)); the
localization triangle gives
$\mathcal H^2(Ri^!\Lambda_T)_{\bar o}\cong(R^1j_*\Lambda_V)_{\bar o}\neq0$,
excluded by $2\operatorname{codim}(Z,T)+1=1$ but allowed by $2\dim T+1=3$.
Even for a regular immersion into a smooth $T$ the codimension controls
$Ri^!$ only when $Z$ is regular as well: for the two axes
$Z=V(xy)\subset T=\mathbf A^2$, support Mayer–Vietoris gives
$\mathcal H^3(Ri^!\Lambda_T)_{\bar 0}\cong\Lambda(-2)\neq0$.

*(iii) Smooth morphisms.* Purity [sk-thm-smooth-purity] identifies
$Rf^!$ with $Lf^*(-)(d)[2d]$. Then $Lf^*$ is exact and preserves bounded
constructibility, the twist does not move degrees, and the shift carries
$[a,b]$ to $[a-2d,b-2d]$. For the Tor amplitude, test against the residue
field: $Rf^!K\otimes^{\mathrm L}_A\kappa\cong Lf^*(K\otimes^{\mathrm L}_A\kappa)(d)[2d]$, so the amplitude of $K$ shifts by
$-2d$ as well. The preservation clauses are thus consequences of purity, not
hypotheses of it.

*(iv) The general case.* For every separated finite-type $f$ the
functor $Rf^!$ of [sk-def-sf-operations] (vi) is defined, and the two
preservation clauses are *proved* as follows; nothing is assumed.
Constructibility and finite Tor amplitude, with given bounds, are local on
$X$. Cover $Y$ by affine opens $V$ and each $f^{-1}(V)$ by affine opens $U$,
with $u:U\hookrightarrow X$ the open immersion; $U\to V$ is affine of finite
type, hence factors as a closed immersion $i_U:U\hookrightarrow\mathbf
A^{d_U}_V$ followed by the smooth projection $\pi_U:\mathbf A^{d_U}_V\to V$.
By [sk-lem-sf-mate] (b), applied to $fu=\pi_Ui_U$ and to the open immersion
$u$ (whose $R(-)_!$ is $u_!$, with right adjoint $Lu^*$),
$Lu^*Rf^!\cong R(fu)^!\cong Ri_U^!\,R\pi_U^!$, so the restriction of $Rf^!L$
to $U$ is $Ri_U^!(R\pi_U^!(L|_V))$. Now compose (iii) with (ii): the smooth
projection shifts $[a,b]$ to $[a-2d_U,b-2d_U]$, and the closed immersion
into the target $\mathbf A^{d_U}_V$ of dimension $\le d_U+\dim Y$ then gives
$[a-2d_U,\,b-2d_U+2(d_U+\dim Y)+1]=[a-2d_U,\,b+2\dim Y+1]$; the maximum over
the finitely many charts is $[a-2D,\,b+2\dim Y+1]$ with $D=\max_Ud_U$, and
the same computation on the residue-field test gives the Tor amplitude. The
open-complement hypothesis of the affine-base form is discharged by the
$c=2d$ bound established in (ii), so it is a theorem here and not an
assumption. The constants depend on the charts and on $\dim Y$ only, not on
$n$, which is what the adic stages need ([sk-thm-sf-ctf-stability] (vii)).
