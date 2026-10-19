+++
kind = "proof"
of = "sk-lem-tf-sp-thick-origin"
uses = ["sk-lem-tf-sp-dnc-functorial", "sk-lem-tf-sp-constant-family"]
+++
Use the contraction $H\colon X\times\mathbf A^1\to X$, $H(x,a)=ax$, and write
$H_a=H(-,a)\colon X\to X$ for $a\in k$. It maps $Z\times\mathbf A^1$ schematically into $Z$, since
$H^*(x^m)=a^mx^m\in(x^m)$; this inclusion of ideals is the hypothesis of
[sk-lem-tf-sp-dnc-functorial], so all $H_a$ lift to the deformations. Moreover
$H_1=\operatorname{id}$, and $H_0$ factors through $Z$ and restricts to the identity on
$Z_{\mathrm{red}}$. Set $E=e^*\operatorname{Sp}_{X,Z}(M_X)$. Pullback exchange for these lifts
induces endomorphisms $\phi_a:E\to E$, with $\phi_1=\operatorname{id}_E$.

There is one endomorphism $\phi$ on the pullback of $E$ to $Z\times\mathbf A^1$ whose fibre at $a$
is $\phi_a$. To construct it, apply pullback exchange for $H:X\times\mathbf A^1\to X$ and then
invert the smooth exchange for the projection to $X$; flat base change identifies its deformation
with $\mathcal D_ZX\times\mathbf A^1$. The restrictions of $H$ and the projection from
$Z\times\mathbf A^1$ induce the same reduced map to $Z$; nilpotent invariance therefore identifies
$H_Z^*E$ with $\operatorname{pr}_Z^*E$, naturally in $E$. This is the identification making the
family an endomorphism of that one pullback. Compatibility with composition identifies the fibre
endomorphisms with those just constructed.

Since $Z_{\mathrm{red}}$ is a point, nilpotent invariance identifies $D^b_c(Z_{\mathrm{\acute et}},A)$
with the bounded derived category of finite $A$-modules. Pullback along the projection
$p\colon Z\times\mathbf A^1\to Z$ is fully faithful on this category: the affine-line calculation
and the hypercohomology spectral sequence give $R\Gamma(\mathbf A^1,p^*B)=B$ for every such bounded
complex $B$, and adjunction gives full faithfulness. Hence $\phi$ is the pullback of a single
endomorphism of $E$, and its two restrictions $\phi_0$ and $\phi_1$ coincide.

It remains to identify $\phi_0$. Let $\alpha:M_Z\to E$ be the restriction of the nearby-cycle unit
for the constant sheaf on $\mathcal D_ZX$. Naturality and $H_0:X\to Z\hookrightarrow X$ give

$$
\phi_0=\alpha\,\epsilon_{X,Z}(M_X),\qquad
\epsilon_{X,Z}(M_X)\,\alpha=\operatorname{id}_{M_Z}.
$$

The second equality is the specialization unit for the constant family $Z\times S$
([sk-lem-tf-sp-constant-family]), followed by its fixed inverse. Since
$\phi_0=\phi_1=\operatorname{id}_E$, the maps $\alpha$ and $\epsilon_{X,Z}(M_X)$ are inverse
isomorphisms.
