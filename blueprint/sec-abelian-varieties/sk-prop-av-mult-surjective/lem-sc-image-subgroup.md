+++
id = "lem-sc-image-subgroup"
kind = "lemma"
title = "The image of a homomorphism is a closed subgroup scheme"
lean = ["AlgebraicGeometry.exists_isMonHom_image\u03b9", "AlgebraicGeometry.exists_isClosedSubgroupScheme_image\u03b9"]
order = 560
uses = ["def-sc-group-scheme", "def-sc-group-scheme-subgroup"]
+++
Let $f:G\to H$ be a homomorphism of
group schemes over a field $k$, with $G$ proper over $k$ and
$H$ separated and locally of finite type over $k$. Let $Z\subseteq H$ be
the scheme-theoretic image of $f$, i.e. the closed subscheme defined
by the kernel of $\mathcal O_H\to f_*\mathcal O_G$. Then $Z$ is of
finite type over $k$, the induced morphism $f':G\to Z$ is
surjective, and $Z$ is a closed
subgroup scheme of $H$.
