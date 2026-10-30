+++
kind = "proof"
of = "sk-lem-tf-sp-constant-family"
uses = ["sk-thm-pe-constructible-comparison"]
+++
By the comparison for constructible complexes, we may work on the small
étale site. We work in a derived enhancement and set
$C_Y(L)=\operatorname{cofib}(\sigma_Y(L))$. This is an exact functor
with bounded constructible values. The base change maps yield

$$
C_Y(Rf_*L')\simeq Rf_*C_{Y'}(L')\quad(f\text{ proper}),\qquad
C_{Y'}(f^*L)\simeq f^*C_Y(L)\quad(f\text{ smooth}).
$$

By the base change isomorphism for étale maps, the question is local on $Y$. For
a closed immersion $Y\hookrightarrow\mathbf A^n$, the base change isomorphism for
proper maps identifies the direct image of $C_Y(L)$ with
$C_{\mathbf A^n}$ of the direct image of $L$, and direct image along a
closed immersion is conservative. Hence it suffices to treat affine
spaces.

For $Y=\mathbf A^n$, the complex $C_Y(L)$ vanishes on a dense open
subset. To see this, we use the truncation triangles to reduce to a
sheaf, shrink until it is locally constant, and pass to a finite
étale cover on which it is constant; this is allowed because $C$
commutes with étale pullback, so that vanishing can be checked after a
surjective étale pullback. For a constant sheaf $M$ on a smooth
$k$-scheme, the base change isomorphism for its smooth structure map identifies $C$
with the pullback of $C_{\operatorname{Spec}k}(M)$, which is zero
because $R\Psi_S(M_\eta)=M$.

We argue by induction on $n$, the case of a point being the calculation
above. Let $T$ be the closure of the support of $C_{\mathbf A^n}(L)$.
By the preceding paragraph, it is a proper closed subset. Choose a
linear projection $q:\mathbf A^n\to\mathbf A^{n-1}$ that is finite on
$T$. Such a projection exists by the linear form of Noether
normalization: we choose its kernel line so that it avoids the
intersection of the projective closure of $T$ with the hyperplane at
infinity. Compactifying that line, we get

$$
\bar q:\bar Y=\mathbf P^1\times\mathbf A^{n-1}
\longrightarrow\mathbf A^{n-1},
\qquad v:\mathbf A^n\hookrightarrow\bar Y,
\qquad \bar L=v_!L.
$$

By locality, $C_{\bar Y}(\bar L)$ is supported on
$T\cup(\bar Y\setminus\mathbf A^n)$. Since $T$ is finite, hence proper,
over $\mathbf A^{n-1}$, it is closed in $\bar Y$, and the boundary
$\bar Y\setminus\mathbf A^n$ is a section. Hence this union is closed in
$\bar Y$ and finite over $\mathbf A^{n-1}$. By the base change isomorphism for proper maps and the
induction hypothesis, we find that

$$
R\bar q_*C_{\bar Y}(\bar L)
\simeq C_{\mathbf A^{n-1}}(R\bar q_*\bar L)=0.
$$

Direct image is conservative on complexes supported on a closed
subscheme finite over the base. Indeed, on a geometric stalk the direct
image of each cohomology sheaf is the finite product of its stalks on
the finite fibre, and hence if the direct image is zero, all those
stalks are zero. It follows that $C_{\bar Y}(\bar L)=0$, and we
conclude by restricting to $\mathbf A^n$.
The compatibility assertions hold because all maps used here are the
specified adjunction units and their mates.
