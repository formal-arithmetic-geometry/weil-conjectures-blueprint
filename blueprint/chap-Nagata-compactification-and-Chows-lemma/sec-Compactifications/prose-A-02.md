+++
id = "prose-A-02"
kind = "hidden"
title = "Compactifications (1)"
order = 1395
+++
To show that $Rp_*j_!$ does not depend on the compactification, we must
compare two of them, and in general neither maps to the other. The plane
$\mathbf A^2$ is open in $\mathbf P^2$ and in
$\mathbf P^1\times\mathbf P^1$, but the identity of $\mathbf A^2$ extends
to a morphism in neither direction: the map
$(x:y:z)\mapsto((x:z),(y:z))$ is undefined at $(1:0:0)$ and $(0:1:0)$,
and its inverse is undefined at $(\infty,\infty)$. What exists is a third
compactification mapping to both, here the closure of $\mathbf A^2$ in
$\mathbf P^2\times\mathbf P^1\times\mathbf P^1$. So we compare two
compactifications through a common refinement. A refinement $h$ is
required to satisfy $h^{-1}(X)=X$. This is what lets us compute
$Rh_*j'_!$ by restriction to $X$ in the proof of
Proposition [proposition-construction-independence-rf-shriek].

Without density, refinements are not unique. For example, the point
$X=\operatorname{Spec}k$ is open in the compactification
$\operatorname{Spec}k\sqcup\mathbf P^1_k$, which is not dense. Every
automorphism of $\mathbf P^1_k$ gives a refinement of it to itself.
Dense compactifications do not have this problem: morphisms between them
are unique, and with their refinements they form a cofiltered category
(Proposition [proposition-dense-compactifications-form-cofiltered-category]).
