+++
kind = "proof"
of = "pur713-lem-monoidal-pullback-module"
uses = ["pur713-input-kflat-transport", "pur713-lem-extension-kflat", "pur713-lem-module-pull-monoidal"]
+++
By Lemma [pur713-lem-module-pull-monoidal], $f^*_T$ is strong symmetric monoidal on module objects. Its two factors preserve K-flat complexes by Input [pur713-input-kflat-transport] and Lemma [pur713-lem-extension-kflat]. Compute the comparisons on K-flat resolutions of $M,N$; their tensor product is K-flat, so these comparisons compute both sides. The coherence diagrams are the corresponding underived diagrams on these resolutions and hence remain commutative after localization.
