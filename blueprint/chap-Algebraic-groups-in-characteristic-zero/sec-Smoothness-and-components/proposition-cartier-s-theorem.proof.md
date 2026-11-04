+++
kind = "proof"
of = "proposition-cartier-s-theorem"
order = 1712
+++
We first show, using translations, that the reduced subscheme
$G_{\mathrm{red}}$ is a smooth group scheme. It then suffices to show
that $G$ has the same tangent space at $1$ as $G_{\mathrm{red}}$, that
is, that nilpotent functions at $1$ lie in $\mathfrak m^2$, and this is
where we divide by an integer.

*Step 1: $G_{\mathrm{red}}$ is a smooth subgroup scheme of $G$.*
Multiplication and inversion restrict to $G_{\mathrm{red}}$. This is
because products of reduced schemes of finite type over the perfect
field $\Omega$ are reduced [Stacks, [035Z](https://stacks.math.columbia.edu/tag/035Z)], and a morphism from a
reduced scheme to $G$ factors through $G_{\mathrm{red}}$. The reduced scheme
$G_{\mathrm{red}}$ contains a dense
smooth open subscheme [Stacks, [056V](https://stacks.math.columbia.edu/tag/056V)]. It is smooth everywhere, since a
translation moves a closed point of this open to any other closed point of
$G_{\mathrm{red}}$.

*Step 2: nilpotent functions at $1$ lie in $\mathfrak m^2$.* Let
$R=\mathcal O_{G,1}$, with maximal ideal $\mathfrak m$ and nilradical
$I$, and let $\widehat R$ be its completion. At the point $(1,1)$ the
multiplication induces a continuous comultiplication

$$
\Delta:\widehat R\longrightarrow
\widehat R\,\widehat\otimes_\Omega\widehat R.
$$

The counit is evaluation at $1$, and composing $\Delta$ with evaluation at $1$
in either factor gives the identity (the counit identities), because $1$ is a
two-sided unit for the group law.
We claim that $I\subseteq\mathfrak m^2$.
As completion is faithfully flat, it suffices to prove that every
nilpotent $b\in\widehat R$ lies in $\widehat{\mathfrak m}^{\,2}$.
Suppose that $b\notin\widehat{\mathfrak m}^{\,2}$, and let $n\ge2$ be
the least integer with $b^n=0$. By the counit identities,

$$
\Delta(b)=b\otimes1+1\otimes b+w,
\qquad
w\in\widehat{\mathfrak m}\,\widehat\otimes_\Omega
\widehat{\mathfrak m}.
$$

Now reduce the second factor modulo $\widehat{\mathfrak m}^{\,2}$. Every
term in the binomial expansion of $\Delta(b)^n$ with at least two
factors from $1\otimes b+w$ vanishes, because
$1\otimes b+w$ has its second factor in $\widehat{\mathfrak m}$, and as $b^n=0$
we are left with

$$
n b^{n-1}\otimes b+n(b^{n-1}\otimes1)w=0.
$$

If we now also reduce the first factor modulo
$b^{n-1}\widehat{\mathfrak m}$, the second term vanishes, and we get

$$
n\,\overline{b^{n-1}}\otimes\overline b=0
\quad\text{in}\quad
(\widehat R/b^{n-1}\widehat{\mathfrak m})
\otimes_\Omega(\widehat R/\widehat{\mathfrak m}^{\,2}).
$$

This identity is impossible, which proves the claim. Indeed, the module
$(b^{n-1})$ is nonzero by the choice of $n$, so the class
$\overline{b^{n-1}}$ is nonzero by Nakayama's lemma. The class
$\overline b$ is nonzero by assumption. A tensor product of nonzero
vectors over a field is nonzero, and $n\ne0$ in characteristic zero.

*Step 3: $G$ is smooth.* The schemes $G$ and $G_{\mathrm{red}}$ have the
same cotangent space at $1$. Indeed, by Step 2 the kernel of
$\mathfrak m/\mathfrak m^2\to(\mathfrak m/I)/(\mathfrak m/I)^2$ is
$(I+\mathfrak m^2)/\mathfrak m^2=0$. They also have the same local
dimension at $1$, because a nilpotent ideal does not change the
underlying space. As the local ring $R/I$ of $G_{\mathrm{red}}$ at $1$
is regular by Step 1, we get

$$
\dim_\Omega\mathfrak m/\mathfrak m^2=\dim R,
$$

so $R$ is regular, and in particular a domain [Stacks, [00NP](https://stacks.math.columbia.edu/tag/00NP)].
By translation the local rings of $G$ at all closed points are
regular. Since $\Omega$ is perfect, $G$ is smooth at every closed point.
The nonsmooth locus is closed and contains no closed point, and hence it
is empty. Being smooth, $G$ is reduced, and its tangent
space at $1$ has dimension $\dim G$. The open subgroup $G^\circ$ has the
same tangent space at $1$.
