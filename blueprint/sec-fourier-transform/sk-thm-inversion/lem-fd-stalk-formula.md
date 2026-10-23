+++
id = "lem-fd-stalk-formula"
kind = "lemma"
title = "Stalks of the transform are fibre integrals"
order = 3949
uses = ["def-fd-kernel", "def-fd-transform", "det-def-sfb-bounded-constructible", "sk-thm-sfb-shriek-base-change", "sk-prop-sf-cbc"]
+++
Let $S$ be a separated finite-type $k_0$-scheme, $V\to S$ a vector bundle of rank $r$ with dual $V^\vee$, let $\bar\xi:\operatorname{Spec}\Omega\to V^\vee$ be a geometric point of $V^\vee$ with $\Omega$ algebraically closed, lying over the geometric point $\bar s$ of $S$, and let $K\in D^b_c(V,\Lambda)$ for $\Lambda=E$ or $\Lambda=\overline{\mathbf Q}_\ell$, the bounded constructible subcategory of $D(V_{\mathrm{proét}},\Lambda)$ ([det-def-sfb-bounded-constructible]). Write $V_{\bar\xi}=(V\times_SV^\vee)\times_{p_2,V^\vee}\bar\xi=V\times_S\operatorname{Spec}\Omega$ for the fibre of $p_2$ over $\bar\xi$, an affine $r$-space over $\Omega$ (for $S=\operatorname{Spec}k$ and $V\cong\mathbf A^r_k$ it is $V_{\bar k}$ when $\bar\xi$ is a $\bar k$-point of $V^\vee$, and the affine $r$-space over $\Omega\supset\kappa(\bar\xi)$ otherwise). Then

$$
(\operatorname{FT}_\psi(K))_{\bar\xi}\cong H^*_c\bigl(V_{\bar\xi},\,K|_{V_{\bar\xi}}\otimes^L\mathcal L_{\psi(\langle x,\xi\rangle)}\bigr)[r],
$$

where $\langle x,\xi\rangle:V_{\bar\xi}\to\mathbf A^1$ is the pairing with the point $\xi$, a linear form on $V_{\bar\xi}$.
