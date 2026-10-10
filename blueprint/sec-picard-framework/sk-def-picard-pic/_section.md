+++
id = "sk-def-picard-pic"
kind = "section"
title = "Picard functor and its $\\sigma$-normalized version"
order = 796
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.picardFunctor", "AlgebraicGeometry.picardFunctorNormalized"]
+++
*Definition (sketch).*

For $f:X\to S$, the *Picard functor* $\Pic_{X/S}$ is the fppf
sheafification of the presheaf $T\mapsto\Pic(X_T)$ on
$(\Sch/S)_{fppf}$. For a section
$\sigma$ of $f$ we also put

$$
\Pic_{X/S,\sigma}(T)=\{\cL\in\Pic(X_T):\sigma_T^*\cL\cong\cO_T\}.
$$

The sections of $\Pic_{X/S}$ are *not* in general given by the
unsheafified quotient: there is a natural map
$\Pic(X_T)/f_T^*\Pic(T)\to\Pic_{X/S}(T)$, but it need not be bijective.
(For an anisotropic smooth conic $X$ over $S=\Spec\mathbf R$ every line
bundle on $X$ has even degree over $\C$, since $X$ has no real point,
whereas the class of $\cO(1)$ on $X_\C$ is Galois-invariant and so is a
section of $\Pic_{X/\mathbf R}(\Spec\mathbf R)$; the obstruction to
descending it as a line bundle is the Brauer class of $X$.) The quotient
formula

$$
\Pic_{X/S}(T)=\Pic(X_T)/f_T^*\Pic(T)
$$

holds for all $T$ when $f$ has a section $\sigma$ and
$\cO_T\to f_{T,*}\cO_{X_T}$ is an isomorphism for every
$T\in\Ob((\Sch/S)_{fppf})$.
