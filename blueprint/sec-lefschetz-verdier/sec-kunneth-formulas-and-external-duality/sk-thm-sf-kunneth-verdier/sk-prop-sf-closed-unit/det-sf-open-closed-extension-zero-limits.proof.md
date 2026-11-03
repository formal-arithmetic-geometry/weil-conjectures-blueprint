+++
kind = "proof"
of = "det-sf-open-closed-extension-zero-limits"
uses = ["det-sf-open-closed-pullback-limits", "det-sf-open-closed-sequence-ring-sheaf"]
+++
*(1) The triangle.* Represent $K$ by a K-injective complex $J$ of
$j^*B$-modules, so that $Rj_*K$ is represented by $j_*J$. Apply the short
exact sequence of [det-sf-open-closed-sequence-ring-sheaf] termwise to
$M=j_*J^q$. Since $j^*j_*=\mathrm{id}$ for an open immersion, its first term
is $j_!J^q$, so we obtain a termwise exact sequence of complexes

$$
0\to j_!J\to j_*J\to i_*i^*j_*J\to0 .
$$

As $j_!$, $i^*$ and $i_*$ are exact
([det-sf-open-closed-sequence-ring-sheaf], [det-sf-open-closed-pullback-limits]),
these complexes represent $j_!K$, $Rj_*K$ and $i_*i^*Rj_*K$, and a short exact
sequence of complexes gives a distinguished triangle, functorial in $K$.

*(2) Products and derived limits.* The pro-étale topos is replete, so
products of sheaves are exact (Bhatt–Scholze, Proposition 3.1.10); hence the
product in $D(-_{\mathrm{proét}})$ of a family of complexes is represented by the
termwise product. The functor $Rj_*$ is a right adjoint, so it preserves
products. The functor $i_*$ is an exact right adjoint, so it preserves
termwise products of complexes, hence derived products. The functor $i^*$ is
exact and preserves products of sheaves
([det-sf-open-closed-pullback-limits]), so it preserves termwise products of
complexes, hence derived products. Thus the second and third terms of the
triangle in (1) are product-preserving exact functors of $K$. Given a family
$(K_\alpha)$, the product of the triangles of (1) is distinguished (a product
of distinguished triangles is distinguished when products are exact), and
the canonical maps from the triangle of $\prod_\alpha K_\alpha$ to it form a
morphism of triangles which is an isomorphism on the second and third
terms; by the five lemma for triangulated categories
$j_!\prod_\alpha K_\alpha\to\prod_\alpha j_!K_\alpha$ is an isomorphism. For a
sequence $(K_n)$ the derived limit is the fibre
$R\varprojlim_nK_n=\operatorname{fib}\bigl(\prod_nK_n\xrightarrow{1-\mathrm{sh}}\prod_nK_n\bigr)$;
an exact functor preserving products and the shift-difference map preserves
this fibre, so $j_!R\varprojlim_nK_n\simeq R\varprojlim_nj_!K_n$.

*(3) Module sheaves.* Products of module sheaves are exact, so for module
sheaves $M_\alpha$ on $U$ placed in degree $0$ the derived product is the
sheaf product. Since $j_!$ is exact, (2) applied to these complexes and
$\mathcal H^0$ give $j_!\prod_\alpha M_\alpha\simeq\prod_\alpha j_!M_\alpha$.
