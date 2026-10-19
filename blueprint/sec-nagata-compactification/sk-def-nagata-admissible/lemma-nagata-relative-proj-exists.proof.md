+++
kind  = "proof"
of    = "lemma-nagata-relative-proj-exists"
+++
**The local squares.** Let $U\subseteq V$ be affine opens and put
$R=\Gamma(V,\mathcal O_X)$, $S=\Gamma(U,\mathcal O_X)$, $C=\mathcal A(V)$.
$\operatorname{Proj}(C)$ is covered by the standard opens $D_+(s)$, $s\in C$
homogeneous of positive degree, with $D_+(s)\cong\operatorname{Spec}C_{(s),0}$.
Since $\mathcal A(U)=S\otimes_RC$ coefficientwise, and the degree-zero
homogeneous localization is a filtered colimit of homogeneous pieces, it
commutes with the base change:
$S\otimes_RC_{(s),0}\cong\mathcal A(U)_{(s),0}$. So the preimage of
$D_+(s)$ in $\operatorname{Proj}(\mathcal A(U))$ is
$\operatorname{Spec}(S\otimes_RC_{(s),0})=U\times_VD_+(s)$. These chart
identifications are compatible on the overlaps $D_+(st)$ by
[lemma-nagata-proj-chart-ring-cocycle], hence glue: the square formed by the
transition morphism, the two structure morphisms and $U\subseteq V$ is
cartesian. In particular each transition morphism is an open immersion
onto the preimage of $U$.

**Gluing.** The diagram $V\mapsto\operatorname{Proj}(\mathcal A(V))$ over
the poset of affine opens, with its structure morphisms to the opens $V$,
therefore has open immersions as transition maps and cartesian
transition squares. Glue the schemes $\operatorname{Proj}(\mathcal A(V))$
along these open immersions: for affine opens $V,V'$, the preimages of
$V\cap V'$ are covered by the images of $\operatorname{Proj}(\mathcal A(W))$,
$W\subseteq V\cap V'$ affine, and are identified through these common
pieces; since the diagram is a functor on a poset, all identifications are
composites of transition maps and the cocycle condition holds automatically.
The glued scheme is the colimit $\operatorname{Proj}_X(\mathcal A)$, the
colimit maps $\iota_V$ are open immersions, and the compatible morphisms
$\operatorname{Proj}(\mathcal A(V))\to V\subseteq X$ induce $\pi$. This gives
(1) and the first half of (3); as for any gluing along cartesian
transition squares, $\pi^{-1}(V)$ is the image of $\iota_V$, so $\iota_V$
identifies $\operatorname{Proj}(\mathcal A(V))$ with $\pi^{-1}(V)$ over $V$,
which is (2). The compatibility in (3) follows by composing with the
projections of the fibre products.

**Uniqueness.** In the situation of (4) the $j_V$ form a cocone on the
diagram, so they induce a unique $e$ with $e\circ\iota_V=j_V$, and
$p\circ e=\pi$ because both agree after composing with every $\iota_V$.
Over each affine $V\subseteq X$, $e$ restricts to
$j_V\circ\iota_V^{-1}\colon\pi^{-1}(V)\to p^{-1}(V)$, an isomorphism by
(2) and the hypothesis on $j_V$. As the $V$ cover $X$, $e$ is an
isomorphism.

**Independence of the cover.** The family $(V_i)$ covers $X$ and the
hypothesis on $k$ ensures that every overlap $V_i\cap V_{i'}$ is covered by
opens $V_k$ with $k\le i,i'$. The gluing argument above, run over the
preordered set $I$, shows that the colimit over $I$ is a scheme over $X$
whose charts satisfy (2); comparing it with $\operatorname{Proj}_X(\mathcal A)$
chart by chart, as in the uniqueness step, identifies the two.
