+++
id = "proposition-adjunction-projective-line--1"
kind = "proposition"
title = "The projective-line adjunction"
order = 553002
aliases = ["bp-r167-1"]
lean = ["AlgebraicGeometry.Etale.exists_projectiveLineAdjunction"]
uses = ["definition-tate-twists", "lemma-cohomology-projective-line-trace"]
+++
Let $\Lambda$ be a finite commutative ring with a normalized Kummer class
and its Tate twists. Let $S$ be a scheme on which the exponent of $\Lambda$
is invertible, and let $p:\mathbf P^1_S\to S$ be the projection. On the
full étale derived categories there is an adjunction

$$
Rp_!:D((\mathbf P^1_S)_{\acute{e}t},\Lambda)
\ \rightleftarrows\ D(S_{\acute{e}t},\Lambda):p^*(1)[2],
\qquad Rp_!\dashv p^*(1)[2],
$$

whose counit at $K$ is the composite

$$
\begin{split}
Rp_!\bigl(p^*K(1)[2]\bigr)
&\xrightarrow{\ \sim\ }
Rp_!\bigl(\Lambda_{\mathbf P^1_S}(1)[2]\otimes_\Lambda^{\mathbf L}p^*K\bigr)\\
&\xrightarrow{\ \sim\ }
Rp_!\Lambda_{\mathbf P^1_S}(1)[2]\otimes_\Lambda^{\mathbf L}K
\xrightarrow{t_p\otimes 1}K.
\end{split}
$$

Here the first isomorphism moves the shift into the Tate factor and
exchanges the tensor factors, the second is the inverse projection map,
and $t_p$ is the second projection of the inverse decomposition with
hyperplane class $h=-c_1(\mathcal O(1))$, read through $Rp_!\simeq Rp_*$.
Thus $t_p=-\operatorname{Tr}_p$ for the normalization in
[lemma-cohomology-projective-line-trace]. This is the Kummer-boundary sign
convention of `AlgebraicGeometry.Etale.projectiveLineTrace`. Since $p$ is
proper, the adjunction also gives $Rp_*\dashv p^*(1)[2]$.
