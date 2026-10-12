+++
kind  = "proof"
of    = "lem-trf-trace-triangle-compatibility"
+++
*The induced morphisms.* Restriction of $u$ to the open correspondence
$c|_U$ uses only $j^*=j^!$ and the inclusions $c_2^{-1}(U)\subset c_1^{-1}(U)$;
the extension by zero $[j]_!(u|_U):c_2^*j_!j^*K\to c_1^!j_!j^*K$ is the
composite of the open $!$-base change $c_2^*j_!\cong j_!(c_2|_U)^*$, of
$j_!(u|_U)$ and of the canonical map $j_!(c_1|_U)^!\to c_1^!j_!$. The
restriction $u|_Z$ exists because $Z$ is $c$-invariant ($c|_Z$ is the
correspondence induced on $c_1^{-1}(Z)_{\mathrm{red}}$, and $u$ pulls back
along the closed immersion of correspondences), and $[i]_!(u|_Z)$ is its
coefficient pushforward along the proper morphism $[i]$ of correspondences,
as in [thm-trf-dualizing-complex-composition] and the proper pushforward
of this chapter. That $(u^U,u,u^Z)$ is a morphism of the open–closed
triangles is checked by adjunction exactly as in the Frobenius case treated
in the proof of item (2) of the trace-class additivity proposition of this
block, the third square following from the first two and the vanishing
$\operatorname{Hom}(j_!N[1],Ri_*M)=0$.

*Additivity.* The identity of trace classes is
[Varshavsky, Prop. 1.5.10](https://arxiv.org/abs/math/0505564) in our leg
convention (his $c$-morphisms are $c_1^*\mathcal F\to c_2^!\mathcal F$, so
his $c_2^{-1}(Z)$ is our $c_1^{-1}(Z)$ and his $c$-invariance
$c_1(c_2^{-1}(Z))\subset Z$ is our $c_2(c_1^{-1}(Z))\subset Z$). His proof
(§5.3, Lemma 5.3.2, after Illusie, SGA 5 III 4.13) lifts the trace map to
the filtered derived category $D^bF_{ctf}(X,A)$: the two-step filtration
$j_!j^*K\subset K$ makes $(K,u)$ a filtered $c$-morphism whose graded
pieces are $(j_!j^*K,u^U)$ and $(Ri_*i^*K,u^Z)$, the trace map is a
morphism of filtered bifunctors, and the trace of a filtered $c$-morphism
is the sum of the traces of its graded pieces. The argument needs the
filtered origin of the triple: it is not a consequence of the three squares
commuting in the derived category.

*What the previous argument got wrong.* An earlier proof of this lemma
restricted the trace classes to the geometric points $\bar y$ of $F$ and
claimed $Li_{\bar y}^*\operatorname{Tr}_c(u)=\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y})$
in general. This is false: the stalk at $\bar y$ of the trace-class source
$R\mathcal Hom_A(c_2^*K,c_1^!K)$ is not $R\mathcal Hom_A(K_{\bar y},K_{\bar y})$
(for $K=j_!A$ on $\mathbf A^1$ the source is $Rj_*A$, with nonzero stalk at
$0$ although $K_0=0$), and the equality of the local term with the stalk
trace holds only under a contracting hypothesis
([lem-trf-local-term-locality], item (1)). The reduction to the point
normalization is therefore not available, and the filtered argument above
replaces it.
