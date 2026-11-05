+++
kind = "proof"
of = "lemma-vanishing-restrictions-after-blowing-up--1"
order = 978002
uses = ["lemma-cohomology-near-two-transverse-divisors", "lemma-restriction-punctured-curve"]
+++
The tangent cone condition implies $\m\subset\sqrt{(f,g)}$, so
$C-t$ maps to $T-D$. Choose regular parameters $x_0,y_0$ of $R$
such that the blowup charts, and their basic opens, are étale limits
of smooth surfaces. This is
`AlgebraicGeometry.Scheme.exists_isEtaleLimitOfSmoothSurfaces_blowupChart`.
The residue field of $R$ is $k$, so we may choose a direction
$x=x_0+a y_0$, $a\in k$, for which the chart
$R[v]/(xv-y_0)$ contains the required strict transforms. The tangent
cone hypotheses give separating chart data by
`AlgebraicGeometry.nonempty_blowupChartData`.

Write $f=x^d f'$ and $h=xh'$ in this chart, and put

$$
Z=\operatorname{Spec}\bigl((R[v]/(xv-y_0))[1/f']\bigr),\qquad
Y=V(x),\qquad X=V(h').
$$

Here $Z$ is regular and locally noetherian, and is an étale limit
of smooth surfaces. The divisors $X$ and $Y$ are regular, $Y$ is
connected, and their intersection is a single reduced point $z$
of codimension two. The blowup map gives
$\varphi:Z-Y\to T-D$, with inverse image of $T-(D\cup H)$ equal
to $Z-(X\cup Y)$. Pullback preserves finite $\ell$-group monodromy,
and base change for extension by zero identifies the pullback of
$j'_!N$ with the extension by zero of the pulled-back complex $N'$.

The chart data also give a finite $R/(g)$-algebra $B'$ for the
strict transform of $C$. After inverting $x$, this algebra agrees
with $(R/(g))[1/x]$, whose spectrum is $C-t$. Since $R$ is strictly
henselian, $B'$ is a finite product of strictly henselian local
rings. Their closed points map to closed points of $Y$.
Thus $C-t\to T-D$ factors through $Z-Y$, and its map to $Z$
factors through this finite disjoint union of strictly local schemes.

Put $M=Rj_*i_!N'$ for $j:Z-Y\hookrightarrow Z$ and
$i:Z-(X\cup Y)\hookrightarrow Z-Y$. Derived global sections of the
pullback of $M$ to each strictly local component identify with its
closed stalk. The restriction map to this stalk is zero by
[lemma-cohomology-near-two-transverse-divisors]: at $z$
the stalk itself vanishes, and at every other closed point of $Y$ the
restriction through $R\Gamma(Y,M|_Y)$ vanishes. This is the
factorization used in [lemma-restriction-punctured-curve], in the form
`AlgebraicGeometry.Etale.globalSectionsRestriction_transverseBoundaryComplex_eq_zero`.
Combining the components and then restricting to $C-t$ gives zero.
Base change and composition of restrictions identify this map with the
one in the statement; these steps are assembled in
`AlgebraicGeometry.Etale.globalSectionsRestriction_eq_zero_of_transverse`
and `AlgebraicGeometry.Etale.blowupRestriction_eq_zero_of_chartData`.

For the geometric formulation with reduced closed curves, the
two-dimensional regular local ring $R$ is factorial. The ideals of
$D$ and $C$ therefore have nonzero generators $f$ and $g$ in $\m$,
and the regular curve $H$ has an equation $h\in\m-\m^2$. Their
complements are the basic opens of $f$ and $fh$. Identifying
$C-t$ with the punctured spectrum of $R/(g)$ now gives the geometric
vanishing by
`AlgebraicGeometry.Etale.globalSectionsRestriction_eq_zero_of_eq_basicOpen`;
`AlgebraicGeometry.Etale.sectionsRestriction_app_eq_zero_of_globalSectionsRestriction_eq_zero`
expresses this as the component of the natural restriction map.
