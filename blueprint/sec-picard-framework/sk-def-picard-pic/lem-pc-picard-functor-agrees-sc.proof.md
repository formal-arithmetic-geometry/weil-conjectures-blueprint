+++
kind  = "proof"
of    = "lem-pc-picard-functor-agrees-sc"
+++
Both sides are the fppf sheafification of the same presheaf on the
category of affine $k$-schemes: the left is the restriction of the fppf
sheafification on $(\mathit{Sch}/k)_{fppf}$, and fppf sheafification
commutes with restricting to the essentially full subcategory of affine
schemes, because the $(\mathit{Sch}/k)_{fppf}$-coverings of an affine
scheme and the corresponding coverings by affines cofinalize (every
scheme is covered by open affines in the Zariski, hence fppf, topology;
and for our purposes the affine objects fully capture the value of a
sheaf). More precisely: let
$F_T=\operatorname{Pic}(X_T)$ and let $\pi:(\mathit{Sch}/k)_{fppf}\to(\mathit{Aff}/k)_{fppf}$
be the restriction; the map of sites $\pi$ induces for the sheafification
$(\pi^{-1}F^\#)^\#=(\pi^{-1}F)^\#$ for the restriction of the sheafified
functor to affine schemes; the sheaves that are sheafifications of
presheaves on the affine site are exactly the fppf sheaves on
$(\mathit{Aff}/k)_{fppf}$, the two prescriptions agree on affine inputs.
This is the standard construction of the big sites (see Topologies,
Section 34.7, Tag [021S](https://stacks.math.columbia.edu/tag/021S)).
