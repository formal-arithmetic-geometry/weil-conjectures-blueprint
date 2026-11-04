+++
id = "lemma-class-diagonal-projective-line"
kind = "lemma"
title = "The class of the diagonal of $\\mathbf P^1_S$"
order = 544
lean = ["AlgebraicGeometry.Etale.projectiveLineTrace_diagonal", "AlgebraicGeometry.Etale.projectiveLineTrace_diagonal_swap"]
uses = ["lemma-cycle-class-cartier-divisor"]
+++
Let $S$ be of finite type over $k$ and let $\Lambda$ be a finite
commutative $\ell$-primary ring; we work on the étale sites, and $p_i$ and
$\operatorname{Tr}_{p_i}$ are as above. The diagonal $\Delta$ is a relative
effective Cartier divisor in $\mathbf P^1_S\times_S\mathbf P^1_S$ over $S$,
and it remains one after every base change $S'\to S$. Let

$$
\delta:\Delta_*\Lambda_{\mathbf P^1_S}\longrightarrow
\Lambda_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
$$

be its cycle class (Lemma [lemma-cycle-class-cartier-divisor]). Then for
$i=1,2$ the composite

$$
s_i:\Lambda_{\mathbf P^1_S}=Rp_{i*}\Delta_*\Lambda_{\mathbf P^1_S}
\xrightarrow{Rp_{i*}\delta}
Rp_{i*}\Lambda_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
\xrightarrow{\operatorname{Tr}_{p_i}}\Lambda_{\mathbf P^1_S}
\tag{6.4}
$$

is the identity.
