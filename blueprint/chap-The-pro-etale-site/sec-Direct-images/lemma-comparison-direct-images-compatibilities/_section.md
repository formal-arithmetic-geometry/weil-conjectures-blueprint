+++
id = "lemma-comparison-direct-images-compatibilities"
kind = "lemma"
title = "Compatibilities of the comparison of direct images"
order = 136
lean = ["AlgebraicGeometry.ProEtale.comparisonDirectImagePlus_comp", "AlgebraicGeometry.ProEtale.fixedComparisonDirectImageMatePlus_counit"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "theorem-comparison-direct-images"]
+++
Let $g:X\to Y$ be a morphism of schemes.

1. For $L\in D^+(Y_{\acute{e}t},\Lambda)$, the composite
   $\href{@proposition-comparison-morphism-inverse-image}{\nu_Y^*L}\to\href{@proposition-comparison-morphism-inverse-image}{\nu_Y^*}Rg_{\acute{e}t,*}g_{\acute{e}t}^*L\xrightarrow{c_g}
  \href{@proposition-topos-functoriality}{Rg_{\mathrm{pro}\acute{e}t,*}}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}g_{\acute{e}t}^*L$ of [$\nu_Y^*$](@proposition-comparison-morphism-inverse-image) of the unit with $c_g$
   equals the unit $\href{@proposition-comparison-morphism-inverse-image}{\nu_Y^*L}\to \href{@proposition-topos-functoriality}{Rg_{\mathrm{pro}\acute{e}t,*}}\href{@proposition-topos-functoriality}{g_{\mathrm{pro}\acute{e}t}^*}\href{@proposition-comparison-morphism-inverse-image}{\nu_Y^*L}$
   followed by $\href{@proposition-topos-functoriality}{Rg_{\mathrm{pro}\acute{e}t,*}}(\beta_g)$.
2. For $K\in D^+(X_{\acute{e}t},\Lambda)$, the composite
   $\href{@proposition-topos-functoriality}{g_{\mathrm{pro}\acute{e}t}^*}\href{@proposition-comparison-morphism-inverse-image}{\nu_Y^*}Rg_{\acute{e}t,*}K\xrightarrow{g^*c_g}
  \href{@proposition-topos-functoriality}{g_{\mathrm{pro}\acute{e}t}^*}\href{@proposition-topos-functoriality}{Rg_{\mathrm{pro}\acute{e}t,*}}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K}\to\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K}$ with the counit equals
   [$\nu_X^*$](@proposition-comparison-morphism-inverse-image) of the counit $g_{\acute{e}t}^*Rg_{\acute{e}t,*}K\to K$ precomposed with
   $\beta_g$.
3. For a second morphism $h:Y\to Z$, under the identifications
   $R(h\circ g)_*\simeq Rh_*Rg_*$ on both sites, $c_{h\circ g}$ is the
   composite
   $$
   \href{@proposition-comparison-morphism-inverse-image}{\nu_Z^*}Rh_{\acute{e}t,*}Rg_{\acute{e}t,*}K\xrightarrow{c_h}
   \href{@proposition-topos-functoriality}{Rh_{\mathrm{pro}\acute{e}t,*}}\href{@proposition-comparison-morphism-inverse-image}{\nu_Y^*}Rg_{\acute{e}t,*}K\xrightarrow{\href{@proposition-topos-functoriality}{Rh_{\mathrm{pro}\acute{e}t,*}}(c_g)}
   \href{@proposition-topos-functoriality}{Rh_{\mathrm{pro}\acute{e}t,*}}\href{@proposition-topos-functoriality}{Rg_{\mathrm{pro}\acute{e}t,*}}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K} .
   $$
