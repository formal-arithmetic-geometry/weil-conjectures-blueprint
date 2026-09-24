+++
id = "lemma-weil-pbc-epsilon-direct-image-site-comparison"
kind = "lemma"
title = "Site-local components of direct-image comparison"
order = 1819
uses = ["def-weil-pbc-epsilon-direct-image-comparison", "lemma-weil-pbc-epsilon-scheme-naturality"]
+++
Suppose $Y$ is affine and let
$W=\varprojlim_iW_i$ be an affine pro-etale object, with $W_i\to Y$ affine
etale and affine transition maps. Put
$X_i=X\times_YW_i$ and $X_W=X\times_YW$. Then

$$
\begin{aligned}
(\epsilon_Y^{-1}f_{\mathrm{et},*}F)(W)
&=\varinjlim_i\Gamma(X_i,F),\\
(f_{\mathrm{proet},*}\epsilon_X^{-1}F)(W)
&=\Gamma(X_W,\epsilon_{X_W}^{-1}g_{\mathrm{et}}^{-1}F),
\end{aligned}
$$

where $g:X_W\to X$. Under these identifications, $\delta_{f,F}(W)$ is the
map induced by pullback from the finite stages. Such $W$ form a covering
basis of $Y_{\mathrm{proet}}$.

## Proof

The first equality is the left-Kan-extension formula for
$\epsilon_Y^{-1}$: the subsystem of the displayed affine etale stages is
cofinal among etale objects receiving a map from $W$. The second equality is
the definition of pro-etale direct image, followed by the scheme-naturality
identification of the restricted inverse image. Expanding the adjoint of
$f_{\mathrm{et},*}\eta^X_F$ shows that a section over $X_i$ is pulled back to
$X_W$; hence its filtered-colimit map is exactly $\delta_{f,F}(W)$. Every
pro-etale object over affine $Y$ admits a cover by inverse limits of this
form, so these evaluations detect sheaf isomorphisms.
