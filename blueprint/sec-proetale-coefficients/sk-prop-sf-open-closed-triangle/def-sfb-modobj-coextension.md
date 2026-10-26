+++
id = "def-sfb-modobj-coextension"
kind = "definition"
title = "Coextension of scalars"
order = 1115
uses = ["det-def-sfb-module-objects-definition"]
lean = ["CategoryTheory.Mod.coextendScalars"]
+++
Let $\mathcal C$ be a monoidal category with equalizers. Assume it is closed: each
$X\otimes-$ has a right adjoint $\underline{\Hom}(X,-)$, with evaluation
$\mathrm{ev}\colon X\otimes\underline{\Hom}(X,Y)\to Y$. Let
$\varphi\colon\mathcal R\to\mathcal S$ be a morphism between monoid objects. No
commutativity or braiding is assumed. For an $\mathcal R$-module object $N$
([det-def-sfb-module-objects-definition]), let $\Hom_{\mathcal R}(\mathcal S,N)$ be the equalizer of
the two maps
$$
\underline{\Hom}(\mathcal S,N)\rightrightarrows\underline{\Hom}(\mathcal R\otimes\mathcal S,N).
$$
The first precomposes with the action
$\mu_{\mathcal S}(\varphi\otimes\mathcal S)\colon\mathcal R\otimes\mathcal S\to\mathcal S$.
The second is adjoint to
$\mathcal R\otimes\mathcal S\otimes\underline{\Hom}(\mathcal S,N)
\xrightarrow{\mathcal R\otimes\mathrm{ev}}\mathcal R\otimes N\xrightarrow{\gamma_N}N$.
Let $\mathcal S$ act on $\Hom_{\mathcal R}(\mathcal S,N)$ by right multiplication on the
source, $(s\cdot f)(t)=f(ts)$. That is, the action is adjoint to
$$
\mathcal S\otimes\mathcal S\otimes\Hom_{\mathcal R}(\mathcal S,N)
\xrightarrow{\mu_{\mathcal S}\otimes1}\mathcal S\otimes\Hom_{\mathcal R}(\mathcal S,N)
\to\mathcal S\otimes\underline{\Hom}(\mathcal S,N)\xrightarrow{\mathrm{ev}}N .
$$
With postcomposition on morphisms, this defines the *coextension of scalars* functor
$\operatorname{Coext}_\varphi=\Hom_{\mathcal R}(\mathcal S,-)\colon
\Mod_{\mathcal R}(\mathcal C)\to\Mod_{\mathcal S}(\mathcal C)$.
