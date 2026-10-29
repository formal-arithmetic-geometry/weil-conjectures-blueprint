+++
id = "def-sfb-module-linear-open-lower-shriek"
kind = "definition"
title = "Linear extension by zero"
order = 1313
uses = ["lem-sfb-open-projection-formula", "det-def-sfb-transport", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-module-objects"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.linearOpenImmersionLowerShriek"]
+++
Let $\Lambda$ be a commutative condensed ring and $j\colon U\to X$ an open immersion.
With $\Lambda_X=p_X^*\Lambda$ ([det-def-sfb-pulled-back-coefficients]) and module
objects as in [det-def-sfb-module-objects], the *linear extension by zero*

$$
j^{\mathrm{lin}}_!\colon\Mod_{j^*\Lambda_X}\to\Mod_{\Lambda_X}
$$

is the linearization ([det-def-sfb-transport]) of the extension by zero $j^{\Ab}_!$ of
abelian sheaves through the projection formula of [lem-sfb-open-projection-formula]:
it sends a $j^*\Lambda_X$-module $M$ to $j^{\Ab}_!M$ with the $\Lambda_X$-action

$$
\Lambda_X\otimes j^{\Ab}_!M\cong j^{\Ab}_!(j^*\Lambda_X\otimes M)
\xrightarrow{\;j^{\Ab}_!(\text{action})\;}j^{\Ab}_!M .
$$

Its underlying sheaf functor is $j^{\Ab}_!$, it is exact, and it is left adjoint to
the transport $\operatorname{mapMod}(j^*_{\Ab})\colon\Mod_{\Lambda_X}\to
\Mod_{j^*\Lambda_X}$.
