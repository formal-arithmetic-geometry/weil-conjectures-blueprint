+++
kind = "proof"
of = "lemma-perverse-sheaves-curve--1"
order = 1249003
uses = ["lemma-perverse-sheaves-curve--2", "prose-10-20"]
+++
Suppose that $K\in{}^pD^{\ge0}$ and $M\in{}^pD^{\le-1}$.
Ordinary truncation identifies a morphism $M\to K$ with its map on
$\mathcal H^{-1}$. The image of this map has finite support, since it
is a quotient of $\mathcal H^{-1}M$, and is a subsheaf of
$\mathcal H^{-1}K$. The lower-class condition makes the image zero,
so the morphism vanishes.

Conversely, suppose that all such morphisms vanish. If $K$ has nonzero
cohomology below degree $-1$, boundedness gives a least such degree $a$.
The sheaf $\mathcal H^aK$ placed in degree $a$ belongs to
${}^pD^{\le-1}$, and its identity lifts to a morphism into $K$ by the
ordinary truncation calculation. The assumed vanishing is a contradiction.
Thus $K$ has no cohomology below degree $-1$. For a finite-support
subsheaf $G\hookrightarrow\mathcal H^{-1}K$, the same calculation lifts
the inclusion to $G[1]\to K$. Since $G[1]\in{}^pD^{\le-1}$, this map
is zero, so $G=0$. This proves
`AlgebraicGeometry.WeilComplex.isCurvePerverseLower_iff_forall_hom_eq_zero`.

For the cone assertion, use the long exact sequence of ordinary
cohomology of the triangle, with its Weil structures as in [prose-10-20].
It gives $\mathcal H^aR=0$ for $a>0$ and $a<-2$, and makes
$\mathcal H^0R$ a quotient of the finite-support sheaf $\mathcal H^0P$.
Put $E=\mathcal H^{-2}R$. The connecting map embeds $E$ into
$\mathcal H^{-1}Q$, so $E$ has no nonzero finite-support subsheaf.
By [lemma-perverse-sheaves-curve--2], $E[1]$ is curve perverse.
The connecting map lifts to $E[1]\to Q$, whose composite with $f$ is
zero. Monicity of $f$ in the perverse subcategory forces this map to
vanish, and hence $E=0$.

Finally, a finite-support subsheaf $G\hookrightarrow\mathcal H^{-1}R$
lifts to a map $v:G[1]\to R$. Composing with $R\to Q[1]$ and shifting
back gives a map $G\to Q$ killed by $f$. The degree-zero complex $G$
is curve perverse by [lemma-perverse-sheaves-curve--2], so this map is
zero. Exactness of $\Hom(G[1],-)$ on the triangle therefore factors
$v$ through $P$. Orthogonality, already proved, makes this factor zero,
since $G[1]\in{}^pD^{\le-1}$ and $P\in{}^pD^{\ge0}$. Thus the inclusion
of $G$ is zero and $G=0$. This is
`AlgebraicGeometry.WeilComplex.isCurvePerverse_of_mono`.
