+++
id = "det-def-sf-operations"
kind = "definition"
title = "The six operations: ambient typing"
order = 2756
uses = ["lem-sf-proetale-constructible-origin", "det-def-localizing-closure-existence", "def-weil-exceptional-adjoint-admissibility", "det-existence-localizing", "det-existence-restriction", "def-sfb-dc-upper-shriek-functor"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.derivedTensor", "AlgebraicGeometry.ProEtale.CondensedRing.derivedHom", "AlgebraicGeometry.ProEtale.CondensedRing.derivedTensorHomAdjunction₂", "AlgebraicGeometry.ProEtale.CondensedRing.openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriek", "AlgebraicGeometry.ProEtale.HasAmbientExceptionalRightAdjoint", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriek", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekHomEquiv", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriek", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekAdjunction"]
+++
For a separated finite-type $f:X\to Y$ the six operations are the following
functors of ambient categories:

1. **(i)** the derived pullback, the derived tensor product and the derived
internal Hom
$$
\begin{aligned}
Lf^*&:D(Y,\Lambda)\longrightarrow D(X,\Lambda),\\
-\otimes^L_\Lambda-&:D(Y,\Lambda)\times D(Y,\Lambda)\longrightarrow D(Y,\Lambda),\\
\RHom_\Lambda(-,-)&:D(Y,\Lambda)^{\mathrm{op}}\times D(Y,\Lambda)\longrightarrow D(Y,\Lambda),
\end{aligned}
$$
where $\RHom_\Lambda$ is the internal Hom, right adjoint to $-\otimes^L_\Lambda-$;
1. **(ii)** the derived direct image
$Rf_*:D^+(X,\Lambda)\to D^+(Y,\Lambda)$;
1. **(iii)** extension by zero $j_!:D^+(U,\Lambda)\to D^+(X,\Lambda)$ for an
open immersion $j:U\hookrightarrow X$;
1. **(iv)** the compact-support direct image $Rf_!=R\bar f_*j_!$ attached to a
compactification $X\xrightarrow{j}\overline X\xrightarrow{p}Y$, as a functor of
ambient categories, independent of the compactification on the étale-origin
complexes;
1. **(v)** *the ambient exceptional right adjoint* $Rf^{\times}$, an
*optional and conditional* notion: it is not defined, it is *assumed*: a
functor of ambient categories
$$
Rf^{\times}:D(Y,\Lambda)\longrightarrow D(X,\Lambda)
$$
which is right adjoint to $Rf_!$ of (iv). Its *existence* — together
with $\operatorname{FullCD}$ for the proper part of the compactification and
the compatibility of units and counits with refinements — is the *ambient
exceptional right adjoint datum*, clause (1) of [def-weil-exceptional-adjoint-admissibility];
1. **(vi)** *the exceptional inverse image* $Rf^!$, a functor of the
small categories
$$
Rf^!:\Dctf(Y,\Lambda)\longrightarrow\Dctf(X,\Lambda),
$$
*defined unconditionally* for every separated finite-type morphism
$f:X\to Y$ of finite-type $k$-schemes, as follows. At a finite stage
$\Lambda=A=A_{E,n}$ let $f^{\times}:D(Y_{\Et},A)\to D(X_{\Et},A)$ be a chosen
right adjoint of the étale compact-support functor
$Rf^{\Et}_!:D(X_{\Et},A)\to D(Y_{\Et},A)$ on the unbounded derived categories
of the small étale sites, which exists by Brown representability ([def-weil-exceptional-inverse-image]). Every
object of $\Dctf(Y,A)$ is of étale origin,
$L\cong\nu_Y^*G$ with $G\in\Dctf(Y_{\Et},A)$ unique up to unique isomorphism
([09AK](https://stacks.math.columbia.edu/tag/09AK), [lem-sf-proetale-constructible-origin]), and one *defines*
$$
Rf^!L:=\nu_X^*\,f^{\times}G\;=\;\nu_X^*\,f^{\times}R\nu_{Y,*}L ,
$$
the étale right adjoint transported along the étale/pro-étale
comparison (the second formula makes sense on all of $D^+(Y_{\Proet},A)$ and
agrees with the first on $\Dctf$, since $G\to R\nu_{Y,*}\nu_Y^*G$ is an
isomorphism by the full faithfulness of $\nu_Y^*$ on $D^+$). Its two
defining properties are *theorems*, not hypotheses: the *adjunction*
$\operatorname{Hom}_Y(Rf_!K,L)\cong\operatorname{Hom}_X(K,Rf^!L)$,
natural in every bounded-below $K$ of étale origin — in particular every
$K\in\Dctf(X,A)$ — and every bounded-below $L$, with units and counits
compatible with refinements of the compactification
([thm-sf-ambient-adjoint-class]); and the *preservation*
$Rf^!\Dctf(Y,A)\subseteq\Dctf(X,A)$, with explicit bounds on the
constructible interval and on the Tor amplitude
([det-existence-restriction], [thm-sf-ctf-stability] (v)). For
$\Lambda\in\{\mathcal O_E,E,\Qlb\}$, regarded as condensed rings, the functor
is defined directly on $\Lambda$-modules. The compact-support
direct image
$Rf_!:\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))$ on the localizing
closures ([det-def-localizing-closure-existence]) is exact and preserves direct sums, and
the objects of $\Dctf$ are compact generators, so Brown representability gives
an exact right adjoint
$f^!:\Loc(\Dctf(Y,\Lambda))\to\Loc(\Dctf(X,\Lambda))$
([det-existence-localizing] (3)). It sends $\Dctf(Y,\Lambda)$ into $\Dctf(X,\Lambda)$
([det-existence-restriction]), and one *defines*
$$
Rf^!:=f^!|_{\Dctf(Y,\Lambda)}:\Dctf(Y,\Lambda)\longrightarrow\Dctf(X,\Lambda).
$$
Since $\Dctf=\Dbc$ for these $\Lambda$, it is right adjoint to $Rf_!$ on
$\Dbc$, and by uniqueness of adjoints it agrees with the functor
$Rf^!=i^*\circ Rp^!$ on $D_{\mathrm{cons}}$ of [def-sfb-dc-upper-shriek-functor]. The
same construction applies to finite $A$, and there it agrees on $\Dctf(Y,A)$
with the étale definition above, again by uniqueness of adjoints.

When the ambient functor $Rf^{\times}$ of (v) exists and satisfies the
preservation clauses of [def-weil-exceptional-adjoint-admissibility], its restriction to $\Dctf$
agrees with $Rf^!$ by uniqueness of adjoints.

*Warning.* The existence hypothesis of the ambient datum of (v),
$\operatorname{FullCD}$ on *every* pro-étale sheaf of $A$-modules, *fails*
already for the structure morphism of an elliptic curve $E$ over
$\overline{\mathbf F}_p$ with $A=\mathbf F_r$, $r\neq p$: there is a pro-étale
$A$-module sheaf $\mathcal F$ on $E$ with $H^n(E_{\Proet},\mathcal F)\neq0$
for every $n\ge1$, and for that morphism $Rf_!=Rf_*$ does not preserve the
coproduct $\bigoplus_n\mathcal F[n]$ and has no right adjoint on
$D(E_{\Proet},A)$, nor on $D^+$ ([sk-rem-sf-fullcd-scope]).
