+++
id = "pur9-input-reduction-monoidal"
kind = "remark"
title = "Reduction commutes with inverse image and tensor product"
order = 2222
tags = ["latex:bpinput"]
uses = ["pur713-def-open-projection", "pur713-lem-monoidal-pullback"]
+++
For every morphism $g:W'\to W$ of $k$-schemes of finite type there are natural isomorphisms $r^*_g:\mathrm{red}_{n,m}Lg^*_{\mathcal O_E/\varpi^n}\cong Lg^*_{\mathcal O_E/\varpi^m}\mathrm{red}_{n,m}$ and $r^\otimes_{A,B}:\mathrm{red}_{n,m}(A\otimes^L_{\mathcal O_E/\varpi^n}B)\cong\mathrm{red}_{n,m}A\otimes^L_{\mathcal O_E/\varpi^m}\mathrm{red}_{n,m}B$, induced on K-flat resolutions by the evident sheaf isomorphisms, such that $r^*_g$ is compatible with the monoidal comparisons of Lemma [pur713-lem-monoidal-pullback] through $r^\otimes$, with the composition comparisons of Lemma “The finite-coefficient inverse-image composition comparison is invertible” (`pur713-lem-pull-composition`), and with the open-extension maps $\sigma$ of Definition [pur713-def-open-projection] (through the identification $\mathrm{red}_{n,m}\mathrm D(j_{!,\mathcal O_E/\varpi^n})\cong\mathrm D(j_{!,\mathcal O_E/\varpi^m})\mathrm{red}_{n,m}$ induced by the exactness of extension by zero). *Status:* not established here; it requires that the sheaf inverse images preserve K-flat complexes (Input “Fixed-coefficient inverse image preserves K-flat complexes” (`pur713-input-kflat-fixed`)) and a check of the listed coherence diagrams.
