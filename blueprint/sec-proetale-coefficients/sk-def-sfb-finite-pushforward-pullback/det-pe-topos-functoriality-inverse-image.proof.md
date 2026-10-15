+++
kind = "proof"
of = "det-pe-topos-functoriality-inverse-image"
+++
*1.* If $V\to Y$ is weakly étale, its base change $V\times_YX\to X$ is weakly étale, so
$u$ is well defined. Base change carries $\mathrm{id}_Y$ to $\mathrm{id}_X$ and
$V_1\times_{V}V_2$ to $(V_1\times_YX)\times_{V\times_YX}(V_2\times_YX)$, so it preserves the
terminal object and fibre products, hence all finite limits. Pro-étale coverings are
stable under base change along $X\to Y$: fpqc coverings are stable under arbitrary base
change of schemes (Stacks Project, Topologies, fpqc coverings), and weakly étale morphisms are stable under base
change, as in part 1 of [det-pe-topos-functoriality-site].

*2.* Since $u$ preserves coverings and fibre products, $G\circ u$ satisfies the sheaf
condition for every sheaf $G$, as in [def-sfb-finite-lower-star]. The left Kan extension
along $u^{\mathrm{op}}$ is left adjoint to restriction $G\mapsto G\circ u$ on presheaves,
and sheafification is left adjoint to the inclusion of sheaves; composing these
adjunctions gives $\Hom(f^{-1}F,G)\cong\Hom(\operatorname{Lan}F,G)\cong\Hom(F,G\circ u)$.

*3.* As a left adjoint $f^{-1}$ preserves colimits. For finite limits: the category
$(u\downarrow T)$ indexing the pointwise Kan extension at $T\in X_{\mathrm{proét}}$ has
objects $(V,T\to u(V))$; since $Y_{\mathrm{proét}}$ has finite limits and $u$ preserves
them, the opposite of this category is filtered (it has the object $(Y,T\to X)$, and
cones over finite diagrams are given by limits in $Y_{\mathrm{proét}}$). Hence
$\operatorname{Lan}_{u^{\mathrm{op}}}F(T)=\varinjlim F(V)$ is a filtered colimit, which
commutes with finite limits of sets. Sheafification is left exact. So $f^{-1}$ preserves
finite limits.

*4.* A functor preserving finite products preserves abelian group objects, so $f^{-1}$
carries abelian sheaves to abelian sheaves, and its restriction is left adjoint to $f_*$
on abelian sheaves. It preserves kernels (finite limits) and cokernels (as a left adjoint),
hence is exact.

*5.* $(g\circ f)_*G=G\circ u_{g\circ f}$ and $g_*f_*G=G\circ u_f\circ u_g$; the canonical
isomorphisms $(W\times_ZY)\times_YX\cong W\times_ZX$ give a natural isomorphism
$u_f\circ u_g\cong u_{g\circ f}$, whence $(g\circ f)_*\cong g_*\circ f_*$ (compare
[def-sfb-finite-lower-star-comp]). Left adjoints of isomorphic functors are canonically
isomorphic, so $(g\circ f)^{-1}\cong f^{-1}\circ g^{-1}$, compatibly with the adjunctions.
