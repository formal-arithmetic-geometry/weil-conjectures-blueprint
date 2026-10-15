+++
id = "def-sfb-modobj-restriction"
kind = "definition"
title = "Restriction of scalars"
order = 1585
uses = ["sk-def-sfb-module-objects"]
lean = ["CategoryTheory.Mod.comap"]
+++
Let $\mathcal C$ be a monoidal category and $\varphi\colon\mathcal R\to\mathcal S$ a
morphism of monoid objects. For an $\mathcal S$-module object $N$
([sk-def-sfb-module-objects]), the morphism
$$
\gamma_N\circ(\varphi\otimes N)\colon\mathcal R\otimes N\to N
$$
is an action of $\mathcal R$ on $N$, and $\mathcal S$-linear maps are $\mathcal R$-linear for
these actions. This defines the *restriction of scalars* functor
$\operatorname{Res}_\varphi\colon\Mod_{\mathcal S}(\mathcal C)\to\Mod_{\mathcal R}(\mathcal C)$,
which is the identity on underlying objects and morphisms.
