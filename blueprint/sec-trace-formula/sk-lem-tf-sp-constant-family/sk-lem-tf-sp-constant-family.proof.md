+++
kind = "proof"
of = "sk-lem-tf-sp-constant-family"
uses = ["sk-thm-pe-constructible-comparison"]
+++
The cofibre of $\sigma_Y$ is compatible with proper direct image and smooth pullback. This
reduces the lemma to affine spaces, where the cofibre vanishes on a dense open, and an induction
on the dimension, projecting along a line that is finite on the support, removes the rest.

By the constructible comparison [sk-thm-pe-constructible-comparison] we may work on the small
étale site. Work in a derived enhancement and put
$B_Y(L)=\operatorname{cofib}(\sigma_Y(L))$. This is an exact functor with bounded constructible
values. The exchanges give

$$
B_Y(Rf_*L')\simeq Rf_*B_{Y'}(L')\quad(f\text{ proper}),\qquad
B_{Y'}(f^*L)\simeq f^*B_Y(L)\quad(f\text{ smooth}).
$$

Smooth exchange for étale maps makes the question local on $Y$. A closed immersion
$Y\hookrightarrow\mathbf A^n$ and the faithfulness of its direct image reduce it to all affine
spaces.

For $Y=\mathbf A^n$, the complex $B_Y(L)$ vanishes on a dense open subset. To see this, use the
truncation triangles to reduce to a sheaf, shrink until it is locally constant, and pass to a
finite étale cover that makes it constant. Smooth base change for the smooth structure map to
$\operatorname{Spec}k$ reduces the assertion there to $R\Psi_S(M_\eta)=M$. Surjective étale
pullback detects vanishing.

Induct on $n$, with the point calculation as base. Let $T$ be the closure of the support of
$B_{\mathbf A^n}(L)$; it is a proper closed subset by the preceding paragraph. Choose a linear
projection $q:\mathbf A^n\to\mathbf A^{n-1}$ finite on $T$. Such a projection exists by the
linear form of Noether normalization: choose its kernel line to avoid the intersection of the
projective closure of $T$ with the hyperplane at infinity. Compactify that line to obtain

$$
\bar q:\bar Y=\mathbf P^1\times\mathbf A^{n-1}\longrightarrow\mathbf A^{n-1},
\qquad v:\mathbf A^n\hookrightarrow\bar Y,
\qquad \bar L=v_!L.
$$

By locality, $B_{\bar Y}(\bar L)$ is supported on $T\cup(\bar Y\setminus\mathbf A^n)$. This union
is closed in $\bar Y$ and finite over $\mathbf A^{n-1}$: $T$ is already finite, hence proper over
that base and therefore closed in $\bar Y$, and the boundary is one section. Proper exchange and
the induction hypothesis give

$$
R\bar q_*B_{\bar Y}(\bar L)\simeq B_{\mathbf A^{n-1}}(R\bar q_*\bar L)=0.
$$

Direct image is conservative on complexes supported on a closed subscheme finite over the base.
On a geometric stalk the direct image of each cohomology sheaf is the finite product of its
stalks on the finite fibre, so a zero direct image forces all those stalks to be zero. It follows
that $B_{\bar Y}(\bar L)=0$; restrict to $\mathbf A^n$. The compatibility assertions hold because
all maps used here are the specified adjunction units and their exchange mates.
