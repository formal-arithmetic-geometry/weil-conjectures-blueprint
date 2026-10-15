+++
id = "sk-def-picard-pic"
kind = "definition"
title = "Relative Picard functor"
order = 603
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.picardFunctor", "AlgebraicGeometry.picardFunctorNormalized"]
tags = ["sketch"]
+++
For a morphism of schemes $f:C\to S$, let

$$
\operatorname{Pic}_{C/S}
=\bigl(T\longmapsto\operatorname{Pic}(C_T)/f_T^*\operatorname{Pic}(T)\bigr)^{\mathrm{fppf}}.
$$

Here $C_T=C\times_ST$ and the superscript denotes sheafification on the
big fppf site of $S$. Equivalently one may sheafify
$T\mapsto\operatorname{Pic}(C_T)$, since an invertible sheaf on $T$
becomes trivial on a Zariski cover. When this functor is represented by
a scheme, we call the representing scheme the *Picard scheme*.

Sheafification is needed: invertible sheaves satisfy effective descent,
but automorphisms can prevent their isomorphism classes from forming a
sheaf, so neither the displayed quotient nor
$T\mapsto\operatorname{Pic}(C_T)$ need be an fppf sheaf (Stacks Project,
Tag 0B9L). (For instance, for an anisotropic smooth conic $C$ over
$S=\Spec\mathbf R$, the class of $\cO(1)$ on $C_\C$ is Galois-invariant,
hence a section of $\operatorname{Pic}_{C/\mathbf R}(\Spec\mathbf R)$,
but it does not come from a line bundle on $C$.)

*Notation.* For a section $\sigma$ of $f$ we write
$\operatorname{Pic}_{C/S,\sigma}(T)=\{\cL\in\operatorname{Pic}(C_T):\sigma_T^*\cL\cong\cO_T\}$
for the subgroup of classes trivial along $\sigma$; in the presence of a
section, the lemma *Rigidification along a section* describes
the sheafification directly through it.
