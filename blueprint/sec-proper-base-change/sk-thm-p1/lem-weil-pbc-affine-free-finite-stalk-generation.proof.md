+++
kind = "proof"
of = "lem-weil-pbc-affine-free-finite-stalk-generation"
uses = ["def-weil-pbc-geometric-stalks"]
+++
*Representing germs.* Every element of the stalk $F_{\bar x}$ is the germ of a section $z\in F(V)$ on a pointed etale neighbourhood $(V,\bar v)$ of $\bar x$, the stalk being the filtered colimit of the sections over pointed etale neighbourhoods [def-weil-pbc-geometric-stalks].

*Shrinking to an affine.* Choose an affine open $W\subseteq V$ containing the image of $\bar v$; the geometric point factors through $W$ (universal property of an open immersion), $W$ is affine etale over $X$, and the restriction $z|_W$ has the same germ.

*The map from $P_W$.* For an affine etale $W$ and $z\in F(W)$, the maps $\Lambda^{(\operatorname{Hom}_X(V',W))}\to F(V')$ sending the basis element indexed by $h:V'\to W$ to $F(h)(z)$ form a morphism of presheaves of $\Lambda$-modules; by the universal property of sheafification it induces $f_z:P_W\to F$, which sends the class of the generator indexed by $\mathrm{id}_W$ to $z$. Hence the germ of $z$ lies in the image of the stalk map of $f_z$.

*Finitely many maps.* Choose finitely many generators $t_1,\dots,t_m$ of the finitely generated $\Lambda$-module $F_{\bar x}$ and, for each, a pair $(W_j,f_j)\in I$ as above with $t_j$ in the image of $(f_j)_{\bar x}$; let $S$ be the finite set of these pairs. Each $f_j$ factors through the inclusion of the summand indexed by $(W_j,f_j)$ in $\bigoplus_{(W,f)\in S}P_W$, so every $t_j$ lies in the image of the stalk of $\bigoplus_{(W,f)\in S}P_W\to F$. That image is a submodule containing a generating set, hence everything: the stalk map is surjective. If $F_{\bar x}=0$, take $S=\emptyset$.
