+++
id = "def-sfb-modobj-linearization"
kind = "definition"
title = "Linearization of a functor with a projection formula"
order = 1158
uses = ["def-sfb-projection-formula", "det-def-sfb-module-objects-definition"]
lean = ["CategoryTheory.Functor.ProjectionFormula.mapModLeft"]
+++
Let $\pi$ be a projection formula for $P\colon\mathcal C\to\mathcal D$ relative to a strong
monoidal $S\colon\mathcal D\to\mathcal C$ ([def-sfb-projection-formula]). Let
$\mathcal B$ be a monoid object of $\mathcal D$, so $S\mathcal B$ is a monoid object of
$\mathcal C$. For an $S\mathcal B$-module object $M$ ([det-def-sfb-module-objects-definition]), the
morphism
$$
\mathcal B\otimes PM\xrightarrow{\pi^{-1}_{\mathcal B,M}}P(S\mathcal B\otimes M)
\xrightarrow{P\gamma_M}PM
$$
makes $PM$ a $\mathcal B$-module object, and $Pf$ is $\mathcal B$-linear for every
$S\mathcal B$-linear $f$. This defines the *linearization*
$$
P_{\mathcal B}\colon\Mod_{S\mathcal B}(\mathcal C)\to\Mod_{\mathcal B}(\mathcal D),
$$
which commutes with the forgetful functors.
