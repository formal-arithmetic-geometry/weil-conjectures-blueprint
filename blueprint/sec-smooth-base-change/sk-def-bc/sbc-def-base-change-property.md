+++
id = "sbc-def-base-change-property"
kind = "definition"
title = "The recorded base-change property $BC(f,n,q)$"
order = 1408
uses = ["def-weil-pbc-scheme-conventions", "sbc-def-base-change-map", "sbc-def-base-change-square", "sbc-def-coefficient-conventions"]
+++
Let $f:X\to S$ be a
morphism of schemes (conventions of [def-weil-pbc-scheme-conventions]),
let $n\geq1$ be an integer invertible on $S$, let $q\geq0$, and put
$\Lambda=\mathbf Z/n\mathbf Z$ (a coefficient ring as in
[sbc-def-coefficient-conventions]).
We say that *$BC(f,n,q)$ holds*, or that *the recorded
base-change property holds for $f$, $n$ and $q$*, if for every
base-change square of
[sbc-def-base-change-square] whose horizontal side $g:T\to S$ is
quasi-compact and
quasi-separated, and every abelian sheaf $\mathcal F$ on $T_{\Et}$
annihilated by $n$ (that is, every sheaf of
$\mathbf Z/n\mathbf Z$-modules on $T_{\Et}$), the base-change map
of [sbc-def-base-change-map] in degree $q$,

$$
\operatorname{BC}^q_{f,g}(\mathcal F):
f^{-1}R^qg_*\mathcal F\longrightarrow R^qh_*e^{-1}\mathcal F,
$$

is an isomorphism. The cumulative form
"$BC(f,n,q')$ for all $q'\leq q$" says that the derived
base-change map $\operatorname{BC}_{f,g}(\mathcal F)$ of
[sbc-def-base-change-map] is an isomorphism on $q'$-th cohomology
sheaves for all $q'\leq q$. We say that *$BC(f,n,q)$ holds
universally* if $BC(f',n,q)$ holds for every base change
$f':X'=X\times_SS'\to S'$ of $f$ along every morphism of schemes
$S'\to S$ (here $n$ is invertible on $S'$ because it is invertible on
$S$). We write $\mathrm{UBC}^{\le q}(f,n)$
for the cumulative universal property "$BC(f,n,q')$ holds universally
for all $q'\leq q$"; it is the property $BC(f,n,q)$ of the Stacks
Project, Tag 0F02.

$BC(f,n,q)$ is a condition in the single degree $q$ only. The universal
form is the one needed when the property is applied to base changes of
$f$, and to horizontal sides $T\to S'$ whose composite with $S'\to S$
need not be quasi-compact and quasi-separated. The fixed-base property
does not imply the universal one: there are flat, finitely presented $f$
with geometrically connected fibres for which $BC(f,n,0)$ holds but
$BC(f_{\mathbf A^1_S},n,0)$ fails. Since smoothness is stable under base
change, $BC(f,n,q)$ for every smooth $f$ and every $q$ gives $BC(f,n,q)$
universally for every smooth $f$ and every $q$.
