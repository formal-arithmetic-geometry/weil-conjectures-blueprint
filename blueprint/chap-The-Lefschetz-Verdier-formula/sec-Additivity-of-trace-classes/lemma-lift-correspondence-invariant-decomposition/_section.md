+++
id = "lemma-lift-correspondence-invariant-decomposition"
kind = "lemma"
title = "Lifting a correspondence to an invariant decomposition"
order = 937
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "lemma-inverse-image-tensor-product", "proposition-composition-base-change-rf-shriek", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "definition-correspondence", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $c:C\to X\times X$ be a correspondence, $i:Z\to X$ a closed
immersion with open complement $j:U\to X$, and suppose

$$
c_1^{-1}(Z)\subset c_2^{-1}(Z),
\qquad\text{equivalently }c_2^{-1}(U)\subset c_1^{-1}(U).
$$

Let $u$ be a cohomological correspondence on $(X,K)$, and write
$K_U=j_!j^*K$ and $K_Z=Ri_*i^*K$ for the two pieces of the localization
triangle $K_U\to K\to K_Z$. Then $u$ has a lift, unique up to
contractible choice, to a cohomological correspondence $\tilde u$ in the
filtered derived category on the two-step filtered complex given by this
triangle. Its graded pieces are cohomological correspondences $u_U$ on
$(X,K_U)$ and $u_Z$ on $(X,K_Z)$, and $\widehat u_Z$ restricted to $Z$ is

$$
Rc_{1Z!}c_{2Z}^*i^*K\simeq i^*\Theta K
\xrightarrow{i^*\widehat u}i^*K.
$$
