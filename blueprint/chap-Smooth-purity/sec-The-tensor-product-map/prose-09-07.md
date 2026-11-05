+++
id = "prose-09-07"
kind = "hidden"
title = "The tensor product map"
order = 735
+++
With finite coefficients, smooth purity says that for $f$ smooth of pure
relative dimension $d$ the exceptional inverse image $f^!$ is the ordinary
inverse image, twisted by $(d)$ and shifted by $[2d]$
(Proposition [proposition-smooth-purity-finite-coefficients]). The
first step is the map $f^*K\otimes^{\mathbf L}\omega_f\to f^!K$, an isomorphism by
Proposition [proposition-exceptional-inverse-image-smooth-morphism](2),
which reduces the problem to the single complex $\omega_f$.

Fix $n\geq1$. We carry out the geometric calculation with
coefficients $\mathbf Z/\ell^n\mathbf Z$, and until Section [sec-ell-adic-coefficients-4] we
omit the subscript, so that $f^*$, $Rf_!$, $f^!$, $\omega_f$ and $\gamma_f$
refer to this cyclic coefficient ring. Afterwards the calculation extends along
$\mathbf Z/\ell^n\mathbf Z\to A$ when $\ell^nA=0$, and in this way
Proposition [proposition-smooth-purity-finite-coefficients] gives the
result for every finite admissible ring $A$.

Let $f:X\to Y$ be smooth of pure relative dimension $d$ and
$K\in D^b_{\mathrm{ctf}}(Y_{\mathrm{pro}\acute{e}t},\mathbf Z/\ell^n\mathbf Z)$. From the projection
formula and the counit $Rf_!\omega_{f}\to(\mathbf Z/\ell^n\mathbf Z)_{Y}$
we get $Rf_!\bigl(f^{*}K\otimes^{\mathbf L}\omega_{f}\bigr)
\simeq K\otimes^{\mathbf L} Rf_!\omega_{f}\to K$, whose adjoint is
the canonical map

$$
\mu_{f,K}:f^{*}K\otimes^{\mathbf L}_{(\mathbf Z/\ell^n\mathbf Z)_{X}}\omega_{f}
\longrightarrow f^{!}K.
\tag{9.4}
$$

To construct the orientation, we compare $\omega$ on the fibres of a family of
sections, and for this we need base change. Consider a cartesian square

$$
\begin{CD}
X' @>{g'}>> X\\
@V{f'}VV @VV{f}V\\
Y' @>{g}>> Y,
\end{CD}
\tag{9.5}
$$

with $f$ smooth of pure relative dimension $d$. For it we have the exceptional
base change map of Definition [definition-exceptional-base-change-map].
By Proposition [proposition-exceptional-inverse-image-smooth-morphism](2) and (3), with
$\Lambda=\mathbf Z/\ell^n\mathbf Z$, the map (9.4)
and the exceptional base change map

$$
g'^{*}f^{!}K\xrightarrow{\sim}(f')^{!}g^{*}K
\tag{9.6}
$$

are isomorphisms for $K\in D^b_{\mathrm{ctf}}(Y_{\mathrm{pro}\acute{e}t},\mathbf Z/\ell^n\mathbf Z)$, and
they are compatible with each other. Moreover, on a chart $f|_U=p_d\circ e$ we have
$\omega_f|_U\simeq(\mathbf Z/\ell^n\mathbf Z)_U(d)[2d]$. Hence
$\omega_f[-2d]$ is a locally constant sheaf of free
$\mathbf Z/\ell^n\mathbf Z$-modules of rank one.
