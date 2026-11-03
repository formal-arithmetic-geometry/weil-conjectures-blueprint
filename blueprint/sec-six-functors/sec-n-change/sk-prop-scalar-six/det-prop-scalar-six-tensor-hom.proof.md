+++
kind  = "proof"
of    = "det-prop-scalar-six-tensor-hom"
uses = ["det-prop-scalar-six-ctf", "det-prop-scalar-six-direct-image", "det-prop-scalar-six-exceptional", "det-prop-scalar-six-pullback", "det-lem-int-tensor-projection", "sk-thm-sf-ctf-stability", "sk-thm-existence"]
+++
*(1)* By associativity and commutativity of the derived tensor product,
$$
\Lambda'_X\otimes^{\mathbf L}_{\Lambda_X}(K\otimes^{\mathbf L}_{\Lambda_X}M)\simeq(\Lambda'_X\otimes^{\mathbf L}_{\Lambda_X}K)\otimes^{\mathbf L}_{\Lambda'_X}(\Lambda'_X\otimes^{\mathbf L}_{\Lambda_X}M),
$$
computed on K-flat resolutions; these isomorphisms are the canonical ones, so they
satisfy the coherence conditions of a symmetric monoidal functor, with
$(\Lambda_X)_{\Lambda'}=\Lambda'_X$.

*(2) Reduction.* Both sides of $v_{K,M}$ lie in $\Dctf(X,\Lambda')$ by
[sk-thm-sf-ctf-stability] and [det-prop-scalar-six-ctf]. Both are exact functors of $K$
(contravariant) and $v$ is natural, so the class of $K$ for which $v_{K,M}$ is an
isomorphism for all $M$ is closed under shifts, cones and direct summands. By
[det-prop-scalar-six-ctf] (1) it suffices to take $K=a_!P$, with
$a\colon S\hookrightarrow X$ locally closed and $P$ locally perfect on $S$.

*The generator.* $P$ is dualizable with dual $P^\vee=R\mathcal Hom_S(P,\Lambda_S)$, locally the
dual complex of finite projective modules, so $R\mathcal Hom_S(P,N)\simeq P^\vee\otimes^{\mathbf L}N$.
For $T\in\Loc(\Dctf(X,\Lambda))$, the tensor–Hom adjunction, the projection formula
$a_!P\otimes^{\mathbf L}T\simeq a_!(P\otimes^{\mathbf L}a^*T)$ ([det-lem-int-tensor-projection]) and
$Ra_!=a_!\dashv a^!$ ([sk-thm-existence]) give natural bijections
$$
\Hom(T,R\mathcal Hom(a_!P,M))=\Hom(a_!(P\otimes^{\mathbf L}a^*T),M)=\Hom(a^*T,R\mathcal Hom(P,a^!M))=\Hom(T,Ra_*(P^\vee\otimes^{\mathbf L}a^!M)).
$$
Both $R\mathcal Hom(a_!P,M)$ and $Ra_*(P^\vee\otimes^{\mathbf L}a^!M)$ lie in $\Dctf(X,\Lambda)$
([sk-thm-sf-ctf-stability]), so by Yoneda in $\Loc(\Dctf(X,\Lambda))$
$$
R\mathcal Hom_X(a_!P,M)\simeq Ra_*\bigl(P^\vee\otimes^{\mathbf L}a^!M\bigr),
$$
and likewise over $\Lambda'$ for $a_!(P_{\Lambda'})\simeq(a_!P)_{\Lambda'}$
([det-prop-scalar-six-pullback] (2)) and $M_{\Lambda'}$. Extension of scalars commutes with
each ingredient on the right: with $Ra_*=i_*Ru_*$ by [det-prop-scalar-six-direct-image];
with $a^!$ by [det-prop-scalar-six-exceptional]; with the dual, since
$(P^\vee)_{\Lambda'}\simeq(P_{\Lambda'})^\vee$ for locally perfect $P$ (for $P=\Lambda_S^m$ both are
$\Lambda'^m_S$, and the map is compatible with summands, shifts, cones and
restriction); and with tensor products by (1). Composing these gives an
isomorphism $(R\mathcal Hom(a_!P,M))_{\Lambda'}\simeq R\mathcal Hom(a_!P_{\Lambda'},M_{\Lambda'})$.

*It is $v_{a_!P,M}$.* Every map used is defined from evaluation pairings, units and
counits, and the comparison maps are compatible with them
([det-prop-scalar-six-direct-image] (2), the definition of $\beta$ in
[det-prop-scalar-six-exceptional]). Hence the transpose of the composite isomorphism
under $-\otimes^{\mathbf L}a_!P_{\Lambda'}\dashv R\mathcal Hom(a_!P_{\Lambda'},-)$ is the extension of scalars
of the evaluation $R\mathcal Hom(a_!P,M)\otimes^{\mathbf L}a_!P\to M$, which is also the transpose of
$v_{a_!P,M}$. So the composite is $v_{a_!P,M}$, which is therefore an isomorphism.
Finite cones and summands give the result for every $K\in\Dctf(X,\Lambda)$.
