+++
id = "prose-10-08"
kind = "hidden"
title = "Tensor formula, base change, orientation plan"
order = 3298
+++
The proof of Theorem [sk-thm-purity-transport] for finite coefficients has two parts. The local part says that
$f^!K\simeq f^*K\otimes^{\mathbf L}\omega_f$ and that $\omega_f$ is
isomorphic to $(\mathbf Z/\ell^n\mathbf Z)(d)[2d]$ on each coordinate
chart. This part, together with base change, was proved in
Section “Torsion coefficients: the strategy”, but it does not say whether the isomorphisms on
charts agree on overlaps. The global part is an orientation of
$\omega_f$ defined without charts, which we construct from the diagonal in
the next subsubsection. We then check that it restricts to the isomorphisms on
charts.

Let $f:X\to Y$ be smooth of pure relative dimension $d$ and
$K\in\Dctf(Y_{\mathrm{pro\acute et}},\mathbf Z/\ell^n\mathbf Z)$. From the projection
formula and the counit $Rf_!\omega_{f}\to(\mathbf Z/\ell^n\mathbf Z)_{Y}$
we get $Rf_!\bigl(f^{*}K\otimes^{\mathbf L}\omega_{f}\bigr)
\simeq K\otimes^{\mathbf L} Rf_!\omega_{f}\to K$, whose adjoint is
the canonical map

$$
f^{*}K\otimes^{\mathbf L}_{(\mathbf Z/\ell^n\mathbf Z)_{X}}\omega_{f}
      \longrightarrow f^{!}K.
$$

To construct the orientation, we compare $\omega$ on the fibres of a family of
sections, and for this we need base change. Consider a cartesian square

$$
\begin{CD}
 X' @>{g'}>> X\\
 @V{f'}VV @VV{f}V\\
 Y' @>{g}>> Y,
\end{CD}
$$

with $f$ smooth of pure relative dimension $d$. For
$K\in\Dctf(Y_{\mathrm{pro\acute et}},\mathbf Z/\ell^n\mathbf Z)$, pulling back the
counit $Rf_!f^{!}K\to K$ along $g$ and using base change for compactly
supported direct image, we obtain a morphism $Rf'_!g'^{*}f^{!}K\to g^{*}K$. Its adjoint under
$Rf'_!\dashv f'^!$ is the *exceptional base change map*
$g'^*f^!K\to f'^!g^*K$.

By Proposition [sk-prop-cohsm](2) and (3), with
$\Lambda=\mathbf Z/\ell^n\mathbf Z$, the canonical map
$f^{*}K\otimes^{\mathbf L}\omega_{f}\to f^{!}K$ above
and the exceptional base change map

$$
g'^{*}f^{!}K\xrightarrow{\sim}(f')^{!}g^{*}K
$$

are isomorphisms for $K\in\Dctf(Y_{\mathrm{pro\acute et}},\mathbf Z/\ell^n\mathbf Z)$, and
they are compatible with each other. On a chart $f|_U=p_d\circ e$ we have
$\omega_f|_U\simeq(\mathbf Z/\ell^n\mathbf Z)_U(d)[2d]$, so $\omega_f[-2d]$
is a locally constant sheaf of free $\mathbf Z/\ell^n\mathbf Z$-modules of
rank one.

Since $f^!K\simeq f^*K\otimes^{\mathbf L}\omega_f$, it remains, for finite coefficients, to construct
a single global isomorphism
$\omega_f\simeq(\mathbf Z/\ell^n\mathbf Z)_X(d)[2d]$.
We obtain it from the diagonal
$\Delta:X\to X\times_YX$, which is a section of the smooth projection
$p_1$. Deformation to the normal bundle moves $\Delta$ to the zero
section of the relative tangent bundle $T_{X/Y}$, where
Proposition [sk-prop-an] provides the
isomorphism.

The deformation argument works for any section of a smooth morphism.
