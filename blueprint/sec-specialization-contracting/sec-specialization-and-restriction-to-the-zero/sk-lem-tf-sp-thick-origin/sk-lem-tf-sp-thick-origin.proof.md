+++
kind = "proof"
of = "sk-lem-tf-sp-thick-origin"
uses = ["sk-lem-tf-sp-dnc-functorial", "sk-lem-tf-sp-constant-family"]
+++
The contraction $x\mapsto ax$ joins the identity
($a=1$) to a map that factors through $Z$ ($a=0$). The endomorphisms of
$z^*\operatorname{Sp}_{X,Z}(M_X)$ that these maps induce form a family
over $\mathbf A^1$, which is constant because $\mathbf A^1$ has the
cohomology of a point. Comparing the two ends shows that
$\tau_{X,Z}(M_X)$ has an inverse.

Consider the contraction $h:X\times\mathbf A^1\to X$, $h(x,a)=ax$,
and write $h_a=h(-,a):X\to X$ for $a\in k$. It maps
$Z\times\mathbf A^1$ schematically into $Z$, since
$h^*(x^m)=a^m x^m\in(x^m)$. This inclusion of ideals is the hypothesis
of Lemma [sk-lem-tf-sp-dnc-functorial], and hence all $h_a$ lift to the
deformations. Moreover, $h_1=\operatorname{id}$, and $h_0$ factors
through $Z$ and restricts to the identity on $Z_{\mathrm{red}}$. Set $N=z^*\operatorname{Sp}_{X,Z}(M_X)$.
The base change maps for pullback along these lifts induce endomorphisms
$\phi_a:N\to N$, with $\phi_1=\operatorname{id}_N$.

There is one endomorphism $\phi$ of the pullback of $N$ to
$Z\times\mathbf A^1$ whose fibre at $a$ is $\phi_a$. To construct it,
we apply the base change map for pullback along $h:X\times\mathbf A^1\to X$
and then invert the base change map for the projection to $X$, which is
smooth. Here we use that, by flat base change, the deformation of
$X\times\mathbf A^1$ is $\mathcal D_ZX\times\mathbf A^1$. The restrictions of $h$ and
of the projection to $Z\times\mathbf A^1$ induce the same map to $Z$ on
reduced schemes. Therefore, by invariance under nilpotent thickenings,
$h_Z^*N$ is identified with $\operatorname{pr}_Z^*N$, naturally in $N$.
Using this identification, we view the family as an endomorphism of a
single pullback. By compatibility with composition, its fibres are the
endomorphisms $\phi_a$ constructed above.

Since $Z_{\mathrm{red}}$ is a point, invariance under nilpotent
thickenings identifies $D^b_c(Z_{\acute et},A)$ with the bounded derived
category of finite $A$-modules. Pullback along the projection
$p:Z\times\mathbf A^1\to Z$ is fully faithful on this category.
Indeed, the calculation for the affine line and the hypercohomology
spectral sequence show that $R\Gamma(\mathbf A^1,p^*B)=B$ for every such
bounded complex $B$, and full faithfulness follows by adjunction.
Hence $\phi$ is the pullback of a single endomorphism of $N$, and its
two restrictions $\phi_0$ and $\phi_1$ coincide.

It remains to identify $\phi_0$. Let
$\alpha:M_Z\to N$ be the restriction of the unit of nearby cycles for
the constant sheaf on $\mathcal D_ZX$. By naturality, and since $h_0$
factors as $X\to Z\hookrightarrow X$, we get

$$
\phi_0=\alpha\tau_{X,Z}(M_X),\qquad
\tau_{X,Z}(M_X)\alpha=\operatorname{id}_{M_Z}.
$$

The second equality holds because the composite is the specialization
map for the constant family $Z\times S$, followed by its fixed inverse. Since
$\phi_0=\phi_1=\operatorname{id}_N$, the maps $\alpha$ and
$\tau_{X,Z}(M_X)$ are inverse isomorphisms.
