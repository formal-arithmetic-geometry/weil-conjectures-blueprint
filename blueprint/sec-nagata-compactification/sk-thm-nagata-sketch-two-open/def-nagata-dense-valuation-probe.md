+++
id = "def-nagata-dense-valuation-probe"
kind = "definition"
title = "Valuation probe through a schematically dense source"
order = 288
lean = ["AlgebraicGeometry.ValuativeCommSqWithPt", "AlgebraicGeometry.ValuativeCommSqWithPt.ofIsDominant"]
uses = ["def-nagata-scheme-theoretic-image"]
+++
Let $h\colon T\to P$ be a morphism of schemes and let $z\in P$. A
*valuation probe* of $h$ at $z$ consists of a valuation ring $A'$ with
fraction field $K'$, a morphism $\eta\colon\operatorname{Spec}(K')\to T$,
and a morphism $\alpha\colon\operatorname{Spec}(A')\to P$ such that the
square

$$
\begin{array}{ccc}
\operatorname{Spec}(K')&\xrightarrow{\eta}&T\\
\big\downarrow&&\big\downarrow h\\
\operatorname{Spec}(A')&\xrightarrow{\alpha}&P
\end{array}
$$

commutes and $\alpha$ maps the closed point of $\operatorname{Spec}(A')$ to
$z$. When $h$ is quasi-compact and dominant, write

$$
\mathsf{VP}(h,z)=
(A'_{h,z},K'_{h,z},\eta_{h,z},\alpha_{h,z})
$$

for a chosen valuation probe of $h$ at $z$.
