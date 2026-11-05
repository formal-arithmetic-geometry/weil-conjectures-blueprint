+++
id = "prose-14-01"
kind = "hidden"
title = "Weights and Deligne's theorem"
order = 626
+++
By the trace formula, the zeta function of $X_0$ is an alternating
product of the characteristic polynomials of Frobenius on the groups
$H^i_c(X,\overline{\mathbf Q}_\ell)$ (Section [sec-tf-determinants]), and the Riemann hypothesis
is a statement about the absolute values of their reciprocal roots.
These roots are $\ell$-adic numbers, and an $\ell$-adic number has no
complex absolute value until we choose a field embedding
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$. No choice is preferred, so we fix
one $\iota$ throughout, and the final theorems hold for every choice. An
eigenvalue $\alpha$ of Frobenius at a closed point of degree $n$ has
weight $w$ if $|\iota(\alpha)|=q^{nw/2}$. The factor $n$ makes the
weight independent of the field over which we look at the point: over
$\mathbf F_{q^{mn}}$ the eigenvalue becomes $\alpha^m$ and $q^n$ becomes
$q^{mn}$.

The examples to keep in mind come from curves. On $\mathbf P^1$,
Frobenius acts on $H^0$ by $1$ and on $H^2=\overline{\mathbf Q}_\ell(-1)$ by $q$, so these
groups have weights $0$ and $2$. For the elliptic curve
$y^2=x^3-x$ over $\mathbf F_3$ of the introduction, the eigenvalues
$\pm i\sqrt3$ on $H^1$ have weight $1$. Weil's purity axiom says that
this pattern persists: $H^i$ of a smooth proper variety is pure of
weight $i$. The name comes from Hodge theory, where $H^i$ of a compact
Kähler manifold carries a Hodge structure of weight $i$, and the idea
that the cohomology of every variety should be built from pure pieces
of different weights is Grothendieck's; Deligne made it precise, in the
$\ell$-adic setting, in [deligne80]. For a variety that is not
smooth and proper, cohomology need not be pure. If
$\mathbf G_m=\mathbf P^1\setminus\{0,\infty\}$, the localization
sequence gives $H^1_c(\mathbf G_m,\overline{\mathbf Q}_\ell)=\overline{\mathbf Q}_\ell$ with trivial Frobenius
and $H^2_c(\mathbf G_m,\overline{\mathbf Q}_\ell)=\overline{\mathbf Q}_\ell(-1)$, and the trace formula reads
$q-1=\#\mathbf G_m(\mathbf F_q)$. Thus $H^1_c$ has weight $0$, strictly
less than $1$. What remains true in general is an upper bound, and
Deligne's theorem is stated in that form.

The Part opening explains why the theorem has to be stated for all
sheaves and complexes. To state it we need three notions
(Definition [sk-d-real-weights]). A sheaf
is pure of weight $w$ if all its eigenvalues at all closed points have
weight $w$, and mixed if it has a finite filtration whose quotients are
pure. A bounded complex $K$ has weights at most $w$ if each
$\mathcal H^i(K)$ is mixed with all weights at most $w+i$. The shift by
$i$ is chosen so that the constant sheaf, which has weight $0$, and its
cohomology fit into one statement: the complex $R\Gamma_c(X,\overline{\mathbf Q}_\ell)$ has
weights at most $0$ exactly when $H^i_c$ has weights at most $i$, as on
$\mathbf G_m$. Deligne's theorem
(Theorem [sk-cor-dl-general-complex]) then says that for every
separated morphism of finite type $f:X_0\to Y_0$, the direct image
$Rf_!$ carries complexes of weights at most $w$ on $X_0$ to complexes
of weights at most $w$ on $Y_0$.

Two warnings will matter later. First, weights depend on
$\iota$. The rank-one Weil sheaf on $\operatorname{Spec}\mathbf F_q$ on
which Frobenius acts by $1+\sqrt2\in \overline{\mathbf Q}_\ell$ has weight $2\log_q(1+\sqrt2)>0$ for
an embedding with $\iota(\sqrt2)=\sqrt2$, and weight
$2\log_q(\sqrt2-1)=-2\log_q(1+\sqrt2)$ for the other one. Only because
Deligne's theorem holds for every $\iota$ do we learn, in
Theorem [sk-thm-weil-final], that the reciprocal roots of $P_i$
have absolute value $q^{i/2}$ under every complex embedding. Second,
being mixed is not a pointwise condition: it asks for a filtration with
pure quotients, which we must construct. That every sheaf has one is a
much deeper theorem of Lafforgue. For the direct images of
Section [sec-deligne-laumon-general], constructing the filtration is where the
work lies.

The first subsection defines weights and shows how they behave under
duals, tensor products, inverse images, shifts and twists
(Proposition [sk-r-real-linear]). The second states Deligne's theorem
and explains how the following sections prove it (Section [sec-wdef-route]).

We define weights on Weil sheaves, sheaves on $X$ with a Frobenius
structure, rather than on sheaves on $X_0$, because normalizing weights
requires twisting by the rank-one Weil sheaves $\mathcal B_b$, on which
a degree-one Frobenius acts by a scalar $b$, and these do not come from
$X_0$ when $b$ is not an $\ell$-adic unit.
