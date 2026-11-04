+++
kind = "proof"
of = "lemma-fourier-transform-boundary-sequence"
order = 1268
uses = ["proposition-weights-j-boundary-points", "lemma-extreme-degrees-affine-curve", "proposition-base-change-fourier-inversion", "proposition-fourier-transform-middle-extension"]
+++
The three assertions are of different kinds. That the transform
of $j_!M$ is a single sheaf is a vanishing statement for the
cohomology of the twisted sheaves $M\otimes\mathcal L_{\psi(yx)}$ on
$U$. The exact sequence comes from transforming the boundary sequence
$0\to j_!M\to j_*M\to B\to0$ term by term. The
bound on $B'$ comes from the stalks of $B$, which are known from
Proposition [proposition-weights-j-boundary-points].

For $G$, the stalk formula
of Proposition [proposition-base-change-fourier-inversion] says that
the stalk of $\operatorname{FT}_\psi(j_!M)$ at $y$ is
$R\Gamma_c(U,M\otimes\mathcal L_{\psi(yx)})[1]$, so we must show that
only $H^1_c$ is nonzero. We apply
Lemma [lemma-extreme-degrees-affine-curve] to the lisse
sheaf $M\otimes\mathcal L_{\psi(yx)}$ on the affine curve $U$, with $j$
the identity. It shows that the group in degree zero vanishes and that
the group in degree two is a twist of
the coinvariants of geometric monodromy on
$M\otimes\mathcal L_{\psi(yx)}$. A nonzero coinvariant would be a
geometric quotient of $M$ isomorphic to $\mathcal L_{\psi(-yx)}$.
Our assumption on $M$ excludes such a constituent, and so
the group in degree two vanishes as well. The shift places the
remaining group $H^1_c$ in degree zero, and the transform is a sheaf
$G$.

The transform of $B$ is computed point by point. After geometric base
change, the punctual sheaf
$B$ is a finite sum of skyscrapers with coefficient modules, and the
transform of each skyscraper is a linear character sheaf tensored with
that module and shifted by one. Since a linear character sheaf is lisse
on the whole dual line, $\operatorname{FT}_\psi(B)=B'[1]$ with $B'$ lisse.

Applying the Fourier transform to the triangle obtained from
$0\to j_!M\to j_*M\to B\to0$, and using
Proposition [proposition-fourier-transform-middle-extension] for the
middle term, we obtain a triangle
$G\to j'_*M'\to B'[1]\to$. Here $G$ and $j'_*M'$ are sheaves in degree
zero, and $B'[1]$ is a sheaf in degree $-1$. Hence the long exact
sequence of cohomology sheaves has only three nonzero terms, and it is
the stated exact sequence.

The weights of $B'$ come from those of $B$, which are at
most $w$ by Proposition [proposition-weights-j-boundary-points].
Here we use that a character sheaf has weight zero. Only at boundary
points that are not rational does this need an argument. Let $s$ be a
boundary point of
degree $d$ and $y$ a rational point of the dual line. The geometric
points over $s$ contribute $d$ summands to $B'_{\bar y}$, which
$\operatorname{Frob}_y$ permutes cyclically. Its $d$th power acts
on one summand as $\operatorname{Frob}_s$ on $B_{\bar s}$ times a root
of unity coming from the character sheaf. Every eigenvalue
$\beta$ of $\operatorname{Frob}_y$ on these summands therefore satisfies
$\beta^d=\zeta\alpha$, with $\zeta$ a root of unity and $\alpha$ an
eigenvalue of $\operatorname{Frob}_s$. Since
$|\iota\alpha|\le q^{dw/2}$, we get $|\iota\beta|\le q^{w/2}$.
At a point $y$ of higher degree we replace $q$ by the cardinality of
$\kappa(y)$.

For a filtration of $B'$ with pure quotients, choose for each boundary
point, over its
residue field, a Frobenius-stable full flag of the coefficient module,
which exists because $\overline{\mathbf Q}_\ell$ is algebraically closed. Each successive
quotient is a line, on which Frobenius acts by one of its eigenvalues.
Tensoring with the linear character sheaves and summing over the
Frobenius orbit, we
obtain a finite Weil filtration of $B'$ whose quotients are pure of
the weights of the coefficient eigenvalues. These weights are at
most $w$.
