+++
id = "sk-prop-cohsm"
kind = "proposition"
title = "Cohomological smoothness"
order = 1991
uses = ["sk-prop-a1", "sk-prop-an", "sk-prop-sf-cbc"]
lean = ["AlgebraicGeometry.Etale.isInvertible_dualizingComplex", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_obj_derivedTensor", "AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_comp_rightDerivedUpperShriek"]
tags = ["sketch"]
+++
Let $\Lambda$ be a finite commutative ring equipped with Tate twists
$\Lambda(m)$, and let $f:X\to Y$ be a separated morphism, smooth of pure
relative dimension $d$, admitting a compactification, such that the exponent
of $\Lambda$ is invertible on $X$. Then:

1. **(a)** $\omega_f=Rf^{!}\Lambda_Y$ is *invertible*: there is an object
$M$ of $D(X_{\mathrm{et}},\Lambda)$ with
$\omega_f\otimes^{\mathbb L}M\cong\Lambda_X$;
1. **(b)** *tensor formula:* for every
$K\in D^b_{ctf}(Y,\Lambda)$ there is an isomorphism
$Lf^{*}K\otimes^{\mathbb L}\omega_f\ \cong\ Rf^{!}K$;
1. **(c)** *smooth base change for $R^{!}$:* for every Cartesian
square
$$
\begin{array}{ccc}
X'&\xrightarrow{\ u\ }&X\\
{\scriptstyle f'}\downarrow&&\downarrow{\scriptstyle f}\\
Y'&\xrightarrow{\ v\ }&Y
\end{array}
$$
with $v$ arbitrary and $f'$ admitting a compactification, there is a natural
isomorphism of functors $D(Y_{\mathrm{et}},\Lambda)\to D(X'_{\mathrm{et}},\Lambda)$
$$
Lu^{*}\circ Rf^{!}\ \cong\ Rf'^{!}\circ Lv^{*};
$$
in particular $Lu^{*}\omega_f\cong\omega_{f'}$, and in the diagonal square
($X'=X\times_YX$, $u=p_2$, $v=f$, $f'=p_1$, and symmetrically)
$\omega_{p_1}\cong Lp_2^{*}\omega_f$, $\omega_{p_2}\cong Lp_1^{*}\omega_f$.
