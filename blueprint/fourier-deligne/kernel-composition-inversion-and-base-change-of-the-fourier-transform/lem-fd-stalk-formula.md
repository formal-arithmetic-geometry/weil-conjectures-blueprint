+++
id = "lem-fd-stalk-formula"
kind = "lemma"
title = "Stalks of the transform are fibre integrals"
order = 4152
uses = ["def-fd-kernel", "def-fd-transform", "def-weil-pbc-qbar-category", "prop-weil-pbc-strict-henselization-stalk-formula", "sbc-thm-overline-mathbf-q-ell-coefficient-smooth-base-ch", "thm-weil-pbc-qbar"]
+++
Let $S=\operatorname{Spec}k$, $V\cong\mathbf A^r_k$, let $\bar\xi$ be a geometric point of $V^\vee$, and let $K\in D^b_c(V,E)$. Then

$$
(\operatorname{FT}_\psi(K))_{\bar\xi}\cong H^*_c\bigl(V_{\bar k},\,K\otimes^L\mathcal L_{\psi(\langle x,\xi\rangle)}\bigr)[r].
$$

## Proof

By the strict-henselization stalk formula of [prop-weil-pbc-strict-henselization-stalk-formula] (in the $\overline{\mathbf Q}_\ell$-form of the coefficient category of [def-weil-pbc-qbar-category]), applied to the compact-support direct image, the stalk at $\bar\xi$ is the compactly supported cohomology of the strict-local fibre

$$
V_{\bar k}\times_k\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{V^\vee,\bar\xi}.
$$

The kernel restricted to this fibre is the pullback of the geometric-fibre kernel $K\otimes^L\mathcal L_{\psi(\langle x,\xi\rangle)}$ along the projection to $V_{\bar k}$: the pairing restricts to $\langle x,\xi\rangle$, the Artin–Schreier sheaf is lisse, and the base change of the twist is the twist by the base-changed function ([def-fd-kernel]). The base change morphism $\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{V^\vee,\bar\xi}\to\operatorname{Spec}k$ is a limit of etale morphisms, hence smooth, so the $\overline{\mathbf Q}_\ell$-coefficient smooth base change of [sbc-thm-overline-mathbf-q-ell-coefficient-smooth-base-ch], applied to the cartesian square formed by the structure morphisms of $V_{\bar k}$ and of its strict-local fibre, identifies the compactly supported cohomology over the strict-local fibre with the compactly supported cohomology of the geometric fibre; the compact-support base change along the proper compactification of the affine part is [thm-weil-pbc-qbar] in the $\overline{\mathbf Q}_\ell$-form. With the shift $[r]$ of [def-fd-transform], this is the displayed formula.
