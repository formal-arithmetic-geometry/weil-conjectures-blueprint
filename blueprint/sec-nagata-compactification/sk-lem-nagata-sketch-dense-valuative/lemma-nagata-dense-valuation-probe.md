+++
id = "lemma-nagata-dense-valuation-probe"
kind = "lemma"
title = "Properties of the valuation probe"
order = 280
lean = ["AlgebraicGeometry.ValuativeCommSqWithPt.ofIsDominant"]
uses = ["def-nagata-dense-valuation-probe"]
+++
Let $h\colon T\to P$ be quasi-compact and dominant, and let $z\in P$. Then
$h$ has a valuation probe at $z$; in particular the maps in
$\mathsf{VP}(h,z)$ form a commutative diagram

$$
\begin{array}{ccc}
\operatorname{Spec}(K'_{h,z})&\xrightarrow{\eta_{h,z}}&T\\
\big\downarrow&&\big\downarrow h\\
\operatorname{Spec}(A'_{h,z})&\xrightarrow{\alpha_{h,z}}&P,
\end{array}
$$

and the closed point of $\operatorname{Spec}(A'_{h,z})$ maps to $z$.
