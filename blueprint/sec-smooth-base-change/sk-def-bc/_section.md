+++
id = "sk-def-bc"
kind = "definition"
title = "The recorded base-change property"
order = 1423
lean = ["AlgebraicGeometry.Etale.BaseChangeProperty", "AlgebraicGeometry.Etale.baseChangeHomologyMap"]
tags = ["sketch"]
+++
For a morphism $f:X\to S$, a commutative ring $\Lambda$, and an integer
$q$, write $\mathrm{BC}(f,\Lambda,q)$ for: for every
quasi-compact quasi-separated $g:T\to S$, every sheaf $\mathcal F$ of
$\Lambda$-modules on $T_{\Et}$, and the Cartesian square

$$
\begin{array}{ccc}
X & \xleftarrow{\;h\;} & Y=X\times_ST\\
f\downarrow & & \downarrow e\\
S & \xleftarrow{\;g\;} & T,
\end{array}
$$

the base-change map
$f^{-1}R^qg_*\mathcal F\longrightarrow R^qh_*e^{-1}\mathcal F$
is an isomorphism. Here the *base-change map* is the degree-$q$
cohomology sheaf of the derived base-change morphism
$Lf^*Rg_*\to Rh_*Le^*$ (adjunction and pullback of the exchange) applied to
$\mathcal F$ placed in degree $0$. No invertibility condition on $\Lambda$
is part of the property. In the applications $\Lambda=\Z/n\Z$ with an
integer $n$ invertible on $S$, and we then write $\mathrm{BC}(f,n,q)$.

We say that $\mathrm{BC}(f,\Lambda,q)$ *holds universally* if
$\mathrm{BC}(f_{S'},\Lambda,q)$ holds for every base change
$f_{S'}:X\times_SS'\to S'$ of $f$ along every morphism $S'\to S$. The
*cumulative universal* property, written $\mathrm{UBC}^{\le q}(f,\Lambda)$
(for $\Lambda=\Z/n\Z$ it is the property $BC(f,n,q)$ of Stacks Project,
Tag `0F02`, written $\mathrm{UBC}^{\le q}(f,n)$), is: for every morphism
$S'\to S$, every quasi-compact quasi-separated $g:T\to S'$, every sheaf
$\mathcal F$ of $\Lambda$-modules on $T_{\Et}$ and every $r\le q$, the
base-change map $(f_{S'})^{-1}R^rg_*\mathcal F\to R^rh_*e^{-1}\mathcal F$
of the square of $f_{S'}$ along $g$ is an isomorphism; that is,
$\mathrm{BC}(f,\Lambda,r)$ holds universally for every $r\le q$ (if $n$ is
invertible on $S$, it is invertible on every $S'$).

The base-change map is natural in $\mathcal F$ and compatible with étale
localization and with composition of squares. $\mathrm{BC}(f,\Lambda,q)$
tests only the fixed morphism $f$ and the single degree $q$, and the
preliminary base change in the universal property is not a formality:
$\mathrm{BC}(f,n,q)$ at the fixed base does not in general imply
$\mathrm{BC}(f_{S'},n,q)$ (already for $q=0$ there are flat, finitely
presented $f$ with geometrically connected fibres satisfying
$\mathrm{BC}(f,n,0)$ but not $\mathrm{BC}(f_{\Aaf^1_S},n,0)$). For smooth
$f$ the distinction disappears: smoothness is stable under base change, so
$\mathrm{BC}(f,n,q)$ for all smooth $f$ gives it universally.
