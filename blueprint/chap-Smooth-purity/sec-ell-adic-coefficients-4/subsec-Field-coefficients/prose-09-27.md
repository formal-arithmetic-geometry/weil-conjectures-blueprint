+++
id = "prose-09-27"
kind = "hidden"
title = "Field coefficients (2)"
order = 789
+++
Since $f^*(-)(d)[2d]$ is now a right adjoint of $Rf_{!,E}$, as is $f^!_E$,
Proposition [proposition-sp-unique-adjoint] gives an isomorphism
$f^!_E\xrightarrow{\sim}f_E^*(-)(d)[2d]$ compatible with the counits, and we let
$\gamma_{f,E}:f_E^*(-)(d)[2d]\xrightarrow{\sim}f^!_E$ be its inverse.

Hom groups over $\overline{\mathbf Q}_\ell$ are colimits of Hom groups over finite extensions,
so the adjunctions over the finite extensions pass to the colimit provided
they correspond under the transition maps. To see that they do, let
$E\subset F$ be a finite extension. Then extension of scalars along the finite
free map $\mathcal O_E\to\mathcal O_F$ commutes with $R\varprojlim$, and at
level $n$ it is extension along $\mathcal O_E/\ell^n\to\mathcal O_F/\ell^n$,
so we may compare the counits in $D(\operatorname{Tow})$. Extending scalars in the
pair of towers $(f_\bullet^!K_\bullet,\varepsilon)$ for $\mathcal O_E$ gives
a pair over $\mathcal O_F$, whose levels represent
$\operatorname{Hom}(Rf_!(-),K_n)$ by Lemma [lemma-sp-reduction]. By the
five lemma, applied levelwise, the pair then represents
$\operatorname{Hom}(Rf_{!,\bullet}(-),K_\bullet)$, and by uniqueness it is
isomorphic to the corresponding pair for $\mathcal O_F$ by a unique
counit-preserving isomorphism. Applying $R\varprojlim$ and inverting
$\ell$, we see that the adjunctions over $E$ and over $F$ correspond under
extension of scalars, transitively in $E\subset F\subset F'$.
