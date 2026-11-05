+++
id = "lemma-artin-schreier-character-sheaf--2"
kind = "lemma"
title = "Multiplication isomorphism"
order = 1220003
aliases = ["bp-r375-2"]
lean = ["AlgebraicGeometry.artinSchreierOf", "AlgebraicGeometry.nonempty_iso_tensorObj_artinSchreierOf"]
+++
For a $k_0$-scheme $X$ and $f\in\Gamma(X,\mathcal O_X)$, put
$\mathcal L_{\psi,f}=f^*\mathcal L_\psi$. For any two global functions
$f,g$ there is an isomorphism of Weil sheaves

$$
\mathcal L_{\psi,f}\otimes_E\mathcal L_{\psi,g}
\simeq\mathcal L_{\psi,f+g}.
$$

Taking $X=\mathbf A^1_{k_0}\times_{k_0}\mathbf A^1_{k_0}$ and $f,g$
to be its two coordinates gives

$$
m^*\mathcal L_\psi\simeq
\operatorname{pr}_1^*\mathcal L_\psi\otimes_E
\operatorname{pr}_2^*\mathcal L_\psi.
$$

The assertion is existence of an isomorphism, with no normalization
at zero imposed.
