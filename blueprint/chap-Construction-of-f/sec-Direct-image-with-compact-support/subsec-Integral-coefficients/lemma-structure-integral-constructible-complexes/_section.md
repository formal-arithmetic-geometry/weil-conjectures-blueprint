+++
id = "lemma-structure-integral-constructible-complexes"
kind = "lemma"
title = "Structure of integral constructible complexes"
order = 491
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isConstructibleModuleObject_serre_padicIntegersRingObj"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "lemma-constructible-sheaves"]
+++
1. $\Dbc(X,\mathcal O_E)$ is a triangulated subcategory of
   $D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ of bounded objects, stable under truncation;
   its objects in degree $0$ form the category $\Cons(X,\mathcal O_E)$, an
   essentially small abelian subcategory of $\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$
   closed under extensions.
2. For $C\in\Cons(X,\mathcal O_E)$ there is a finite stratification on
   whose strata $C$ is pro-étale locally
   $\mathcal O_{E,S}\otimes_{\mathcal O_E}P$, with $P$ finitely generated.
3. On each such stratum $C$ is dualizable of Tor amplitude $[-1,0]$, and
   its dual has Tor amplitude $[0,1]$.
