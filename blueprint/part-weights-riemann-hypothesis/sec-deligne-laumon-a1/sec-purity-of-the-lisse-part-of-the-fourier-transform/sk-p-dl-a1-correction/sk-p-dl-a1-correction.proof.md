+++
kind = "proof"
of = "sk-p-dl-a1-correction"
+++
By the stalk formula
of Proposition [sk-thm-inversion], the stalk of
$\operatorname{FT}_\psi(j_!M)$ at $y$ is
$R\Gamma_c(U,M\otimes\mathcal L_{\psi(yx)})[1]$. The group in degree
zero vanishes by Lemma [sk-l-dl-a1-endpoints], applied to the
lisse sheaf $M\otimes\mathcal L_{\psi(yx)}$ on the affine curve $U$
with $j$ the identity. The group in degree
two vanishes as well, since a nonzero coinvariant would give $M$ a
geometric rank-one quotient of the form that our assumption on $M$
excludes. Hence the transform is a sheaf $G$. After geometric base
change, the punctual sheaf $B$ is a finite sum of skyscrapers with
coefficient modules, and the transform of each skyscraper is a linear
character sheaf tensored with that module and shifted by one. It
follows that $B'$ is lisse. Now we apply the Fourier transform to the
triangle obtained from $0\to j_!M\to j_*M\to B\to0$. The isomorphism of
Proposition [sk-p-dl-a1-middle] identifies the transform of the
middle term with $j'_*M'$, and the long exact sequence of cohomology
sheaves is the stated exact sequence.

To bound the weights, recall that Proposition [sk-p-real-semi]
bounds the weights of the
stalks of $B$ by $w$, and that a character sheaf has weight zero.
These bounds pass to $B'$ at boundary points that are not rational as
follows. Let $s$ be a boundary point of
degree $d$ and $y$ a rational point of the dual line. The geometric
points over $s$ contribute $d$ summands to $B'_{\bar y}$, which
$\operatorname{Frob}_y$ permutes cyclically, and its $d$th power acts
on one summand as $\operatorname{Frob}_s$ on $B_{\bar s}$ times a root
of unity coming from the character sheaf. Hence every eigenvalue
$\beta$ of $\operatorname{Frob}_y$ on these summands satisfies
$\beta^d=\zeta\alpha$, with $\zeta$ a root of unity and $\alpha$ an
eigenvalue of $\operatorname{Frob}_s$, so that
$|\iota\alpha|\le q^{dw/2}$. It follows that $|\iota\beta|\le q^{w/2}$.
At a point $y$ of higher degree the same argument applies with $q$
replaced by the cardinality of $\kappa(y)$.

It remains to construct a filtration of $B'$ with pure quotients.
Choose for each boundary point, over its
residue field, a Frobenius-stable full flag of the coefficient module,
which exists because $\overline{\mathbf Q}_\ell$ is algebraically closed. Frobenius acts
on each successive quotient, a line, by one of its eigenvalues.
Tensoring with
the linear character sheaves and summing over the Frobenius orbit, we
obtain a finite Weil filtration of $B'$ whose quotients are pure of
the weights of the coefficient eigenvalues, and these weights are at
most $w$.
