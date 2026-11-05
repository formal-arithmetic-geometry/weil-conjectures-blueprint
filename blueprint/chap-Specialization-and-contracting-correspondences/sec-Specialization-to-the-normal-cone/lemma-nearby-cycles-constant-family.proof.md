+++
kind = "proof"
of = "lemma-nearby-cycles-constant-family"
order = 1626
+++
The compatibilities (1) and (2) are formal. For the isomorphism we show
that the cone $C_Y(L)$ of $\sigma_Y(L)$ vanishes. To do this we use that, like nearby
cycles, the cone commutes with smooth pullback and proper direct image.
Smooth pullback lets us check vanishing locally, and it also shows that
the cone vanishes generically, by
reduction to constant coefficients and the calculation $R\Psi_S(M_\eta)=M$.
Proper direct image along a compactified linear projection then shows
that the remaining support is empty, by induction on the dimension of
an affine space containing $Y$.

By the comparison for constructible complexes, we may work on the small
étale site. There $\sigma$ is $\bar i^*$ of the unit of
$\bar j^*\dashv R\bar j_*$ and the base change maps are $\bar i^*$ of
mates, so (1), (2) and naturality follow from the triangle identities.

We take cofibres in the stable $\infty$-category underlying the derived
category, where they are functorial, unlike cones in a triangulated
category, and set
$C_Y(L)=\operatorname{cofib}(\sigma_Y(L))$.  This is an exact functor
with bounded constructible values.  By (1) and (2), the base change maps yield

$$
C_Y(Rf_*L')\simeq Rf_*C_{Y'}(L')\quad(f\text{ proper}),\qquad
C_{Y'}(f^*L)\simeq f^*C_Y(L)\quad(f\text{ smooth}).
$$

By the base change isomorphism for étale maps, the question is local on $Y$.  For
a closed immersion $Y\hookrightarrow\mathbf A^n$, the base change isomorphism for
proper maps identifies the direct image of $C_Y(L)$ with
$C_{\mathbf A^n}$ of the direct image of $L$, and since direct image along a
closed immersion is conservative, it suffices to treat affine
spaces.

For $Y=\mathbf A^n$, the complex $C_Y(L)$ vanishes on a dense open
subset.  Indeed, by the truncation triangles we may assume that $L$ is
a sheaf. After shrinking, it is locally constant, and after pulling
back to a finite étale cover, it is constant. The pullback does no
harm: $C$ commutes with étale pullback, so vanishing can be checked
after a surjective étale pullback.  For a constant sheaf $M$ on a smooth
$k$-scheme, the base change isomorphism for its smooth structure map identifies $C$
with the pullback of $C_{\operatorname{Spec}k}(M)$, which is zero
because $R\Psi_S(M_\eta)=M$.

We argue by induction on $n$, the case of a point being the calculation
above.  By the preceding paragraph, the closure $T$ of the support of
$C_{\mathbf A^n}(L)$ is a proper closed subset.  By the linear form of Noether
normalization there is a linear projection $q:\mathbf A^n\to\mathbf A^{n-1}$
that is finite on $T$: we choose its kernel line so that it avoids the
intersection of the projective closure of $T$ with the hyperplane at
infinity.  Compactifying that line, we get

$$
\bar q:\bar Y=\mathbf P^1\times\mathbf A^{n-1}
\longrightarrow\mathbf A^{n-1},
\qquad v:\mathbf A^n\hookrightarrow\bar Y,
\qquad \bar L=v_!L.
$$

We compactified the line so that the support becomes finite over
$\mathbf A^{n-1}$ and can be detected by direct image there.
As $C$ commutes with restriction to the open subscheme $\mathbf A^n$
of $\bar Y$, the complex $C_{\bar Y}(\bar L)$ is supported on
$T\cup(\bar Y\setminus\mathbf A^n)$.  This union is closed in
$\bar Y$ and finite over $\mathbf A^{n-1}$. Indeed, $T$ is finite, hence
proper, over $\mathbf A^{n-1}$, and therefore closed in $\bar Y$; the
boundary $\bar Y\setminus\mathbf A^n$ is a section.  By the base change isomorphism
for proper maps and the induction hypothesis,

$$
R\bar q_*C_{\bar Y}(\bar L)
\simeq C_{\mathbf A^{n-1}}(R\bar q_*\bar L)=0.
$$

Direct image is conservative on complexes supported on a closed
subscheme finite over the base, since on a geometric stalk the direct
image of each cohomology sheaf is the finite product of its stalks on
the finite fibre.  Therefore $C_{\bar Y}(\bar L)=0$, and restricting to
$\mathbf A^n$ gives $C_{\mathbf A^n}(L)=0$.
