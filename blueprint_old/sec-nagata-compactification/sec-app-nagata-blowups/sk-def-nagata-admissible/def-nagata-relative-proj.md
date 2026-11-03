+++
id = "def-nagata-relative-proj"
kind = "definition"
title = "Relative Proj"
lean = ["AlgebraicGeometry.Scheme.GradedAlgebraData.relProj", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProjHom", "AlgebraicGeometry.Scheme.GradedAlgebraData.relProj\u03b9"]
order = 58
uses = ["def-nagata-affine-proj"]
+++
Let $X$ be a scheme. A *quasi-coherent graded $\mathcal O_X$-algebra*
$\mathcal A$ consists of an $\mathbb N$-graded
$\Gamma(V,\mathcal O_X)$-algebra
$\mathcal A(V)=\bigoplus_{n\geq0}\mathcal A(V)_n$ for every affine open
$V\subseteq X$, and degree-preserving ring homomorphisms
$\operatorname{res}_{U,V}\colon\mathcal A(V)\to\mathcal A(U)$ for affine
opens $U\subseteq V$, with $\operatorname{res}_{V,V}=\mathrm{id}$ and
$\operatorname{res}_{U,V}\circ\operatorname{res}_{V,W}=\operatorname{res}_{U,W}$,
such that every $\operatorname{res}_{U,V}$ is a coefficientwise base change:
$\Gamma(U,\mathcal O_X)\otimes_{\Gamma(V,\mathcal O_X)}\mathcal A(V)_n
\cong\mathcal A(U)_n$ for all $n$.

For affine opens $U\subseteq V$, the graded homomorphism
$\operatorname{res}_{U,V}$ induces a morphism
$\operatorname{Proj}(\mathcal A(U))\to\operatorname{Proj}(\mathcal A(V))$,
compatible with the structure morphisms
$\operatorname{Proj}(\mathcal A(V))\to\operatorname{Spec}\mathcal A(V)_0
\to\operatorname{Spec}\Gamma(V,\mathcal O_X)\cong V$. This gives a diagram
$V\mapsto\operatorname{Proj}(\mathcal A(V))$ on the poset of all affine opens
of $X$. The *relative Proj* $\operatorname{Proj}_X(\mathcal A)$ is the scheme
obtained by gluing this diagram, i.e. its colimit, with the chart morphisms
$\iota_V\colon\operatorname{Proj}(\mathcal A(V))\to\operatorname{Proj}_X(\mathcal A)$
and the structure morphism
$\pi\colon\operatorname{Proj}_X(\mathcal A)\to X$ glued from the structure
morphisms $\operatorname{Proj}(\mathcal A(V))\to V\subseteq X$.
