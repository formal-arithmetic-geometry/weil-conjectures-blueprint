+++
kind = "proof"
of = "det-sp-finite-general-ring"
+++
(1) The ring map $\mathbf Z/\ell^n\to A$ is a map of finite rings killed by a
power of $\ell$, so [det-sp-reduction-exceptional] applies and
$c_{\mathbf Z/\ell^n,A}((\mathbf Z/\ell^n)_Y)$ is an isomorphism; the
extension of scalars of $(\mathbf Z/\ell^n)_X(d)[2d]$ is $A_X(d)[2d]$ because
the Tate sheaf is free of rank one, so its derived and ordinary extensions
agree ([det-sp-scalar-extension-functor]).

(2) The direct construction with $A$-coefficients uses the Kummer class, the
diagonal class and the projective-line splitting into two free summands,
each extended along $\mathbf Z/\ell^n\to A$; the integration and triangle
identities hold with the same normalization. Hence the local adjunctions over
$A$ are the scalar extensions of those over $\mathbf Z/\ell^n$, which is the
chart description of $c_{\mathbf Z/\ell^n,A}$ in
[det-sp-reduction-exceptional]. The vector-bundle and deformation steps
involve only rank-one locally free sheaves and the geometry of the deformation
space, which do not depend on coefficients, and the comparisons are determined
by their normalization at $t=1$; so the two orientations agree on charts and,
being maps of locally constant rank-one sheaves (after removing the shift),
agree globally.

(3) The orientation is an isomorphism by (1), the tensor map is an isomorphism
by the tensor formula [thm-pur-cohomological-smoothness] with
$A$-coefficients, and the twist reassociation is canonical; naturality in $K$
holds factorwise. If $\ell^{n'}A=0$ with $n'\geq n$, the orientation built from
$\mathbf Z/\ell^{n'}$ is the extension of scalars of the one built from
$\mathbf Z/\ell^n$ along $\mathbf Z/\ell^{n'}\to\mathbf Z/\ell^n\to A$, by the
composition compatibility of the coefficient comparisons; hence $\gamma_{f,A}$
is independent of $n$.
