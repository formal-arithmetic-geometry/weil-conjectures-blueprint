+++
kind = "proof"
of = "det-formal-closed-support-ii-limits"
+++
*Reduction.* In a triangulated category with countable products,

$$
R\varprojlim_nK_n=\fib\Bigl(\prod_nK_n\xrightarrow{\ 1-\mathrm{shift}\ }\prod_nK_n\Bigr),
$$

where $\mathrm{shift}$ has components the transition maps $K_{n+1}\to K_n$. An exact functor that
preserves countable products therefore carries this fiber to the fiber of $1-\mathrm{shift}$ on the
products of the $F(K_n)$, i.e. to $R\varprojlim_nF(K_n)$. Exact functors preserve fibers, so it
suffices to show that each listed functor is exact and preserves products.

*Open restriction.* $j^*$ and $u^*$ are exact on sheaves and are right adjoints (of $j_!$, $u_!$), so
they preserve products of sheaves; products in $\D(X_{\mathrm{proét}},\Lambda)$ are termwise
([sk-prop-pe-products]), hence $j^*$, $u^*$ preserve derived products.

*Closed restriction.* $i^*$ is exact and preserves products (Stacks, Tag 09AA); again since derived
products are termwise products, it preserves derived products.

*Open direct image.* $Rj_*$ is right adjoint to $j^*$, hence preserves all products that exist.

*Closed support.* $R\underline\Gamma_Z=i^*\fib(\mathrm{id}\to Rj_*j^*)$ by
part (1) of [sk-lem-formal-closed-support]. The functor $K\mapsto\fib(K\to Rj_*j^*K)$ preserves products,
because $\mathrm{id}$ and $Rj_*j^*$ do and fibers commute with products (a product of
distinguished triangles is distinguished). Composing with $i^*$ and $u^*$ gives the claim for
$R\underline\Gamma_Z$ and $u^*R\underline\Gamma_Z$.

*Tensoring with $L$.* Since $L$ is finite locally free, $L\otimes_{\Lambda_S}-$ is exact on sheaves
and agrees with the derived tensor product. It is right adjoint to $L^\vee\otimes_{\Lambda_S}-$
(with $L^\vee=\underline{\Hom}(L,\Lambda_S)$), because
$\Hom(L^\vee\otimes M,N)=\Hom(M,L\otimes N)$ via the evaluation and coevaluation of the dualizable
$L$. Hence it preserves products.
