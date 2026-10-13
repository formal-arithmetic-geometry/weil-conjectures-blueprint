+++
kind = "proof"
of = "pur9-lem-push-projection-reduction"
uses = ["pur713-lem-monoidal-pullback", "pur9-def-reduction-push", "pur9-rem-determination"]
+++
Compare adjoints under $Lp^*_{\mathcal O_E/\varpi^m}\dashv Rp_{*,\mathcal O_E/\varpi^m}$. By Definition [pur713-def-star-projection], $P$ is the adjoint of the monoidal comparison of the derived inverse image (Lemma [pur713-lem-monoidal-pullback]) followed by the counit tensored with the identity, and by Definition [pur9-def-reduction-push], $r_*$ is the adjoint of $(r^*)^{-1}$ followed by the reduced counit. Substituting, each side becomes a map

$$
Lp^*_{\mathcal O_E/\varpi^m}\mathrm{red}_{n,m}\bigl(Rp_{*,\mathcal O_E/\varpi^n}M\otimes^L_{\mathcal O_E/\varpi^n}L\bigr)\to\mathrm{red}_{n,m}M\otimes^L_{\mathcal O_E/\varpi^m}Lp^*_{\mathcal O_E/\varpi^m}\mathrm{red}_{n,m}L
$$

that moves $\mathrm{red}_{n,m}$ past the inverse images and tensor products by $r^*,r^\otimes$, applies the monoidal comparison of $Lp^*_{\mathcal O_E/\varpi^n}$ or $Lp^*_{\mathcal O_E/\varpi^m}$, and applies $\varepsilon_{p,M}\otimes1$ (left side) or $\mathrm{red}(\varepsilon_{p,M})\otimes1$ (right side) at the corresponding stage. The coherence of $r^*$ with the monoidal comparisons in Input [pur9-input-reduction-monoidal], and naturality of $r^\otimes$ applied to $\varepsilon_{p,M}\otimes1$, identify the two maps. The adjunction bijection gives the equality. The argument proves equality of the specified maps; it does not use agreement on generators (Remark [pur9-rem-determination]).
