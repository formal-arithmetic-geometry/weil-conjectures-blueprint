+++
id = "def-sfb-modobj-transport"
kind = "definition"
title = "Transport of module objects along a lax monoidal functor"
order = 1543
uses = ["sk-def-sfb-module-objects", "sk-def-sfb-ring-object"]
lean = ["CategoryTheory.Functor.mapMod"]
+++
Let $F\colon\mathcal C\to\mathcal D$ be a lax monoidal functor between monoidal categories,
with structure maps $\mu^F_{X,Y}\colon FX\otimes FY\to F(X\otimes Y)$ and
$\varepsilon^F\colon\mathbf 1\to F\mathbf 1$. Let $\mathcal R$ be a monoid object of
$\mathcal C$ ([sk-def-sfb-ring-object]). Then $F\mathcal R$ is a monoid object of
$\mathcal D$, with multiplication $F(\mu)\circ\mu^F_{\mathcal R,\mathcal R}$ and unit
$F(\eta)\circ\varepsilon^F$. For an $\mathcal R$-module object $M$
([sk-def-sfb-module-objects]), the morphism
$$
F\mathcal R\otimes FM\xrightarrow{\mu^F_{\mathcal R,M}}F(\mathcal R\otimes M)
\xrightarrow{F\gamma_M}FM
$$
makes $FM$ an $F\mathcal R$-module object. For an $\mathcal R$-linear map $f$, the map
$Ff$ is $F\mathcal R$-linear. This defines the functor
$$
\operatorname{mapMod}(F)\colon\Mod_{\mathcal R}(\mathcal C)\to\Mod_{F\mathcal R}(\mathcal D),
$$
which commutes with the forgetful functors.
