+++
kind = "proof"
of = "pur9-cs-lem-bc-dualizing"
uses = ["pur7710-lem-constructible-equivalence", "pur7710-lem-origin-stalk-detection", "pur9-cs-input-constructible-closure", "pur9-cs-input-phi-local", "pur9-input-preservation"]
+++
Both objects lie in $D^b_c(X'_{\Proet},\mathcal O_E/\varpi^n)$ by Inputs [pur9-input-preservation] and [pur9-cs-input-constructible-closure], so by Lemmas [pur7710-lem-constructible-equivalence] and [pur7710-lem-origin-stalk-detection] it suffices to check étale geometric stalks, and as in the proof of Lemma [pur9-cs-lem-tensor-formula] it suffices to check after restriction to the charts $X_x$ and their base changes. On a chart, Input [pur9-cs-input-bc-phi] with $K=(\mathcal O_E/\varpi^n)_Y$ and Input [pur9-cs-input-phi-local] identify the restricted map with the map for $p_d$ and its base change, pulled back along the étale $v_x$; by Input [pur9-cs-input-bc-model] the latter is an isomorphism.
