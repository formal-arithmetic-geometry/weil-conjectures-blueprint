+++
id = "lem-weil-pbc-idempotent-endomorphism-image-base-change"
kind = "lemma"
title = "The image of an idempotent endomorphism of a finite free module is finite projective and commutes with base change"
lean = ["LinearMap.idempotent_image_baseChange"]
order = 1811
+++
Let $R$ be a commutative ring, $n\ge0$ and $p:R^{\oplus n}\to R^{\oplus n}$ an $R$-linear map with $p\circ p=p$, with matrix $X\in M_n(R)$ in the standard basis. (i) $R^{\oplus n}=\operatorname{Im}(p)\oplus\operatorname{Im}(1-p)$ (internal direct sum, with $\operatorname{Im}(1-p)=\ker p$), so $\operatorname{Im}(p)$ is a finite projective $R$-module (a direct summand of a finite free module). (ii) Let $\rho:R\to S$ be a ring map and $p_S:S^{\oplus n}\to S^{\oplus n}$ the $S$-linear map with matrix $\rho(X)$ (entrywise); then $p_S\circ p_S=p_S$, and the $S$-linear map $\operatorname{Im}(p)\otimes_RS\to S^{\oplus n}$, $v\otimes s\mapsto s\cdot\rho(v)$ ($\rho$ applied to coordinates), is injective with image $\operatorname{Im}(p_S)$; hence $\operatorname{Im}(p)\otimes_RS\cong\operatorname{Im}(p_S)$ as $S$-modules.
