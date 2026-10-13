+++
id = "def-sfb-module-open-lower-shriek"
kind = "definition"
title = "Extension by zero of module objects"
order = 1696
uses = ["def-sfb-module-linear-open-lower-shriek", "sk-def-sfb-coefficient-morphisms", "sk-def-sfb-change-of-scalars"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.openImmersionLowerShriek"]
+++
Let $\Lambda$ be a commutative condensed ring and $j\colon U\to X$ an open immersion.
The *extension by zero of module objects* is

$$
j_!:=j^{\mathrm{lin}}_!\circ\operatorname{Res}_{\alpha_j}\colon
\Mod_{\Lambda_U}\to\Mod_{\Lambda_X},
$$

restriction of scalars along $\alpha_j\colon j^*\Lambda_X\to\Lambda_U$
([sk-def-sfb-coefficient-morphisms]) followed by the
linear extension by zero of [def-sfb-module-linear-open-lower-shriek]. The underlying
sheaf of $j_!M$ is the extension by zero $j^{\Ab}_!M$ of the underlying sheaf of $M$,
and $j_!$ is additive and exact.
