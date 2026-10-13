+++
kind = "proof"
of = "pur713-lem-pull-composition-module"
uses = ["pur713-def-derived-pull-module", "pur713-lem-extension-kflat"]
+++
Let $P\to M$ be a K-flat resolution. The complex $(u^{-1}_{\mathbf Z})_{\mathcal R_{X,T}}P$ is K-flat by Input [pur713-input-kflat-transport], and extension of scalars preserves K-flat complexes by Lemma [pur713-lem-extension-kflat]. Hence $u^*_TP$ is K-flat. Therefore $Lu^*_TM$ is represented by $u^*_TP$, $Lv^*_TLu^*_TM$ by $v^*_Tu^*_TP$, and $L(uv)^*_TM$ by $(uv)^*_TP$, by Definition [pur713-def-derived-pull-module]. The termwise isomorphism $\sigma_{u,v,T,P}$ is a map between these representatives; it is natural in $P$ and compatible with maps of K-flat resolutions, so by the universal property of the total left derived functors it defines a natural isomorphism, independent of the resolution, and it is the only natural transformation with the stated values.
