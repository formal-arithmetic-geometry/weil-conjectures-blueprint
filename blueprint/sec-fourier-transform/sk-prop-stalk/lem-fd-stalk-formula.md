+++
id = "lem-fd-stalk-formula"
kind = "lemma"
title = "Stalks of the transform are fibre integrals"
order = 3037
lean = ["AlgebraicGeometry.Etale.fourierTransformStalkIso"]
uses = ["def-fd-kernel", "def-fd-transform", "def-weil-pbc-qbar-category", "thm-cbc-finite-extension", "thm-cbc-qbar"]
+++
Let $S=\operatorname{Spec}k$, $V\cong\mathbf A^r_k$, let $\bar\xi:\operatorname{Spec}\Omega\to V^\vee$ be a geometric point of $V^\vee$ with $\Omega$ algebraically closed, and let $K\in D^b_c(V,E)$. Write $V_{\bar\xi}=(V\times_kV^\vee)\times_{p_2,V^\vee}\bar\xi=V\times_k\Omega$ for the fibre of $p_2$ over $\bar\xi$ (it is $V_{\bar k}$ when $\bar\xi$ is a $\bar k$-point of $V^\vee$; for $\bar\xi$ over a non-closed point it is the affine $r$-space over $\Omega\supset\kappa(\bar\xi)$). Then

$$
(\operatorname{FT}_\psi(K))_{\bar\xi}\cong H^*_c\bigl(V_{\bar\xi},\,K|_{V_{\bar\xi}}\otimes^L\mathcal L_{\psi(\langle x,\xi\rangle)}\bigr)[r],
$$

where $\langle x,\xi\rangle:V_{\bar\xi}\to\mathbf A^1$ is the pairing with the point $\xi$.
