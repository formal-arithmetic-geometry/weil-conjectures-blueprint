+++
kind  = "proof"
of    = "det-lem-int-tensor-product"
uses = ["det-lem-int-tensor-shriek", "det-lem-int-tensor-pullback", "det-lem-int-tensor-projection", "sk-prop-integral-criterion", "sk-def-pe-derived-completion", "sk-def-sfb-constructible", "sk-lem-int-integral-heart"]
+++
*Dualizability of a local model.* Let $M$ be as in the second paragraph, with a
pro-étale cover $\{W_k\to S\}$ and $M|_{W_k}\simeq P_k\otimes_{\mathcal O_E}\mathcal O_{E,W_k}$. Put
$M^\vee=R\mathcal Hom(M,\mathcal O_{E,S})$. On $W_k$ it is
$P_k^\vee\otimes_{\mathcal O_E}\mathcal O_{E,W_k}$ with $P_k^\vee=\Hom_{\mathcal O_E}(P_k,\mathcal O_E)$, and the
evaluation $M^\vee\otimes^{\mathbf L}M\to\mathcal O_{E,S}$ and the canonical map
$M\otimes^{\mathbf L}N\to R\mathcal Hom(M^\vee,N)$ are, on $W_k$, the corresponding maps for
the bounded complex of finite free modules $P_k$, which are isomorphisms
(respectively satisfy the triangle identities) because they do so for
$P=\mathcal O_E$ and are compatible with finite sums and cones. A morphism in the
derived category is an isomorphism if it is so on a cover, and the triangle
identities are equalities of morphisms that can be checked after the
isomorphisms just established. So $M$ is dualizable with dual $M^\vee$, and
$M\otimes^{\mathbf L}-\simeq R\mathcal Hom(M^\vee,-)$ is a right adjoint (of
$M^\vee\otimes^{\mathbf L}-$) as well as a left adjoint (of $R\mathcal Hom(M,-)$). Being a
right adjoint, it preserves products; being exact, it preserves
$R\varprojlim$ of sequences, which is the fibre of a map between products. It
also commutes with reduction modulo $\pi_E^n$ by associativity of the derived
tensor product. Hence, if $N$ is derived complete, applying $M\otimes^{\mathbf L}-$ to
the isomorphism $N\simeq R\varprojlim_nN\otimes^{\mathbf L}\mathcal O_E/\pi_E^n$ shows that
$M\otimes^{\mathbf L}N$ is derived complete ([sk-def-pe-derived-completion]).

*Reduction to a stratum.* Fix $L\in\Dbc(X,\mathcal O_E)$. The functor
$K\mapsto K\otimes^{\mathbf L}L$ is exact and $\Dbc(X,\mathcal O_E)$ is triangulated
([sk-lem-int-integral-heart]), so the class of $K$ with
$K\otimes^{\mathbf L}L\in\Dbc(X,\mathcal O_E)$ is closed under extensions. By
[det-lem-int-tensor-shriek] (2) it suffices to treat $K=a_!M$ with
$a\colon S\hookrightarrow X$ a stratum and $M$ a local model as above. By
[det-lem-int-tensor-projection],
$$
a_!M\otimes^{\mathbf L}L\simeq a_!\bigl(M\otimes^{\mathbf L}a^*L\bigr),
$$
and by [det-lem-int-tensor-shriek] (1) it suffices to show
$M\otimes^{\mathbf L}a^*L\in\Dbc(S,\mathcal O_E)$.

*The stratum.* By [det-lem-int-tensor-pullback], $N:=a^*L\in\Dbc(S,\mathcal O_E)$; in
particular $N$ is derived complete, so $M\otimes^{\mathbf L}N$ is derived complete by
the first paragraph. Its reduction is, by associativity,
$$
(M\otimes^{\mathbf L}N)\otimes^{\mathbf L}\mathcal O_E/\pi_E\simeq(M/\pi_E)\otimes^{\mathbf L}_{\mathbf F_{E,S}}(N/\pi_E),
\qquad \mathbf F_E=\mathcal O_E/\pi_E .
$$
Both factors lie in $\Dbc(S,\mathbf F_E)$ (by [sk-prop-integral-criterion] for $N$,
and for $M$ because it is locally a bounded complex of finite free modules on
the single stratum $S$). It remains to see that $\Dbc(S,\mathbf F_E)$ is closed
under $\otimes^{\mathbf L}$. Every $\mathbf F_{E,S}$-module is flat: the tensor product
over the constant sheaf of the field $\mathbf F_E$ is the sheafification of the
sectionwise tensor product over $\mathbf F_E$, which is exact. So
$\otimes^{\mathbf L}=\otimes$ is exact in each variable, and by the truncation
triangles (both factors are bounded) it suffices to show that $F\otimes G$ is
constructible for constructible sheaves $F$, $G$
([sk-def-sfb-constructible]). Choose a common refinement of their
stratifications and, on each stratum, a common refinement of the covers
carrying finite constant local models $F\simeq\mathbf F_E^r$, $G\simeq\mathbf F_E^s$
(finitely presented modules over a field are free); then
$F\otimes G\simeq\mathbf F_E^{rs}$ there. Hence $F\otimes G$ is constructible, the
reduction of $M\otimes^{\mathbf L}N$ is bounded constructible, and
$M\otimes^{\mathbf L}N\in\Dbc(S,\mathcal O_E)$ by [sk-prop-integral-criterion].
