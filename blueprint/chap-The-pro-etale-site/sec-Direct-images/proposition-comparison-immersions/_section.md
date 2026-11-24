+++
id = "proposition-comparison-immersions"
kind = "proposition"
title = "Comparison for immersions"
order = 139
lean = ["AlgebraicGeometry.ProEtale.rightDerivedLowerShriekOfCompactificationComparisonIso"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-compactification-refinement"]
+++
1. For an open immersion $j:U\hookrightarrow X$, there is a canonical
   isomorphism
   $$
   \href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}j_{\acute{e}t,!}\simeq j_{\mathrm{pro}\acute{e}t,!}\href{@proposition-comparison-morphism-inverse-image}{\nu_U^*}\quad\text{of functors }\operatorname{Mod}(U_{\acute{e}t},\Lambda)\to\operatorname{Mod}(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda),
   \tag{2.10}
   $$
   and hence of functors $D(U_{\acute{e}t},\Lambda)\to D(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)$.
2. For a closed immersion $i:Z\hookrightarrow X$, the map
   (2.9) is an isomorphism
   $\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}Ri_{\acute{e}t,*}\simeq \href{@proposition-topos-functoriality}{Ri_{\mathrm{pro}\acute{e}t,*}}\href{@proposition-comparison-morphism-inverse-image}{\nu_Z^*}$ of functors
   $D^+(Z_{\acute{e}t},\Lambda)\to D^+(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)$, and
   $\href{@proposition-topos-functoriality}{i_{\mathrm{pro}\acute{e}t}^*}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}\simeq\href{@proposition-comparison-morphism-inverse-image}{\nu_Z^*}i_{\acute{e}t}^*$. For $K\in D^+(X_{\acute{e}t},\Lambda)$,
   these isomorphisms and (2.10) carry
   [$\nu_X^*$](@proposition-comparison-morphism-inverse-image) of the localization triangle
   $j_{\acute{e}t,!}j_{\acute{e}t}^*K\to K\to Ri_{\acute{e}t,*}i_{\acute{e}t}^*K\to$ to a distinguished
   triangle
   $j_{\mathrm{pro}\acute{e}t,!}\href{@proposition-topos-functoriality}{j_{\mathrm{pro}\acute{e}t}^*}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K}\to\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K}\to \href{@proposition-topos-functoriality}{Ri_{\mathrm{pro}\acute{e}t,*}}\href{@proposition-topos-functoriality}{i_{\mathrm{pro}\acute{e}t}^*}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K}\to$
   whose first two maps are the counit and the unit of the adjunctions
   $j_!\dashv j^*$ and $i^*\dashv Ri_*$ on [$X_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site).
3. Let $f:X\to Y$ be a separated morphism of finite type with a
   factorization $f=\bar f\circ j$, where $j$ is an open immersion and
   $\bar f$ is proper. Then there is a canonical isomorphism
   $\href{@proposition-comparison-morphism-inverse-image}{\nu_Y^*}R\bar f_{\acute{e}t,*}j_{\acute{e}t,!}\simeq \href{@proposition-topos-functoriality}{R\bar f_{\mathrm{pro}\acute{e}t,*}}j_{\mathrm{pro}\acute{e}t,!}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}$
   of functors $D^+(X_{\acute{e}t},\Lambda)\to D^+(\href{@definition-small-pro-etale-site}{Y_{\mathrm{pro}\acute{e}t}},\Lambda)$.
