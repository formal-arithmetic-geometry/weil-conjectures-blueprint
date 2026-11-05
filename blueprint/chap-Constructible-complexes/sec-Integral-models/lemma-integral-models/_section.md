+++
id = "lemma-integral-models"
kind = "lemma"
title = "Integral models"
order = 294
lean = ["AlgebraicGeometry.ProEtale.IntegralModelsStacks.completion_transport", "AlgebraicGeometry.ProEtale.IntegralModelsStacks.integral_models_stacks", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_leftDerivedUpperStar_obj_of_scheme", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_tensorObj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_openImmersionLowerShriek_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightDerivedLowerStar_of_isClosedImmersion"]
uses = ["definition-small-pro-etale-site", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves"]
+++
1. Restriction of scalars along the map from the constant sheaf
   $\mathcal O_E$ to $\mathcal O_{E,X}$ is an equivalence between the
   derived complete objects of $D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ and the derived
   complete complexes of modules over the constant sheaf $\mathcal O_E$.
2. An object $K$ of $D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ lies in
   $\Dbc(X,\mathcal O_E)$ if and only if its restriction of scalars lies in
   $\Dc(X,\mathcal O_E)$.
3. $\Dbc(-,\mathcal O_E)$ is preserved by
   $f^*:D(Y_{\mathrm{pro}\acute{e}t},\mathcal O_E)\to D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$
   for every morphism $f:X\to Y$, by
   $\otimes^{\mathbf L}_{\mathcal O_{E,X}}$ on $D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$,
   and by
   $a_!:D(S_{\mathrm{pro}\acute{e}t},\mathcal O_E)\to D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ for
   every locally closed immersion $a:S\hookrightarrow X$.
4. Every object of $\Dbc(X,E)$ is obtained by finitely many cones and
   shifts from objects $(a_!L_0)[1/\ell]$, where $a:S\hookrightarrow X$ is
   a locally closed immersion and $L_0$ is a lisse
   $\mathcal O_{E,S}$-module that is locally free of finite rank. Every object of $\Dbc(X,\overline{\mathbf Q}_\ell)$ is obtained in
   the same way from the objects $\QbarX\otimes_{\mathcal O_{E,X}}a_!L_0$,
   for some finite $E/\mathbf Q_\ell$.
