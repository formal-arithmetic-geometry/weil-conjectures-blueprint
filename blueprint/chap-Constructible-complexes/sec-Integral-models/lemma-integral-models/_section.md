+++
id = "lemma-integral-models"
kind = "lemma"
title = "Integral models"
order = 294
lean = ["AlgebraicGeometry.ProEtale.IntegralConstantCompletion.integral_constant_completion"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "theorem-existence-contractible-covers", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "lemma-constructible-sheaves"]
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
