+++
id = "def-sfb-modobj-linearization-right-adjoint"
kind = "definition"
title = "Linearization of a right adjoint"
order = 1598
uses = ["def-sfb-projection-formula", "sk-def-sfb-module-objects"]
lean = ["CategoryTheory.Functor.ProjectionFormula.mapModRight"]
+++
Let $\pi$ be a projection formula for $P\colon\mathcal C\to\mathcal D$ relative to a strong
monoidal $S\colon\mathcal D\to\mathcal C$ ([def-sfb-projection-formula]). Let
$P\dashv G$ be an adjunction with counit $c$. Let
$$
\theta_{L,N}\colon SL\otimes GN\to G(L\otimes N)
$$
be the adjoint of
$P(SL\otimes GN)\xrightarrow{\pi_{L,GN}}L\otimes PGN\xrightarrow{L\otimes c_N}L\otimes N$.
Let $\mathcal B$ be a monoid object of $\mathcal D$. For a $\mathcal B$-module object $N$
([sk-def-sfb-module-objects]), the morphism
$$
S\mathcal B\otimes GN\xrightarrow{\theta_{\mathcal B,N}}G(\mathcal B\otimes N)
\xrightarrow{G\gamma_N}GN
$$
makes $GN$ an $S\mathcal B$-module object, and $Gf$ is $S\mathcal B$-linear for every
$\mathcal B$-linear $f$. This defines the *linearization*
$$
G_{\mathcal B}\colon\Mod_{\mathcal B}(\mathcal D)\to\Mod_{S\mathcal B}(\mathcal C),
$$
which commutes with the forgetful functors.
