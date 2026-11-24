+++
id = "prose-09-07"
kind = "hidden"
title = "The tensor product map"
order = 736
+++
With finite coefficients, smooth purity says that for $f$ smooth of pure
relative dimension $d$ the [exceptional inverse image $f^!$](@theorem-existence-exceptional-inverse-image) is the ordinary
inverse image, twisted by [$(d)$](@definition-tate-twists) and shifted by $[2d]$
(Proposition [proposition-smooth-purity-finite-coefficients]). The
first step is the map $f^*K\otimes^{\mathbf L}\href{@definition-relative-dualizing-complex}{\omega_f}\to \href{@theorem-existence-exceptional-inverse-image}{f^!K}$, an isomorphism by
Proposition [proposition-exceptional-inverse-image-smooth-morphism](2),
which reduces the problem to the single complex [$\omega_f$](@definition-relative-dualizing-complex).

Fix $n\geq1$. We carry out the geometric calculation with
coefficients $\mathbf Z/\ell^n\mathbf Z$, and until Section [sec-ell-adic-coefficients-4] we
omit the subscript, so that $f^*$, [$Rf_!$](@proposition-construction-independence-rf-shriek), [$f^!$](@theorem-existence-exceptional-inverse-image), [$\omega_f$](@definition-relative-dualizing-complex) and [$\gamma_f$](@theorem-smooth-purity-all-admissible-coefficients)
refer to this cyclic coefficient ring. Afterwards the calculation extends along
$\mathbf Z/\ell^n\mathbf Z\to A$ when $\ell^nA=0$, and in this way
Proposition [proposition-smooth-purity-finite-coefficients] gives the
result for every finite admissible ring $A$.

Let $f:X\to Y$ be smooth of pure relative dimension $d$ and
$K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{Y_{\mathrm{pro}\acute{e}t}},\mathbf Z/\ell^n\mathbf Z)$. From the projection
formula and the counit $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@definition-relative-dualizing-complex}{\omega_{f}}\to(\mathbf Z/\ell^n\mathbf Z)_{Y}$
we get $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\bigl(f^{*}K\otimes^{\mathbf L}\href{@definition-relative-dualizing-complex}{\omega_{f}}\bigr)
\simeq K\otimes^{\mathbf L} \href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@definition-relative-dualizing-complex}{\omega_{f}}\to K$, whose adjoint is
the canonical map

$$
\mu_{f,K}:f^{*}K\otimes^{\mathbf L}_{(\mathbf Z/\ell^n\mathbf Z)_{X}}\href{@definition-relative-dualizing-complex}{\omega_{f}}
\longrightarrow \href{@theorem-existence-exceptional-inverse-image}{f^{!}K}.
\tag{9.4}
$$

To construct the orientation, we compare [$\omega$](@definition-relative-dualizing-complex) on the fibres of a family of
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
and the [exceptional base change map](@definition-exceptional-base-change-map)

$$
g'^{*}\href{@theorem-existence-exceptional-inverse-image}{f^{!}K}\xrightarrow{\sim}\href{@theorem-existence-exceptional-inverse-image}{(f')^{!}g^{*}K}
\tag{9.6}
$$

are isomorphisms for $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{Y_{\mathrm{pro}\acute{e}t}},\mathbf Z/\ell^n\mathbf Z)$, and
they are compatible with each other. Moreover, on a chart $f|_U=p_d\circ e$ we have
$\href{@definition-relative-dualizing-complex}{\omega_f}|_U\simeq\href{@definition-tate-twists}{(\mathbf Z/\ell^n\mathbf Z)_U(d)}[2d]$. Hence
$\href{@definition-relative-dualizing-complex}{\omega_f}[-2d]$ is a locally constant sheaf of free
$\mathbf Z/\ell^n\mathbf Z$-modules of rank one.
