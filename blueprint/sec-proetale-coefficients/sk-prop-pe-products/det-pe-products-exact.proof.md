+++
kind = "proof"
of = "det-pe-products-exact"
+++
Products of sheaves are computed sectionwise (the forgetful functor to presheaves creates
limits, and limits of presheaves are computed objectwise). Kernels commute with products, so
in both parts only the surjectivity of a product of epimorphisms has to be shown.

*1, and 2 for sheaves of $\Lambda$-modules.* Let $\varphi_i\colon A_i\to B_i$ be epimorphisms
(of abelian sheaves, or of sheaves of $\Lambda$-modules) and let $W$ be an affine weakly
contractible object. By [det-pe-wc-sections-exact] each $A_i(W)\to B_i(W)$ is surjective, and
a tuple $(b_i)\in\prod_iB_i(W)=(\prod_iB_i)(W)$ lifts to $(a_i)\in\prod_iA_i(W)$ by choosing a
preimage $a_i$ of each $b_i$ (axiom of choice). Hence $\prod_i\varphi_i$ is surjective on
sections over every such $W$, and by [det-pe-sections-conservative] (exactness of
$\prod_iA_i\to\prod_iB_i\to0$) it is an epimorphism. This argument works for every index set;
for countable index sets repleteness alone suffices, as in Bhatt–Scholze, §3.1.

*2 for module objects.* A morphism of module objects over the pullback of a condensed ring is
an epimorphism if and only if its underlying morphism of abelian sheaves is one, and products
of module objects are computed on underlying abelian sheaves. So the assertion follows from 1.
