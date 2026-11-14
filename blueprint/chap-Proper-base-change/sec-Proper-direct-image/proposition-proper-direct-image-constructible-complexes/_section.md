+++
id = "proposition-proper-direct-image-constructible-complexes"
kind = "proposition"
title = "Proper direct image of constructible complexes"
order = 425
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.finiteProperBaseChange", "AlgebraicGeometry.ProEtale.CondensedRing.integralProperDirectImageAndFormulas"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-comparison-morphism-inverse-image", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "definition-pro-etale-base-change-map", "definition-projection-formula-map"]
+++
Let $p:X\to Y$ be proper and let $\Lambda$ be admissible.

1. $Rp_*:D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$ maps
   $D^b_{\mathrm{ctf}}(X,\Lambda)$ into $D^b_{\mathrm{ctf}}(Y,\Lambda)$.
2. For a cartesian square with $g:Y'\to Y$, $g':X'\to X$ and
   $p':X'\to Y'$, the base change map (4.5)
   $g^*Rp_*\to Rp'_*g'^*$ is an isomorphism of functors
   $D^b_{\mathrm{ctf}}(X,\Lambda)\to D^b_{\mathrm{ctf}}(Y',\Lambda)$.
3. The projection formula map (4.14)
   is an isomorphism for $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and $M\in D^b_{\mathrm{ctf}}(Y,\Lambda)$.
