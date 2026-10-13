+++
kind = "proof"
of = "pur9-thm-smooth-purity"
uses = ["pur9-cs-lem-diagonal-square", "pur9-def-section-invariant", "pur9-def-tate-twist", "pur9-dg-lem-diagonal-normal", "pur9-dg-lem-diagonal-regular", "pur9-dnc-def-iso", "pur9-lem-vector-bundle-purity"]
+++
The first isomorphism is $\mu$ of Lemma “The finite-coefficient inverse-image composition comparison is invertible” (`pur713-lem-pull-composition`) for $p_2\Delta=\mathrm{id}$; the second is Lemma [pur9-cs-lem-diagonal-square]; the equality is Definition [pur9-def-section-invariant]. By Lemma [pur9-dg-lem-diagonal-regular] $\Delta$ is a closed section of the smooth $p_1$, so Definition [pur9-dnc-def-iso] applies; by Lemma [pur9-dg-lem-diagonal-normal] its normal bundle is $T=T_{X/Y}$, of rank $d$, with projection $\pi_T$ and zero section $0_T$. The next isomorphism is Lemma [pur9-lem-vector-bundle-purity] for $\pi_T$, via $\gamma_{\pi_T,(\mathcal O_E/\varpi^n)_X}$, and the last is the inverse-image behaviour of twists in Definition [pur9-def-tate-twist] together with $\mu$ for $\pi_T0_T=\mathrm{id}$. Each step is an isomorphism.
