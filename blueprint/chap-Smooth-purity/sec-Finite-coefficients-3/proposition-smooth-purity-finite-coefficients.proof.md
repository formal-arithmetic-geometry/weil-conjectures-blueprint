+++
kind = "proof"
of = "proposition-smooth-purity-finite-coefficients"
order = 753
uses = ["proposition-exceptional-inverse-image-smooth-morphism", "proposition-relative-dualizing-complex"]
+++
The calculation so far was made with coefficients $\mathbf Z/\ell^n\mathbf Z$,
and every ingredient in it extends along $\mathbf Z/\ell^n\mathbf Z\to A$,
where we choose $n$ with $\ell^nA=0$. Once the Kummer and diagonal classes are
extended, the calculation works with $A$ throughout. The splitting for the
projective line has two free summands. Its integration and triangle
identities keep the same normalization, since
(9.9) is an identity of endomorphisms of a
constant sheaf and is preserved by extension of scalars. So the local
adjunctions compute $f_A^!$. The arguments for vector bundles and
deformations then show that $\omega_{f,A}\simeq A_X(d)[2d]$. We define $\gamma_{f,A}(K)$
as the composite

$$
f_A^{*}K\otimes^{\mathbf L}A_X(d)[2d]
\xrightarrow{\sim}f_A^{*}K\otimes^{\mathbf L}\omega_{f,A}
\xrightarrow{\sim}f_A^{!}K.
$$

These are the isomorphisms given by the orientation and by (9.4),
and both are natural in $K$.
By (9.17) below, $\gamma_{f,A}$ does not depend
on the choice of $n$ and is compatible with maps of finite rings.
