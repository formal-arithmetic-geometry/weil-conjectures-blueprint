+++
id = "det-cor-jacobian-torsion-pic"
kind = "lemma"
title = "Divisibility of $J(C)(k)$ and the $n$-torsion of $\\operatorname{Pic}(C)$"
lean = ["AlgebraicGeometry.surjective_npow_points", "AlgebraicGeometry.Scheme.surjective_pow_picardZero", "AlgebraicGeometry.Scheme.ker_picDegreeMod", "AlgebraicGeometry.Scheme.Hom.pic_proper_ntorsion_coker"]
uses = ["sk-prop-av-mult-surjective", "sk-prop-av-isogeny", "sk-prop-av-divisible", "sk-cor-picard-degree", "sk-thm-picard-main"]
+++
Let $k$ be algebraically closed and let $C/k$ be a smooth proper connected
curve of genus $g$, with Jacobian $J(C)$.

1. For every $n\ge1$, multiplication by $n$ on $J(C)(k)$ is surjective.
2. Let $n>0$. The inclusion $J(C)(k)=\operatorname{Pic}^0(C)\subset\operatorname{Pic}(C)$
   restricts to an equality
   $$
   J(C)[n](k)=J(C)(k)[n]=\operatorname{Pic}(C)[n],
   $$
   and the degree map induces an isomorphism
   $$
   \operatorname{Pic}(C)/n\operatorname{Pic}(C)\xrightarrow[\ \deg\ ]{\sim}\Z/n\Z.
   $$
