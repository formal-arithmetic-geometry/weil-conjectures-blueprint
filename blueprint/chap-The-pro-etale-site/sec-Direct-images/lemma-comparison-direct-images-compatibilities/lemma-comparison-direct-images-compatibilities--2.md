+++
id = "lemma-comparison-direct-images-compatibilities--2"
kind = "lemma"
title = "Compatibilities of the comparison of direct images (2)"
name_showing = false
order = 136003
aliases = ["bp-r039-2"]
lean = ["_private.WeilConjectures.SixFunctors.ProEtale.BaseChange.ComparisonCounit.0.AlgebraicGeometry.ProEtale.ComparisonCore.comparison_counit_plus"]
uses = ["proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "theorem-comparison-direct-images"]
+++
Let $\Lambda$ be a commutative ring, and work with sheaves of ordinary
$\Lambda$-modules on the two sites. Let $g:X\to Y$ be a morphism of
schemes and $K\in D^+(X_{\acute{e}t},\Lambda)$. Write $c_g$ for the
right derived transformation induced by the canonical comparison
$\nu_Y^*g_{\acute{e}t,*}\to g_{\mathrm{pro}\acute{e}t,*}\nu_X^*$, and obtain
$\beta_g:g_{\mathrm{pro}\acute{e}t}^*\nu_Y^*\simeq\nu_X^*g_{\acute{e}t}^*$
by applying the pullback comparison termwise to complexes. Then the composite

$$
\nu_X^*g_{\acute{e}t}^*Rg_{\acute{e}t,*}K
\xrightarrow{\beta_g^{-1}}
g_{\mathrm{pro}\acute{e}t}^*\nu_Y^*Rg_{\acute{e}t,*}K
\xrightarrow{g_{\mathrm{pro}\acute{e}t}^*c_g}
g_{\mathrm{pro}\acute{e}t}^*Rg_{\mathrm{pro}\acute{e}t,*}\nu_X^*K
\xrightarrow{\varepsilon_{\mathrm{pro}\acute{e}t}}\nu_X^*K
$$

equals $\nu_X^*$ applied to the counit
$g_{\acute{e}t}^*Rg_{\acute{e}t,*}K\to K$. Equivalently, precomposing with
$\beta_g$ gives the counit identity in part (2) of the lemma.
