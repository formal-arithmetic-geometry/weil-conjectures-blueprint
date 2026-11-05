+++
id = "lemma-comparison-direct-images-compatibilities--3"
kind = "lemma"
title = "Compatibilities of the comparison of direct images (3)"
name_showing = false
order = 136004
aliases = ["bp-r039-3"]
lean = []
uses = ["proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "theorem-comparison-direct-images"]
+++
This direct-image composition identity is bypassed by the Lean proof of the main theorem; the comparison of base-change maps instead uses counit compatibility and coherence of the pullback comparison around a commutative square.

For a second morphism $h:Y\to Z$, under the identifications
$R(h\circ g)_*\simeq Rh_*Rg_*$ on both sites, $c_{h\circ g}$ is the
composite

$$
\nu_Z^*Rh_{\acute{e}t,*}Rg_{\acute{e}t,*}K\xrightarrow{c_h}
Rh_{\mathrm{pro}\acute{e}t,*}\nu_Y^*Rg_{\acute{e}t,*}K\xrightarrow{Rh_{\mathrm{pro}\acute{e}t,*}(c_g)}
Rh_{\mathrm{pro}\acute{e}t,*}Rg_{\mathrm{pro}\acute{e}t,*}\nu_X^*K .
$$
