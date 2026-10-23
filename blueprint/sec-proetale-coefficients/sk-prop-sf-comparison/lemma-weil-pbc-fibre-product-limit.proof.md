+++
kind  = "proof"
of    = "lemma-weil-pbc-fibre-product-limit"
+++
By [def-weil-pbc-strict-henselization-limit], $S_{(\bar s)}$ is the limit of
the affine pointed etale neighbourhoods $V$ of $\bar s$ in the category of
schemes. The index category is cofiltered, hence connected, and the forgetful
functor from schemes over $S$ to schemes creates connected limits, so
$S_{(\bar s)}$ is also their limit in the category of $S$-schemes. Base change
along $f$, from $S$-schemes to $X$-schemes, is right adjoint to composition
with $f$, so it preserves this limit: $X\times_SS_{(\bar s)}$ is the limit of
the $X\times_SV$ in the category of $X$-schemes. Since the index category is
connected, the forgetful functor from $X$-schemes to schemes preserves this
limit, which gives the displayed isomorphism. No finiteness hypothesis on $f$
is needed.
