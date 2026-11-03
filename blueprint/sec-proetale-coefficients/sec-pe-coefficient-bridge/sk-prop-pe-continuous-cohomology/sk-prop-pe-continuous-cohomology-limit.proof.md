+++
kind = "proof"
of = "det-pe-continuous-cohomology-limit"
+++
The topos $X_{\Proet}$ is replete ([det-pe-replete-epimorphism]). In a replete
topos, for an inverse system of abelian sheaves with surjective transition maps,
$R^1\varprojlim F_n=0$ and the higher derived limits vanish, i.e.
$R\varprojlim_nF_n\simeq\varprojlim_nF_n$ ([det-pe-milnor-epimorphic];
Bhatt–Scholze, Proposition 3.1.10);
equivalently the map $1-\text{shift}\colon\prod_nF_n\to\prod_nF_n$ is an
epimorphism with kernel $F$, and countable products of sheaves are exact on a
replete topos so that $\prod_nF_n$ computes the derived product.

The functor $R\Gamma(W,-)\colon D(X_{\Proet})\to D(\mathbf Z)$ is triangulated and,
as a right adjoint, preserves products. Applying it to the triangle
$R\varprojlim_nF_n\to\prod_nF_n\xrightarrow{1-\text{shift}}\prod_nF_n\to$ gives the
triangle defining $R\varprojlim_nR\Gamma(W,F_n)$, whence the isomorphism.
