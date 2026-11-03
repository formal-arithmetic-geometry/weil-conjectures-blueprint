+++
kind = "proof"
of = "sk-thm-smooth-purity"
uses = ["sk-prop-sp-orientation", "sk-prop-cohsm", "sk-lem-sp-finite-existence", "sk-lem-sp-reduction"]
+++
Choose $n$ with $\ell^nA=0$. Once we extend the Kummer and diagonal classes along
$\mathbf Z/\ell^n\mathbf Z\to A$, the calculation above works with $A$
throughout. The splitting for the projective line has
two free summands, and its integration and triangle identities keep
the same normalization. Hence the local adjunctions compute
$f_A^!$, and the arguments for vector bundles and deformations
show that $\omega_{f,A}\simeq A_X(d)[2d]$. We define $\gamma_{f,A}(K)$
as the composite

$$
f_A^{*}K\otimes^{\mathbf L}A_X(d)[2d]
\xrightarrow{\sim}f_A^{*}K\otimes^{\mathbf L}\omega_{f,A}
\xrightarrow{\sim}f_A^{!}K.
$$

These are the isomorphisms given by the orientation and by (10.9),
and both are natural in $K$.
By (10.16) below, $\gamma_{f,A}$ does not depend
on the choice of $n$ and is compatible with maps of finite rings.
