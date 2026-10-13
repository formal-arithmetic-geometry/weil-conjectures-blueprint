+++
id = "lemma-constructible-hom-constant-locally"
kind = "lemma"
title = "Morphisms between constant sheaves"
order = 1211
lean = ["CategoryTheory.Sheaf.isConstant_cokernel_over", "CategoryTheory.Sheaf.isConstant_kernel_over", "CategoryTheory.exists_mem_forall_exists_constantSheafOverHom_comp_map_eq", "CategoryTheory.exists_mem_forall_exists_linearMap"]
uses = ["def-constructible-constant"]
+++
Let $\mathcal A=\mathrm{Mod}_\Lambda$ with $\Lambda$ a ring, let $M$ be a finite
$\Lambda$-module, let $N$ be a $\Lambda$-module and let $\varphi\colon M_X\to N_X$ be a
morphism of constant sheaves on $\et X$. Then there is an étale cover
$(U_i\to X)_i$ such that $\varphi|_{U_i}$ is induced by a $\Lambda$-linear
map $f_i\colon M\to N$, i.e. equals $(f_i)_{U_i}\colon M_{U_i}\to N_{U_i}$.
Consequently the kernel and the cokernel of $\varphi$ are locally constant,
with restrictions $(\ker f_i)_{U_i}$ and $(\operatorname{coker}f_i)_{U_i}$.
