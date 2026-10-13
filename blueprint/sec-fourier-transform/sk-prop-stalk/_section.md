+++
id = "sk-prop-stalk"
kind = "proposition"
title = "P3: the stalks are fibre integrals"
order = 3042
lean = ["AlgebraicGeometry.Etale.fourierTransformStalkIso"]
uses = ["sk-def-as", "sk-def-ft", "sk-def-kernel", "sk-prop-sf-cbc"]
tags = ["sketch"]
+++
Let $S=\Spec k$, $V\cong\mathbf A^r_k$, let $\bar\xi:\Spec\Omega\to V^\vee$
be a geometric point of $V^\vee$, $\Omega$ algebraically closed, and
$K\in\Dbc(V,E)$. Write
$V_{\bar\xi}=(V\times_kV^\vee)\times_{p_2,V^\vee}\bar\xi=V\times_k\Omega$ for
the fibre of $p_2$ over $\bar\xi$: it is $V_{\bar k}$ when $\bar\xi$ is a
$\bar k$-point of $V^\vee$, and for $\bar\xi$ lying over a non-closed point
it is the affine $r$-space over $\Omega\supset\kappa(\bar\xi)$. Then

$$
\bigl(\FT_\psi(K)\bigr)_{\bar\xi}
\cong H^*_c\bigl(V_{\bar\xi},\,K|_{V_{\bar\xi}}\otimes^L\mathcal L_{\psi(\langle x,\xi\rangle)}\bigr)[r],
$$

where $\langle x,\xi\rangle:V_{\bar\xi}\to\mathbf A^{1}$ is the pairing with
the point $\xi$.
