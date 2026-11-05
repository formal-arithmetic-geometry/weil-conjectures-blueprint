+++
id = "lemma-class-diagonal-projective-line"
kind = "lemma"
title = "The class of the diagonal of $\\mathbf P^1_S$"
order = 550
lean = ["AlgebraicGeometry.Etale.projectiveLine_diagonal_ker_isInvertible", "AlgebraicGeometry.Etale.ordinaryFiniteP1_diagonal_integral"]
uses = ["lemma-cycle-class-cartier-divisor", "lemma-cohomology-projective-line-trace"]
+++
Let $S$ be of finite type over $k$, and let $p_i$ and
$\operatorname{Tr}_{p_i}$ be as above. The diagonal $\Delta$ is a relative
effective Cartier divisor in $\mathbf P^1_S\times_S\mathbf P^1_S$ over $S$,
and it remains one after every base change $S'\to S$. Let

$$
\delta:\Delta_*A_{\mathbf P^1_S}\longrightarrow
A_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
$$

be its cycle class (Lemma [lemma-cycle-class-cartier-divisor]). Then for
$i=1,2$ the composite

$$
s_i:A_{\mathbf P^1_S}=Rp_{i*}\Delta_*A_{\mathbf P^1_S}
\xrightarrow{Rp_{i*}\delta}
Rp_{i*}A_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2]
\xrightarrow{\operatorname{Tr}_{p_i}}A_{\mathbf P^1_S}
\tag{6.4}
$$

is the identity.
