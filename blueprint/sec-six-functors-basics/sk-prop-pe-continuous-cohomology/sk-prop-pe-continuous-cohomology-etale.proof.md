+++
kind = "proof"
of = "det-pe-continuous-cohomology-etale"
+++
*First isomorphism.* Write $\Gamma_{\mathrm{cont}}=\varprojlim\circ\Gamma^{\mathbf N}$,
where $\Gamma^{\mathbf N}\colon\Sh(X_{\Et})^{\mathbf N}\to\Ab^{\mathbf N}$ applies
$\Gamma(X_{\Et},-)$ levelwise and $\varprojlim\colon\Ab^{\mathbf N}\to\Ab$. The
functor $\Gamma^{\mathbf N}$ is right adjoint to the levelwise constant-sheaf
functor, which is exact, so $\Gamma^{\mathbf N}$ preserves injectives. By the
Grothendieck composite-functor theorem,
$R\Gamma_{\mathrm{cont}}=R\varprojlim\circ R\Gamma^{\mathbf N}$. An injective object
of $\Sh(X_{\Et})^{\mathbf N}$ is levelwise injective (evaluation at $n$ has the exact left adjoint sending $G$ to the system with $G$
in levels $m\leq n$, identity transitions among them, and $0$ in levels $m>n$; a
map from this system to $(H_m)$ is determined by its level-$n$ component), so $R\Gamma^{\mathbf N}((G_n))$ is the system
$(R\Gamma(X_{\Et},G_n))_n$ in $D(\Ab^{\mathbf N})$. On $D(\Ab^{\mathbf N})$ the
derived functor of $\varprojlim$ is computed by the triangle
$R\varprojlim K\to\prod_nK_n\xrightarrow{1-\text{shift}}\prod_nK_n$, since this
holds for injective systems (whose transition maps are split surjective) and
both sides are triangulated. This gives the first isomorphism.

*Second isomorphism.* The cohomology comparison
([lem-weil-pbc-comparison-global-cohomology], [sk-prop-sf-comparison]) gives
natural isomorphisms $R\Gamma(X_{\Et},F_{n,\Et})\simeq R\Gamma(X_{\Proet},F_n)$,
compatible with the transition maps, hence an isomorphism of the derived limits
(the defining triangles are functorial in the system).

*Third isomorphism.* This is [det-pe-continuous-cohomology-limit] with $W=X$,
using that $\nu_X^*$ preserves epimorphisms.
